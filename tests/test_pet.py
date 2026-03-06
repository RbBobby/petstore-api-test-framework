import pytest


class TestPetApi:

    def test_create_and_get_pet(self, pet_api, created_pet):
        get_response = pet_api.get_pet(created_pet["id"])

        assert get_response.status_code == 200

        data = get_response.json()
        assert data["name"] == created_pet["name"]


    def test_delete_pet(self, pet_api, pet_payload):
        create_response = pet_api.create_pet(pet_payload)
        assert create_response.status_code == 200

        delete_response = pet_api.delete_pet(pet_payload["id"])
        assert delete_response.status_code == 200

        get_response = pet_api.get_pet(pet_payload["id"])
        assert get_response.status_code == 404