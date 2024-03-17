import requests

from pages.api_testing.base_class import BaseClass


class CreateBook(BaseClass):
    data = {"firstname": "Alex", "lastname": "Forever"}
    data_date = {"checkin": "2023-01-01", "checkout": "2024-01-01"}

    book_id = None
    book_json = None

    # book create in fixture "created_book"
    def get_created_book_id(self):
        self.response = requests.get('https://restful-booker.herokuapp.com/booking/', params=self.data)
        self.response_json = self.response.json()
        self.book_id = self.response_json[0]['bookingid']

    def get_created_book(self):
        self.book_json = requests.get('https://restful-booker.herokuapp.com/booking/{}'.format(self.book_id)).json()

    def check_initials(self):
        return {"firstname": self.book_json['firstname'], "lastname": self.book_json['lastname']} == self.data

    def check_dates(self):
        return {"checkin": self.book_json['bookingdates']['checkin'], "checkout": self.book_json['bookingdates']['checkout']} == self.data_date
