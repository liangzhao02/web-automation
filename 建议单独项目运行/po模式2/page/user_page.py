from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class UserPage(BaseAction):

    collect_label = By.LINK_TEXT, "我的收藏"
    news_label = By.XPATH, '//ul[@class="article_list"]/li/a'

    def click_my_collect(self):
        """
        点击我的收藏
        :return:
        """
        self.click(self.collect_label)

    def get_frame(self):
        """
        切换frame
        :return:
        """
        self.driver.switch_to.frame("main_frame")

    def get_news(self):
        """
        获取新闻
        :return:
        """
        # 获取所有新闻 [元素1，元素2， 元素3]
        new_lists = self.find_elements(self.news_label)
        # 获取所有新闻标题
        news_title = [ele.text for ele in new_lists]

        return news_title