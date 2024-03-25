from pages.uitesting.qa_practice.selenium.base_page import BasePage
from selenium.webdriver.common.by import By


start_button_selector = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-test"]')
progress_bar_selector = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')
stop_button_selector = (By.CSS_SELECTOR, 'button[class="btn btn-info btn-test"]')
result_text = (By.CSS_SELECTOR, 'p[id="result"]')


class ProgressBarPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('http://uitestingplayground.com/progressbar')

    @property
    def __start_button(self):
        return self.find(start_button_selector)

    def click_start(self):
        self.__start_button.click()

    def wait_for_progress_bar_75(self):
        while self.find(progress_bar_selector).text != '75%':
            pass

    @property
    def __stop_button(self):
        return self.find(stop_button_selector)

    def click_stop(self):
        self.__stop_button.click()

    @property
    def result_text(self):
        return int(self.find((By.CSS_SELECTOR, 'p[id="result"]')).text[8:9])
