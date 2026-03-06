import requests
from urllib.parse import urljoin
from config import BASE_URL


class ApiClient:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def _build_url(self, endpoint: str) -> str:
        return urljoin(BASE_URL.rstrip("/") + "/", endpoint.lstrip("/"))

    def get(self, endpoint, **kwargs):
        return self.session.get(self._build_url(endpoint), **kwargs)

    def post(self, endpoint, **kwargs):
        return self.session.post(self._build_url(endpoint), **kwargs)

    def put(self, endpoint, **kwargs):
        return self.session.put(self._build_url(endpoint), **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(self._build_url(endpoint), **kwargs)