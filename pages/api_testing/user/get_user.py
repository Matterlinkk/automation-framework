import requests

from pages.api_testing.base_class import BaseClass


class GetUser(BaseClass):

    def get_user_by_nickname(self):
        self.response = requests.get('https://petstore.swagger.io/v2/user/JScofy')
        self.response_json = self.response.json()

    def check_nickname(self):
        return self.response_json['username'] == 'JScofy'