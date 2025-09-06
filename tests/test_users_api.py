import pytest
import sys
from utils.api_client import APIClient
# from utils.read_json_files import read_json
from conftest import read_json

print("PYTHONPATH:", sys.path)

@pytest.fixture(scope="module")
def api_client():
    return APIClient()


def test_get_users(api_client):
    response = api_client.get("users")
    assert response.status_code == 200
    assert len(response.json())>0
    print(f"\n{response.json()}")


def test_create_user(api_client):
    payload = {
      "name" : "prasanth",
      "username" : "qa user",
      "email": "test_email@gmail.com"
    }
    # payload = read_json("../data/create_user_data.json")
    print(f"\nPayload :: \n{payload}")
    response = api_client.post("users", payload)
    assert response.status_code == 201
    assert len(response.json()) > 0
    print(f"\n{response.json()}")
    response = api_client.get("users/10")
    assert response.status_code == 200
    assert len(response.json()) > 0
    print(f"\n{response.json()}")


def test_update_user(api_client):
    payload = read_json("create_user_data.json")
    print(f"\nPayload :: \n{payload}")
    response = api_client.put("users/10", payload)
    assert response.status_code == 200
    assert len(response.json()) > 0
    print(f"\n{response.json()}")


def delete(api_client):
    response = api_client.delete("users/10")
    assert response.status_code == 200


