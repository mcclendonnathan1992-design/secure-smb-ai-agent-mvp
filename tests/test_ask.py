from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

MOCK_ANSWER = "You get 15 days of PTO per year."


def test_ask_valid_question():
    with patch("app.main.ask", return_value=MOCK_ANSWER):
        response = client.post("/ask", json={"question": "How much PTO do employees get?"})
    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == MOCK_ANSWER
    assert isinstance(data["sources"], list)


def test_ask_empty_question():
    response = client.post("/ask", json={"question": ""})
    assert response.status_code == 422


def test_ask_missing_field():
    response = client.post("/ask", json={})
    assert response.status_code == 422


def test_ask_wrong_type():
    response = client.post("/ask", json={"question": 12345})
    assert response.status_code == 422


def test_ask_source_grounding():
    with patch("app.main.ask", return_value=MOCK_ANSWER):
        response = client.post("/ask", json={"question": "What is the PTO policy?"})
    assert response.status_code == 200
    sources = response.json()["sources"]
    assert any("hr_policy" in s for s in sources)
