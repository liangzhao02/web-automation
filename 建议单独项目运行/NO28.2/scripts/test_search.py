import unittest
from selenium import webdriver
from time import sleep
from page.click_page import ClickPage
from page.home_page import HomePage
from page.search_results_page import SearchResultsPage

class TestSearch(unittest.TestCase):
    def setUp(self):
        """
        初始化
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()

        self.click_page = ClickPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)

    def tearDown(self):
        """
        结束
        :return:
        """
        sleep(3)
        self.driver.quit()

    def test_search(self):
        # 点击左上角hao123
        self.home_page.click_hao123()
        # 切换新窗口
        sleep(3)
        handle_x = self.driver.window_handles
        self.driver.switch_to.window(handle_x[-1])
        sleep(3)
        # 搜索框输入国庆节
        self.click_page.input_something("国庆节")
        # 点击搜索
        self.click_page.click_search()
        sleep(3)
        # 跳转新窗口
        handle_y = self.driver.window_handles
        self.driver.switch_to.window(handle_y[-1])
        sleep(3)
        assert '国庆节 - 百度百科' in self.search_results_page.get_news()
        # 断言