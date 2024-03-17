import requests

from pages.api_testing.base_class import BaseClass


class FindByStatus(BaseClass):

    def get_pets(self, status):
        self.response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params='status={}'.format(status))
        self.response_json = self.response.json()

    def is_status(self, status):
        return self.response_json[0]['status'] == status
