import pytest


class TestUserAuth:

    def test_user_login(self, user_api, created_user):
        response = user_api.login(
            created_user["username"],
            created_user["password"]
        )

        assert response.status_code == 200
        assert "logged in user session" in response.text


    def test_get_user_after_create(self, user_api, created_user):
        response = user_api.get_user(created_user["username"])

        assert response.status_code == 200
        body = response.json()

        assert body["username"] == created_user["username"]


    def test_get_unknown_user(self, user_api):
        response = user_api.get_user("unknown_user_999999")

        assert response.status_code == 404