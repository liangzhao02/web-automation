from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class UserPage(BaseAction):

    sign_label = By.ID, 'signature'
    save_label = By.XPATH, '//input[@value="保 存"]'

    def get_frame(self):
        """
        切换frame
        :return:
        """
        self.driver.switch_to.frame('main_frame')

    def clear_sign(self):
        """
        清空签名
        :return:
        """
        self.clear(self.sign_label)

    def input_sign(self, sign):
        """
        输入签名
        :return:
        """
        self.send_keys(self.sign_label, sign)

    def click_save(self):
        """
        点击保存签名
        :return:
        """
        self.click(self.save_label)

    def get_sign(self, name):
        """
        获取签名
        :return:
        """
        return self.get_attribute(self.sign_label, name)
