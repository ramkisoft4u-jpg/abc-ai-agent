from typing import Dict, Any
from langchain_huggingface import HuggingFaceEndpoint
from app.config import settings
from app.rag.pipeline import get_retriever
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate


def get_llm():
    if settings.USE_GROQ:
        from groq import Groq
        from langchain.llms.base import LLM

        class GroqLLM(LLM):
            client: Groq

            @property
            def _llm_type(self) -> str:
                return "groq"

            def _call(self, prompt: str, stop=None):
                resp = self.client.chat.completions.create(
                    model=settings.GROQ_MODEL,
                    messages=[{"role": "user", "content": prompt}],
                )
                return resp.choices[0].message.content

        client = Groq(api_key=settings.GROQ_API_KEY)
        return GroqLLM(client=client)

    return HuggingFaceEndpoint(
        repo_id=settings.HF_LLM_MODEL,
        temperature=0.2,
        max_new_tokens=512,
        huggingfacehub_api_token=settings.HF_API_KEY,
    )


_orchestrator_prompt = ChatPromptTemplate.from_template(
    """You are the OrchestratorAgent for ABC.

User query:
{query}

Task:
1. Decide intent:
   - "create_order_with_reservation" if user wants to check doses, hold, and order.
   - "delete_reservation" if user wants to delete/unhold a reservation.
2. Extract:
   - product_id or prod_sale_use_num
   - date (yyyy-MM-dd if possible)
   - quantity (if mentioned)
   - reservation_id (if mentioned)

Return a JSON object with keys:
intent, product_id, prod_sale_use_num, date, quantity, reservation_id.
Do not include any other text.
"""
)


def orchestrator_node(state: Dict[str, Any]) -> Dict[str, Any]:
    llm = get_llm()
    retriever = get_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": _orchestrator_prompt},
    )
    result = qa({"query": state["user_query"]})
    import json

    try:
        parsed = json.loads(result["result"])
    except Exception:
        parsed = {"intent": None}

    state["intent"] = parsed.get("intent")
    state["product_id"] = parsed.get("product_id")
    state["prod_sale_use_num"] = parsed.get("prod_sale_use_num")
    state["date"] = parsed.get("date")
    state["quantity"] = parsed.get("quantity")
    state["reservation_id"] = parsed.get("reservation_id")
    return state
