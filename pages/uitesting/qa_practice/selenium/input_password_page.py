import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.uitesting.qa_practice.selenium.base_page import BasePage

input_field_args = (By.CSS_SELECTOR, 'input[class="textinput textInput form-control"]')
result_text_args = (By.CSS_SELECTOR, 'p[id="result-text"]')


class PasswordInputPage(BasePage):
    def __init__(self, browser, password):
        super().__init__(browser)
        self.password = password

    def open(self):
        with allure.step('Open the web page'):
            self.browser.get('https://www.qa-practice.com/elements/input/passwd')

    @property
    def __input(self):
        return self.find(input_field_args)

    def paste_text_to_input(self):
        with allure.step('Fill the input-field'):
            self.__input.send_keys(self.password)
            self.__input.send_keys(Keys.ENTER)

    @property
    def result_text(self):
        with allure.step('Copy result text'):
            return self.find(result_text_args).text
