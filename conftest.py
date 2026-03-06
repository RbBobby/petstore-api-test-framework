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