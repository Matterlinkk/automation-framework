import allure

from pages.uitesting.qa_practice.selenium.base_page import BasePage
from selenium.webdriver.common.by import By

link_args = (By.CSS_SELECTOR, 'a[id="new-page-link"]')
result_text_args = (By.CSS_SELECTOR, 'p[id="result-text"]')


class NewTabLinkPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open the web page'):
            self.browser.get('https://www.qa-practice.com/elements/new_tab/link')

    @property
    def __link(self):
        with allure.step('Find link'):
            return self.find(link_args)

    def click_link(self):
        with allure.step('Open the link in new tab'):
            self.__link.click()

    def switch_page(self):
        with allure.step('Change tab'):
            self.browser.execute_script("arguments[0].click();", self.__link)

            self.browser.switch_to.window(self.browser.window_handles[1])

    @property
    def result_text(self):
        with allure.step('Copy result text'):
            return self.find(result_text_args).text
