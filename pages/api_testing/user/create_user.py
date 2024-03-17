import requests

from pages.api_testing.base_class import BaseClass


class CreateUser(BaseClass):
    json_user = [
        {
            "id": 14145,
            "username": "JScofy",
            "firstName": "John",
            "lastName": "Scofield",
            "email": "johnscofield14145@gmail.com",
            "password": "qwerty14145",
            "phone": "447520662094",
            "userStatus": 0
        }
    ]

    def create_user(self):
        self.response = requests.post('https://petstore.swagger.io/v2/user/createWithList', json=self.json_user)
        self.response_json = self.response.json()

    def check_response_status(self):
        return self.response_json['message'] == 'ok'
