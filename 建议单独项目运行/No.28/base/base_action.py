from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, pool=0.1):
        return WebDriverWait(self.driver, timeout, pool).until(lambda x: x.find_element(*feature))

    def click(self, feature, timeout=10, pool=0.1):
        self.find_element(feature, timeout, pool).click()

    def send_keys(self, feature, text, timeout=10, pool=0.1):
        self.find_element(feature, timeout, pool).send_keys(text)