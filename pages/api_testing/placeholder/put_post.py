import requests

from pages.api_testing.base_class import BaseClass


class Update(BaseClass):
    data = {
        "userId": 1,
        "id": 1,
        "title": "test title",
        "body": "i don`t care about title and body for sure it`s only test value"
    }

    data_for_patch = {
        "userId": 123,
    }

    def put_post(self):
        self.response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=self.data)
        self.response_json = self.response.json()

    def patch_post(self):
        self.response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', json=self.data_for_patch)
        self.response_json = self.response.json()

    def compate_titles(self):
        return self.response_json['title'] == self.data['title']

    def compare_user_id(self):
        return self.response_json['userId'] == self.data_for_patch['userId']
