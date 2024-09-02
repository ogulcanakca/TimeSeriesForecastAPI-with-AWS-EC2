# tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_predict_no_file():
    response = client.post("/predict/")
    assert response.status_code == 422


def test_predict_invalid_file():
    response = client.post(
        "/predict/", files={"file": ("test.txt", b"invalid content")}
    )
    assert response.status_code == 400
