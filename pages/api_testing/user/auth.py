import requests

from pages.api_testing.base_class import BaseClass


class Auth(BaseClass):
    data = {'username': 'JScofy', 'password': 'qwerty14145'}
    expected_text = "logged in user session:"

    def auth_user(self):
        self.response = requests.get('https://petstore.swagger.io/v2/user/login', params=self.data)
        self.response_json = self.response.json()

    def check_response_status(self):
        return self.expected_text in self.response_json['message']
