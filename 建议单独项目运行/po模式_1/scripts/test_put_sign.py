import unittest
from selenium import webdriver
from time import sleep
from page.login_page import LoginPage
from page.user_page import UserPage
from page.home_page import HomePage

class TestPutSign(unittest.TestCase):

    def setUp(self):
        """
        初始化
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.1.18:9999/')
        self.driver.maximize_window()

        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.user_page = UserPage(self.driver)

    def tearDown(self):
        """
        结束
        :return:
        """
        sleep(3)
        self.driver.quit()

    def test_case1(self):
        """
        修改签名为天天向上
        :return:
        """
        # 点击登录
        self.home_page.click_login()
        # 输入账号
        self.login_page.input_mobile('15296797153')
        # 输入密码
        self.login_page.input_password('123456')
        # 点击登录
        self.login_page.click_login()
        # 点击用户名
        sleep(2)
        self.home_page.click_username()
        # 切换frame
        sleep(2)
        self.user_page.get_frame()
        # 清空签名
        self.user_page.clear_sign()
        # 输入签名
        self.user_page.input_sign('天天向上')
        # 点击保存
        self.user_page.click_save()
        # 刷新
        self.driver.refresh()
        # 切换frame
        self.user_page.get_frame()
        # 断言
        assert self.user_page.get_sign('value') == '天天向上'