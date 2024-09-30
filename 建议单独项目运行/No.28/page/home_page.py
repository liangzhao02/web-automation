from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    def get_frame(self):
        """
        切换frame
        :return:
        """
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, 'QQMailSdkTool_login_loginBox_qq_iframe'))
        self.driver.switch_to.frame('ptlogin_iframe')