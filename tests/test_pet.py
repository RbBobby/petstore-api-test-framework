import random


def test_create_and_get_pet(pet_api):

    pet_id = random.randint(10000, 99999)

    pet_data = {
        "id": pet_id,
        "name": "doggie",
        "status": "available"
    }

    # create pet
    create_response = pet_api.create_pet(pet_data)
    assert create_response.status_code == 200

    # get pet
    get_response = pet_api.get_pet(pet_id)

    assert get_response.status_code == 200
    assert get_response.json()["name"] == "doggie"