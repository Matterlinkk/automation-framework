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
        self.browser.get('https://www.qa-practice.com/elements/popup/modal')
    
    @property
    def __launch_pop_up(self):
        return self.find(launch_pop_up_args)

    def click_launch_pop_up(self):
        self.__launch_pop_up.click()

    @property
    def __checkbox(self):
        return self.find(checkbox_args)

    def click_checkbox(self):
        self.__checkbox.click()

    @property
    def __send_button(self):
        return self.find(send_button_args)

    def click_send_button(self):
        self.__send_button.click()

    @property
    def result_text(self):
        return self.find(result_text_args).text
