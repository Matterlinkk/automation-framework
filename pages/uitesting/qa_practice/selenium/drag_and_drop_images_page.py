from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from pages.uitesting.qa_practice.selenium.base_page import BasePage

drop_here_args = (By.CSS_SELECTOR, 'div[id="rect-droppable2"]')
drag_me_args = (By.CSS_SELECTOR, 'img[class="rect-draggable ui-draggable ui-draggable-handle"]')
result_text_args = (By.XPATH, '//*[@id="rect-droppable2"]/p')


class DragAndDropImagePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/dragndrop/images')

    @property
    def __drag_object(self):
        return self.find(drag_me_args)

    @property
    def __coords(self):
        return self.find(drop_here_args)

    def drag_and_drop(self):
        action = ActionChains(self.browser)
        action.drag_and_drop(self.__drag_object, self.__coords).perform()

    @property
    def result_text(self):
        return self.find(result_text_args).text
