from selenium.webdriver.support.select import Select

from pages.uitesting.qa_practice.selenium.base_page import BasePage
from selenium.webdriver.common.by import By

drop_down_list_args_1 = (By.CSS_SELECTOR, 'select[id="id_choose_the_place_you_want_to_go"]')
drop_down_list_args_2 = (By.CSS_SELECTOR, 'select[id="id_choose_how_you_want_to_get_there"]')
drop_down_list_args_3 = (By.CSS_SELECTOR, 'select[id="id_choose_when_you_want_to_go"]')
submit_button_args = (By.CSS_SELECTOR, 'input[id="submit-id-submit"]')
result_text = (By.CSS_SELECTOR, 'p[id="result-text"]')


class MultSelectPage(BasePage):
    def __init__(self, browser, marker_1, marker_2, marker_3):
        super().__init__(browser)
        self.marker_1 = marker_1
        self.marker_2 = marker_2
        self.marker_3 = marker_3

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/select/mult_select')

    @property
    def __drop_down_list_1(self):
        return self.find(drop_down_list_args_1)

    @property
    def __drop_down_list_2(self):
        return self.find(drop_down_list_args_2)

    @property
    def __drop_down_list_3(self):
        return self.find(drop_down_list_args_3)

    def change_drop_down_list_to_marker_values(self):
        state = Select(self.__drop_down_list_1)
        state.select_by_visible_text(self.marker_1)

        state = Select(self.__drop_down_list_2)
        state.select_by_visible_text(self.marker_2)

        state = Select(self.__drop_down_list_3)
        state.select_by_visible_text(self.marker_3)

    @property
    def __button(self):
        return self.find(submit_button_args)

    def click_button(self):
        self.__button.click()

    @property
    def result_text(self):
        return self.find(result_text).text
