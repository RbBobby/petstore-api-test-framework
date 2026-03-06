import random


def test_user_login(user_api):

    username = f"user_{random.randint(1000,9999)}"

    user_data = {
        "id": 0,
        "username": username,
        "firstName": "Alex",
        "lastName": "QA",
        "email": "alex@test.com",
        "password": "12345",
        "phone": "123456789",
        "userStatus": 1
    }

    # create user
    create_response = user_api.create_user(user_data)
    assert create_response.status_code == 200

    # login
    login_response = user_api.login(username, "12345")

    assert login_response.status_code == 200
    assert "logged in user session" in login_response.text