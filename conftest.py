import pytest
import requests

from selenium import webdriver as webdriver_selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver as webdriver_appium
from appium.options.android import UiAutomator2Options
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


# selenuim
@pytest.fixture(scope='function')
def start_selenium_driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver_selenium.Chrome(options=options)

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


# appium
@pytest.fixture()
def driver_init():
    driver = startDriver()

    yield driver

    closeDriver(driver)


def startDriver():
    options = AppiumOptions()
    appium_server_url = 'http://127.0.0.1:4723'
    desired_capabilities = {
        "platformName": "Android",
        "deviceName": "Pixel 7a API 30",
        "noReset": True,
    }

    driver = webdriver_appium.Remote(appium_server_url,
                                     options=UiAutomator2Options().load_capabilities(desired_capabilities))
    return driver


def closeDriver(driver):
    if driver:
        tabs = driver.find_element(AppiumBy.ID, 'com.android.chrome:id/tab_switcher_button')
        tabs.click()

        option = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="More options"]')
        option.click()

        close_tabs = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Close all tabs"]')
        close_tabs.click()

        new_tab = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="New tab"]')
        new_tab.click()

        wait_for_url_bar = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]')))

        driver.tap([(539, 2336)])

        driver.quit()
