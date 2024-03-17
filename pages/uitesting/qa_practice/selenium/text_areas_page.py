from selenium.webdriver.common.by import By
from pages.uitesting.qa_practice.selenium.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

chapter_1 = (By.CSS_SELECTOR, 'textarea[id="id_first_chapter"]')
chapter_2 = (By.CSS_SELECTOR, 'textarea[id="id_second_chapter"]')
chapter_3 = (By.CSS_SELECTOR, 'textarea[id="id_third_chapter"]')
submit_button = (By.CSS_SELECTOR, 'input[id="submit-id-submit"]')
result_text = (By.CSS_SELECTOR, 'p[id="result-text"]')
req_args = (By.CSS_SELECTOR, 'a[id="req_header"]')


class TextAreasPage(BasePage):
    def __init__(self, browser, args: list):
        super().__init__(browser)
        self.value1, self.value2, self.value3 = args

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/textarea/textareas')

    @property
    def __chapter_1(self):
        return self.find(chapter_1)

    @property
    def __chapter_2(self):
        return self.find(chapter_2)

    @property
    def __chapter_3(self):
        return self.find(chapter_3)

    def write_messages_to_chapters(self):
        self.__chapter_1.send_keys(self.value1)
        self.__chapter_2.send_keys(self.value2)
        self.__chapter_3.send_keys(self.value3)

    @property
    def __button(self):
        return self.find(submit_button)

    @property
    def __req(self):
        return self.find(req_args)

    def scroll_to(self):
        actions = ActionChains(self.browser)
        actions.move_to_element(self.__req).perform()

    def click_button(self):
        self.__button.click()

    @property
    def result_text(self):
        return self.find(result_text).text
