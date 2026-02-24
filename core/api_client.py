import requests


class APIClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get(self, endpoint: str):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, timeout=10)
        return response