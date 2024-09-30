from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    login_label = By.LINK_TEXT, '登录'
    username_label = By.ID, 'nick_name'

    def click_login(self):
        self.click(self.login_label)

    def get_username(self):
        return self.get_text(self.username_label)

    def get_fail_text(self):
        return self.driver.switch_to.alert.text