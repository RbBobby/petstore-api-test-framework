class UserAPI:

    def __init__(self, client):
        self.client = client

    def create_user(self, user_data):
        return self.client.post("/user", json=user_data)

    def login(self, username, password):
        return self.client.get(
            "/user/login",
            params={
                "username": username,
                "password": password
            }
        )

    def logout(self):
        return self.client.get("/user/logout")

    def get_user(self, username):
        return self.client.get(f"/user/{username}")

    def delete_user(self, username):
        return self.client.delete(f"/user/{username}")