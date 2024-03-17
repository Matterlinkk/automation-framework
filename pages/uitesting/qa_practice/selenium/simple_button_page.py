from pages.uitesting.qa_practice.selenium.base_page import BasePage

from selenium.webdriver.common.by import By

button_args = (By.CSS_SELECTOR, 'input[id="submit-id-submit"]')

result_args = (By.CSS_SELECTOR, 'p[id="result-text"]')


class SimpleButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/simple')

    @property
    def button(self):
        return self.find(button_args)

    @property
    def button_is_displayed(self):
        return self.button.is_displayed()

    @property
    def result_text(self):
        return self.find(result_args).text
