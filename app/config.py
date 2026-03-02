from pydantic import BaseSettings


class Settings(BaseSettings):
    HF_API_KEY: str | None = None
    HF_LLM_MODEL: str = "mistralai/Mistral-7B-Instruct-v0.2"
    HF_EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    USE_GROQ: bool = False
    GROQ_API_KEY: str | None = None
    GROQ_MODEL: str = "llama-3.1-70b-versatile"

    ABC_API_BASE_URL: str = "https://api.dev.cardinalhealth.net/nphs/abc-experience/v1/api"
    ABC_API_BEARER_TOKEN: str

    MYSQL_URL: str = "mysql+pymysql://user:password@localhost:3306/abc"

    VECTOR_DB_PATH: str = "data/rag/vectorstore/faiss_index"

    class Config:
        env_file = ".env"


settings = Settings()
