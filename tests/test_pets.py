from fastapi.testclient import TestClient
from src.main import app
from src.config import API_KEY


client = TestClient(app)
headers = {"x-api-key": API_KEY}


def test_add_pet():
    # TestCase 1 add pet

    pet = {"name": "Tommy", "age": 2, "type": "cat"}

    response = client.post("pets/", json=pet, headers=headers)

    assert response.status_code == 200


def test_get_pets():
    # TestCase 2 get pets

    response = client.get("pets/", headers=headers)

    assert response.status_code == 200
