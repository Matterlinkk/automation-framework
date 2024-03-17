import requests

from pages.api_testing.base_class import BaseClass


class UpdateUser(BaseClass):
    expected_result = "test_lastname"

    user_json = None

    changed_json = {
        "id": 14145,
        "username": "JScofy",
        "firstName": "John",
        "lastName": expected_result,
        "email": "johnscofield14145@gmail.com",
        "password": "qwerty14145",
        "phone": "447520662094",
        "userStatus": 0
    }

    def update_user(self):
        self.response = requests.put('https://petstore.swagger.io/v2/user/JScofy', json=self.changed_json)
        self.response_json = self.response.json()

    def get_user(self):
        self.user_json = requests.get('https://petstore.swagger.io/v2/user/JScofy').json()

    def check_nickname(self):
        return self.user_json['lastName'] == self.expected_result
