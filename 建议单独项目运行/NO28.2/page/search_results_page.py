from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchResultsPage(BaseAction):

    news_label = By.XPATH, '//a[@class]'
    def get_news(self):

        news_list = self.find_elements(self.news_label)
        news_title = [ele.text for ele in news_list]
        return news_title
