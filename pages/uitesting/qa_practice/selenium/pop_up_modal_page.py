import allure
from selenium.webdriver.common.by import By
from pages.uitesting.qa_practice.selenium.base_page import BasePage

launch_pop_up_args = (By.CSS_SELECTOR, 'button[data-bs-toggle="modal"]')
checkbox_args = (By.CSS_SELECTOR, 'input[class="form-check-input"]')
send_button_args = (By.CSS_SELECTOR, 'button[form="id-checkbox-form"]')
result_text_args = (By.CSS_SELECTOR, 'p[id="result-text"]')


class PopUpModalPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open the web page'):
            self.browser.get('https://www.qa-practice.com/elements/popup/modal')
    
    @property
    def __launch_pop_up(self):
        with allure.step('Find "Launch pop-up" button'):
            return self.find(launch_pop_up_args)

    def click_launch_pop_up(self):
        with allure.step('Click "Launch pop-up" button'):
            self.__launch_pop_up.click()

    @property
    def __checkbox(self):
        with allure.step('Find checkbox'):
            return self.find(checkbox_args)

    def click_checkbox(self):
        with allure.step('Click checkbox'):
            self.__checkbox.click()

    @property
    def __send_button(self):
        with allure.step('Find "Send" button'):
            return self.find(send_button_args)

    def click_send_button(self):
        with allure.step('Click "Send" button'):
            self.__send_button.click()

    @property
    def result_text(self):
        with allure.step('Copy result text'):
            return self.find(result_text_args).text
