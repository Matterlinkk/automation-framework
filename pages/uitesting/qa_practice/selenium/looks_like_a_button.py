import allure
from selenium.webdriver.common.by import By
from pages.uitesting.qa_practice.selenium.base_page import BasePage

button_args = (By.CSS_SELECTOR, 'a[class="a-button"]')
result_args = (By.CSS_SELECTOR, 'p[id="result-text"]')


class LooksLikeAButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open the web page'):
            self.browser.get('https://www.qa-practice.com/elements/button/like_a_button')

    @property
    def button(self):
        with allure.step('Check button'):
            return self.find(button_args)

    @property
    def button_is_displayed(self):
        with allure.step('Check is displayed button'):
            return self.button.is_displayed()

    @property
    def result_text(self):
        with allure.step('Copy result text'):
            return self.find(result_args).text
