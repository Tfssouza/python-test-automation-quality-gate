import pytest
from core.api_client import APIClient
from core.data_loader import load_posts_test_data


@pytest.mark.parametrize("item", load_posts_test_data())
def test_get_post_by_id_data_driven(item):
    client = APIClient()

    response = client.get(f"/posts/{item['id']}")

    assert response.status_code == item["expected_status"]
