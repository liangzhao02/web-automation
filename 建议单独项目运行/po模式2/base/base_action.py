from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, pool=0.1):
        return WebDriverWait(self.driver, timeout, pool).until(lambda x: x.find_element(*feature))

    def find_elements(self, feature, timeout=10, pool=0.1):
        return WebDriverWait(self.driver, timeout, pool).until(lambda x: x.find_elements(*feature))

    # 定位元素.click()
    def click(self, feature,  timeout=10, pool=0.1):
        self.find_element(feature, timeout, pool).click()

    def send_keys(self, feature, text, timeout=10, pool=0.1):
        self.find_element(feature, timeout, pool).send_keys(text)

    def get_text(self, feature, timeout=10, pool=0.1):
        return self.find_element(feature, timeout, pool).text

    def clear(self, feature, timeout=10, pool=0.1):
        self.find_element(feature, timeout, pool).clear()

    def get_attribute(self, feature, name, timeout=10, pool=0.1):
       return self.find_element(feature, timeout, pool).get_attribute(name)
