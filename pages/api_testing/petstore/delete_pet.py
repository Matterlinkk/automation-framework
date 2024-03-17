import requests

from pages.api_testing.base_class import BaseClass


class DeletePet(BaseClass):

    def delete_pet(self):
        self.response = requests.delete('https://petstore.swagger.io/v2/pet/1554')
        self.response_json = self.response.json()

    def is_id_correct(self):
        return self.response_json['message'] == '1554'
