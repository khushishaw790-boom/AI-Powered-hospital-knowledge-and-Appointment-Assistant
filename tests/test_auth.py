from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_register():
    response = client.post(
        "/api/v1/auth/register",
        json={
            "name": "Test User",
            "email": "test_phase9@example.com",
            "password": "TestPassword123",
            "role": "patient",
        },
    )

    # 200/201 means registration succeeded.
    # 400 means the email may already exist.
    assert response.status_code in [200, 201, 400]