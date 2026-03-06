import random
import pytest

from api.client import ApiClient
from api.user_api import UserAPI
from api.pet_api import PetAPI


@pytest.fixture(scope="session")
def api_client():
    return ApiClient()


@pytest.fixture
def user_api(api_client):
    return UserAPI(api_client)


@pytest.fixture
def pet_api(api_client):
    return PetAPI(api_client)


@pytest.fixture
def user_payload():
    suffix = random.randint(10000, 99999)
    return {
        "id": suffix,
        "username": f"user_{suffix}",
        "firstName": "Alex",
        "lastName": "QA",
        "email": f"alex_{suffix}@test.com",
        "password": "12345",
        "phone": "123456789",
        "userStatus": 1,
    }


@pytest.fixture
def pet_payload():
    pet_id = random.randint(10000, 99999)
    return {
        "id": pet_id,
        "name": "doggie",
        "status": "available",
    }


@pytest.fixture
def created_user(user_api, user_payload):
    response = user_api.create_user(user_payload)
    assert response.status_code == 200
    yield user_payload
    user_api.delete_user(user_payload["username"])


@pytest.fixture
def created_pet(pet_api, pet_payload):
    response = pet_api.create_pet(pet_payload)
    assert response.status_code == 200
    yield pet_payload
    pet_api.delete_pet(pet_payload["id"])


@pytest.fixture
def valid_user_credentials(created_user):
    return created_user["username"], created_user["password"]


@pytest.fixture(params=[
    ("unknown_user_12345", "12345"),
    ("", "12345"),
    ("unknown_user_12345", ""),
])
def invalid_user_credentials(request):
    return request.param