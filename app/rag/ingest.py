from pathlib import Path
import os

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from app.rag.pipeline import get_embeddings
from app.config import settings


def load_docs():
    base_dir = Path("data/knowledge_base")
    loaders = [
        DirectoryLoader(str(base_dir), glob="**/*.pdf", loader_cls=PyPDFLoader),
        DirectoryLoader(str(base_dir), glob="**/*.md", loader_cls=TextLoader),
        DirectoryLoader(str(base_dir), glob="**/*.txt", loader_cls=TextLoader),
    ]
    docs = []
    for loader in loaders:
        docs.extend(loader.load())
    return docs


def ingest():
    docs = load_docs()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = get_embeddings()
    vs = FAISS.from_documents(chunks, embeddings)

    os.makedirs(os.path.dirname(settings.VECTOR_DB_PATH), exist_ok=True)
    vs.save_local(settings.VECTOR_DB_PATH)
    print("Vector store created at:", settings.VECTOR_DB_PATH)
