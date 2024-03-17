import requests

from pages.api_testing.base_class import BaseClass


class DeletePost(BaseClass):

    first_post_json = None

    def get_first_post(self):
        self.first_post_json = requests.get('https://jsonplaceholder.typicode.com/posts/1').json()

    def delete_post(self):

        self.response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
        self.response_json = self.response.json()

    def compare_posts(self):
        return self.first_post_json != self.response_json
