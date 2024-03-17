import requests

from pages.api_testing.base_class import BaseClass


class FindById(BaseClass):

    def get_pet_by_id(self):
        self.response = requests.get('https://petstore.swagger.io/v2/pet/1456')
        self.response_json = self.response.json()

    def check_pet_name(self):
        return self.response_json['category']['name'] == 'Biscuit'
