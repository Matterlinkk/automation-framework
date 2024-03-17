import requests

from pages.api_testing.base_class import BaseClass


class GetPosts(BaseClass):

    expected_results = {
        1: "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        2: "qui est esse",
        3: "ea molestias quasi exercitationem repellat qui ipsa sit aut"
    }

    def get_posts(self):
        self.response = requests.get('https://jsonplaceholder.typicode.com/posts')
        self.response_json = self.response.json()

    def check_posts(self):
        return {1: self.response_json[0]['title'], 2: self.response_json[1]['title'], 3: self.response_json[2]['title']} == self.expected_results
