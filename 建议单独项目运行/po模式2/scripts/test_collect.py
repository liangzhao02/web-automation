import unittest
from selenium import webdriver
from time import sleep
from page.user_page import UserPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.news_page import NewsPage

class TestCollect(unittest.TestCase):

    def setUp(self):
        """
        初始化
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.1.18:9999/")
        self.driver.maximize_window()

        self.user_page = UserPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.news_page = NewsPage(self.driver)

    def tearDown(self):
        """
        结束
        :return:
        """
        sleep(3)
        self.driver.quit()

    def test_collect(self):
        """
        收藏
        :return:
        """
        # 点击登录
        self.home_page.click_login()

        # 输入账号
        self.login_page.input_mobile("15296797153")

        # 输入密码
        self.login_page.input_password("123456")

        # 点击登录
        self.login_page.click_login()

        # 点击新闻
        sleep(2)
        self.home_page.click_news()

        # 点击收藏
        self.news_page.click_collect()

        # 点击用户名
        self.home_page.click_username()

        # 点击我的收藏
        self.user_page.click_my_collect()

        # 切换frame
        self.user_page.get_frame()

        # 断言
        assert '申度量化数据报告1.17' in self.user_page.get_news()