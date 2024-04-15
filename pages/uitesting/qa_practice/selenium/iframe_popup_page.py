import allure
from selenium.webdriver.common.by import By

from pages.uitesting.qa_practice.selenium.base_page import BasePage

launch_pop_up_args = (By.CSS_SELECTOR, 'button[data-bs-toggle="modal"]')
pop_up_args = (By.CSS_SELECTOR, 'iframe[class="embed-responsive-item"]')
coppied_text_args = (By.CSS_SELECTOR, 'p[id="text-to-copy"]')
check_button_args = (By.CSS_SELECTOR, 'button[form="empty-form"]')
input_text_args = (By.CSS_SELECTOR, 'input[class="textinput textInput form-control"]')
submit_button_args = (By.CSS_SELECTOR, 'input[class="btn btn-primary"]')
result_text_args = (By.CSS_SELECTOR, 'div[class="alert alert-success"]')


class IframePopUp(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def get_browser(self):
        return self.browser

    def open(self):
        with allure.step('Open the web page'):
            self.browser.get('https://www.qa-practice.com/elements/popup/iframe_popup')

    @property
    def __launch_pop_up(self):
        with allure.step('Find "Launch pop-up" button'):
            return self.find(launch_pop_up_args)

    def click_launch_popup(self):
        with allure.step('Click "Launch pop-up" button'):
            self.__launch_pop_up.click()

    @property
    def __pop_up(self):
        with allure.step('Find pop-up frame'):
            return self.find(pop_up_args)

    def switch_to_pop_up_frame(self):
        with allure.step('Change pop-up frame'):
            self.browser.switch_to.frame(self.__pop_up)

    def copy_text(self):
        with allure.step('Copy text from frame'):
            return self.find(coppied_text_args).text

    def switch_to_default(self):
        with allure.step('Switch driver to default frame'):
            self.browser.switch_to.default_content()

    @property
    def __check_button(self):
        with allure.step('Find button'):
            return self.find(check_button_args)

    def click_check_button(self):
        with allure.step('Click button'):
            self.__check_button.click()

    @property
    def __input_text_field(self):
        with allure.step('Find input field'):
            return self.find(input_text_args)

    def paste_text_to_input(self, text: str):
        with allure.step('Fill input field with text'):
            self.__input_text_field.clear()
            self.__input_text_field.send_keys(text)

    @property
    def __submit_button(self):
        with allure.step('Find "Submit" button'):
            return self.find(submit_button_args)

    def click_submit_button(self):
        with allure.step('Click "Submit" button'):
            self.__submit_button.click()

    @property
    def result_text(self):
        with allure.step('Copy result text'):
            return self.find(result_text_args).text
