from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class LoginPage(BaseAction):

    password_login_label = By.LINK_TEXT, '密码登录'
    input_mobile_label = By.ID, 'u'
    input_password_label = By.ID, 'p'
    login_label = By.XPATH, '//input[@value="登录"]'

    def click_password_login(self):
        """
        点击密码登录
        :return:
        """
        self.click(self.password_login_label)

    def input_mobile(self, mobile):
        """
        输入账号
        :return:
        """
        self.send_keys(self.input_mobile_label, mobile)

    def input_password(self, password):
        """
        输入密码
        :param password:
        :return:
        """
        self.send_keys(self.input_password_label, password)

    def click_login(self):
        """
        点击登录
        :return:
        """
        self.click(self.login_label)