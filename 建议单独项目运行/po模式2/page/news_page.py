from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewsPage(BaseAction):

    collect_label = By.LINK_TEXT, '收藏'

    def click_collect(self):
        """
        点击收藏
        :return:
        """
        self.click(self.collect_label)
