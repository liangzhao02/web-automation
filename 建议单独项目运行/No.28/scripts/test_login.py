import unittest
from selenium import webdriver
from time import sleep
from page.login_page import LoginPage
from page.home_page import HomePage

class TestLogin(unittest.TestCase):

    def setUp(self):
        """
        初始化
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.qq.com/')
        self.driver.maximize_window()

        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
    def tearDown(self):
        """
        结束
        :return:
        """
        sleep(3)
        self.driver.quit()
    def test_case1(self):
        """
        登录测试
        :return:
        """
        #切换frame
        sleep(3)
        self.home_page.get_frame()
        sleep(2)
        # 点击密码登录
        self.login_page.click_password_login()
        # 输入账号
        self.login_page.input_mobile('3629645927')
        # 输入密码
        self.login_page.input_password('huahai020414.')
        sleep(2)
        # 点击登录
        self.login_page.click_login()
