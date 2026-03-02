from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_chat_endpoint():
    resp = client.post("/chat", json={"query": "test", "use_rag": False})
    assert resp.status_code == 200
