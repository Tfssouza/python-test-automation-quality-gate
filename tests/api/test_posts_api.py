from core.api_client import APIClient


def test_get_post_by_id_returns_200_and_expected_fields():
    client = APIClient()

    response = client.get("/posts/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "userId" in data
    assert "title" in data
    assert "body" in data