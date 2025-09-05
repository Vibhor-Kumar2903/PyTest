import pytest
import sys
from utils.api_client import APIClient

print("PYTHONPATH:", sys.path)

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get("users")
    assert response.status_code == 200
    assert len(response.json())>0
    print(response.json())


