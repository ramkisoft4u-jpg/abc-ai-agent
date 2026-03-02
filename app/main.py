from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.graph.workflow import workflow
from app.schemas.chat import ChatRequest, WorkflowState

app = FastAPI(title="ABC AI Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
def chat(req: ChatRequest):
    state: WorkflowState = {
        "user_query": req.query,
        "intent": None,
        "product_id": None,
        "prod_sale_use_num": None,
        "date": None,
        "quantity": None,
        "reservation_id": None,
        "order_id": None,
        "messages": [],
    }
    final_state = workflow.invoke(state)
    return {
        "intent": final_state.get("intent"),
        "reservation_id": final_state.get("reservation_id"),
        "order_id": final_state.get("order_id"),
        "messages": final_state.get("messages"),
    }
