import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# selenuim
@pytest.fixture(scope='function')
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--javascript")
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(10)

    return browser


# api_testing
@pytest.fixture(scope='function')
def create_pet_with_status_sold():
    """
    Create a pet with id 1554 for test_delete_pet function
    """

    pet_data = {
        "id": 1554,
        "category": {
            "id": 1554,
            "name": "Jake"
        },
        "name": "cartoon hero",
        "photoUrls": [
            "null"
        ],
        "tags": [
            {
                "id": 0,
                "name": "Adventure Time"
            }
        ],
        "status": 'sold'
    }

    requests.post('https://petstore.swagger.io/v2/pet', json=pet_data)


@pytest.fixture(scope='function')
def create_and_delete_with_status_pending():
    """
    Create and delete for function which get pet by ID
    """

    pet_data = {
        "id": 1456,
        "category": {
            "id": 1456,
            "name": "Biscuit"
        },
        "name": "animal",
        "photoUrls": [
            "null"
        ],
        "tags": [
            {
                "id": 0,
                "name": "cake"
            }
        ],
        "status": "pending"
    }

    requests.post('https://petstore.swagger.io/v2/pet', json=pet_data)

    yield None

    requests.delete('https://petstore.swagger.io/v2/pet/1456')


@pytest.fixture(scope='function')
def create_and_delete():
    """
    Create and delete for function which get pet by ID
    """

    pet_data = {
        "id": 1456,
        "category": {
            "id": 1456,
            "name": "Biscuit"
        },
        "name": "animal",
        "photoUrls": [
            "null"
        ],
        "tags": [
            {
                "id": 0,
                "name": "cake"
            }
        ],
        "status": "sold"
    }

    requests.post('https://petstore.swagger.io/v2/pet', json=pet_data)

    yield None

    requests.delete('https://petstore.swagger.io/v2/pet/1456')


@pytest.fixture(scope='function')
def create_user():
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

    requests.post('https://petstore.swagger.io/v2/user/createWithList', json=json_user)


@pytest.fixture(scope='function')
def create_and_delete_user():
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

    requests.post('https://petstore.swagger.io/v2/user/createWithList', json=json_user)

    yield

    requests.delete('https://petstore.swagger.io/v2/user/JScofy')


@pytest.fixture(scope='function')
def created_book():
    data = {
        "firstname": "Alex",
        "lastname": "Forever",
        "totalprice": 145,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "qwe"
    }

    requests.post('https://restful-booker.herokuapp.com/booking', json=data)
