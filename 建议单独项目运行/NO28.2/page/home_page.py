from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    hao123_label = By.LINK_TEXT, 'hao123'

    def click_hao123(self):
        """
        点击hao123
        :return:
        """
        self.click(self.hao123_label)