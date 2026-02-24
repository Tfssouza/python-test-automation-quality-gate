import requests


def test_get_post_by_id_returns_200_and_expected_fields():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url, timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "userId" in data
    assert "title" in data
    assert "body" in data