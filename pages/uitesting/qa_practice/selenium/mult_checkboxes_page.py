import allure

from pages.uitesting.qa_practice.selenium.base_page import BasePage
from selenium.webdriver.common.by import By

checkbox1_args = (By.CSS_SELECTOR, 'input[id="id_checkboxes_0"]')
checkbox2_args = (By.CSS_SELECTOR, 'input[id="id_checkboxes_1"]')
checkbox3_args = (By.CSS_SELECTOR, 'input[id="id_checkboxes_2"]')
submit_button_args = (By.CSS_SELECTOR, 'input[id="submit-id-submit"]')
result_text_args = (By.CSS_SELECTOR, 'p[id="result-text"]')


class MultCheckboxes(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open the web page'):
            self.browser.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')

    @property
    def __chechbox1(self):
        with allure.step('Find first checkbox'):
            return self.find(checkbox1_args)

    @property
    def __chechbox2(self):
        with allure.step('Find second checkbox'):
            return self.find(checkbox2_args)

    @property
    def __chechbox3(self):
        with allure.step('Find third checkbox'):
            return self.find(checkbox3_args)

    def click_all_checkboxes(self):
        with allure.step('Click checkboxes'):
            self.__chechbox1.click()
            self.__chechbox2.click()
            self.__chechbox3.click()

    @property
    def __button(self):
        with allure.step('Find button'):
            return self.find(submit_button_args)

    def click_button(self):
        with allure.step('Click button'):
            self.__button.click()

    @property
    def result_text(self):
        with allure.step('Copy result text'):
            return self.find(result_text_args).text
