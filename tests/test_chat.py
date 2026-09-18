from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_chat_requires_authentication():
    response = client.post(
        "/api/v1/chat/",
        json={
            "question": "What departments does the hospital have?",
            "top_k": 3,
        },
    )

    assert response.status_code == 401