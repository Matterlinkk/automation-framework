from pages.uitesting.qa_practice.selenium.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

submit_button_args = (By.CSS_SELECTOR, 'a[class="a-button"]')
result_text_args = (By.CSS_SELECTOR, 'p[id="result-text"]')


class ConfirmAlertPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/alert/confirm#')

    @property
    def __button(self):
        return self.find(submit_button_args)

    def click_button(self):
        self.__button.click()

    def confirm_alert(self):
        alert = Alert(self.browser)
        alert.accept()

    def dismiss_alert(self):
        alert = Alert(self.browser)
        alert.dismiss()

    @property
    def result_text(self):
        return self.find(result_text_args).text
