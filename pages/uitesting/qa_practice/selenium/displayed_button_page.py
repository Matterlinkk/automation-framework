import allure
from selenium.webdriver.support.select import Select

from pages.uitesting.qa_practice.selenium.base_page import BasePage
from selenium.webdriver.common.by import By


drop_down_list_args = (By.CSS_SELECTOR, 'select[class="form-select"]')
submit_button_args = (By.CSS_SELECTOR, 'input[id="submit-id-submit"]')
result_text = (By.CSS_SELECTOR, 'p[id="result-text"]')


class DisplayedButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open the web page'):
            self.browser.get('https://www.qa-practice.com/elements/button/disabled')

    @property
    def __drop_down_list(self):
        with allure.step('Find dropdown list'):
            return self.find(drop_down_list_args)

    def change_drop_down_list_to_enable(self):
        with allure.step('Select state "enable" in dropdown list'):
            state = Select(self.__drop_down_list)
            state.select_by_value("enabled")

    @property
    def button(self):
        with allure.step('Find the button'):
            return self.find(submit_button_args)

    @property
    def result_text(self):
        with allure.step('Copy result value'):
            return self.find(result_text).text
