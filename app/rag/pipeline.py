import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import settings


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=settings.HF_EMBEDDING_MODEL,
        huggingfacehub_api_token=settings.HF_API_KEY,
    )


def load_vectorstore():
    embeddings = get_embeddings()
    if os.path.exists(settings.VECTOR_DB_PATH):
        return FAISS.load_local(
            settings.VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True,
        )
    raise RuntimeError("Vector store not found. Run scripts/ingest_docs.py first.")


def get_retriever():
    vs = load_vectorstore()
    return vs.as_retriever(search_kwargs={"k": 4})
