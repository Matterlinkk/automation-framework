import requests

from pages.api_testing.base_class import BaseClass


class DeleteUser(BaseClass):

    def delete_user(self):
        self.response = requests.delete('https://petstore.swagger.io/v2/user/JScofy')
        self.response_json = self.response.json()

    def check_nickname(self):
        return self.response_json['message'] == 'JScofy'
