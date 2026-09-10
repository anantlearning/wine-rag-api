from unittest.mock import patch, MagicMock

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Wine RAG API is running"


def test_query_validation():
    response = client.post(
        "/query",
        json={"query": "a"}
    )

    assert response.status_code == 422


@patch("app.main.generate_answer")
@patch("app.main.build_context")
@patch("app.main.get_top_wines")
def test_query(mock_get_top_wines, mock_build_context, mock_generate_answer):

    # Mock Qdrant retrieval
    mock_get_top_wines.return_value = [
        MagicMock()
    ]

    # Mock context creation
    mock_build_context.return_value = "Mock wine context"

    # Mock Gemini response
    mock_generate_answer.return_value = "This wine is a good match."

    response = client.post(
        "/query",
        json={
            "query": "Suggest a Cabernet from Napa"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["query"] == "Suggest a Cabernet from Napa"
    assert data["answer"] == "This wine is a good match."

    # Verify each component was called
    mock_get_top_wines.assert_called_once()
    mock_build_context.assert_called_once()
    mock_generate_answer.assert_called_once()