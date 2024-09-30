from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    mobile_label = By.ID, 'mobile'
    password_label = By.ID, 'password'
    login_label = By.XPATH, '//input[@value="登 录"]'

    def input_mobile(self, mobile):
        """
        输入账号
        :return:
        """
        self.send_keys(self.mobile_label, mobile)


    def input_password(self, password):
        """
        输入密码
        :return:
        """
        self.send_keys(self.password_label, password)

    def click_login(self):
        """
        点击登录
        :return:
        """
        self.click(self.login_label)