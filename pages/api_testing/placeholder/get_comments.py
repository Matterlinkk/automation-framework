import requests

from pages.api_testing.base_class import BaseClass


class GetComments(BaseClass):
    expected_results = {
        1: "id labore ex et quam laborum",
        2: "quo vero reiciendis velit similique earum",
        3: "odio adipisci rerum aut animi"
    }

    def get_comments(self):
        self.response = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
        self.response_json = self.response.json()

    def check_comments(self):
        return {1: self.response_json[0]['name'], 2: self.response_json[1]['name'], 3: self.response_json[2]['name']} == self.expected_results
