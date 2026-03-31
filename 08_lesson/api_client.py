import requests
import config


class ApiClient:
    def __init__(self):
        self.base_url = config.BASE_URL
        self.headers = config.get_headers()

    def post(self, endpoint, data):
        url = self.base_url + endpoint
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def put(self, endpoint, data):
        url = self.base_url + endpoint
        response = requests.put(url, json=data, headers=self.headers)
        return response

    def get(self, endpoint):
        url = self.base_url + endpoint
        response = requests.get(url, headers=self.headers)
        return response
