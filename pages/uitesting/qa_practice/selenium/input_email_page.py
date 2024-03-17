from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.uitesting.qa_practice.selenium.base_page import BasePage

input_field_args = (By.CSS_SELECTOR, 'input[class="textinput textInput form-control"]')
result_text_args = (By.CSS_SELECTOR, 'p[class="result-text"]')


class EmailInputPage(BasePage):
    def __init__(self, browser, email):
        super().__init__(browser)
        self.email = email

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/input/email')

    @property
    def __input(self):
        return self.find(input_field_args)

    def paste_text_to_input(self):
        self.__input.send_keys(self.email)
        self.__input.send_keys(Keys.ENTER)

    @property
    def result_text(self):
        return self.find(result_text_args).text
