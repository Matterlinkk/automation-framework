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

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/popup/iframe_popup')

    @property
    def __launch_pop_up(self):
        return self.find(launch_pop_up_args)

    def click_launch_popup(self):
        self.__launch_pop_up.click()

    @property
    def __pop_up(self):
        return self.find(pop_up_args)

    def switch_to_pop_up_frame(self):
        self.browser.switch_to.frame(self.__pop_up)

    def copy_text(self):
        return self.find(coppied_text_args).text

    def switch_to_default(self):
        self.browser.switch_to.default_content()

    @property
    def __check_button(self):
        return self.find(check_button_args)

    def click_check_button(self):
        self.__check_button.click()

    @property
    def __input_text_field(self):
        return self.find(input_text_args)

    def paste_text_to_input(self, text: str):
        self.__input_text_field.clear()
        self.__input_text_field.send_keys(text)

    @property
    def __submit_button(self):
        return self.find(submit_button_args)

    def click_submit_button(self):
        self.__submit_button.click()

    @property
    def result_text(self):
        return self.find(result_text_args).text
