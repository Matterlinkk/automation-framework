import requests

from pages.api_testing.base_class import BaseClass


class CreatePet(BaseClass):
    expected_result = "Brownie"

    pet_data = {
        "id": 1554,
        "category": {
            "id": 1554,
            "name": "Brownie"
        },
        "name": "animal",
        "photoUrls": [
            "null"
        ],
        "tags": [
            {
                "id": 0,
                "name": "goose"
            }
        ],
        "status": "available"
    }

    def create_pet(self):
        self.response = requests.post('https://petstore.swagger.io/v2/pet', json=self.pet_data)
        self.response_json = self.response.json()

    def check_pet_name(self):
        return self.response_json['category']['name'] == self.expected_result

