from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ClickPage(BaseAction):

    input_something_label = By.XPATH, '//input[@data-hook="searchInput"]'
    click_search_label = By.XPATH, '//input[@data-hook="searchSubmit"]'

    def input_something(self, value):
        """
        在搜索框输入内容
        :return:
        """
        self.send_keys(self.input_something_label, value)

    def click_search(self):
        """
        点击搜索
        :param value:
        :return:
        """
        self.click(self.click_search_label)