from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):


    login_label = By.LINK_TEXT, '登录'
    username_label = By.ID, 'nick_name'

    def click_login(self):
        """
        点击登录
        :return:
        """
        self.click(self.login_label)

    def click_username(self):
        """
        点击用户名
        :return:
        """
        self.click(self.username_label)