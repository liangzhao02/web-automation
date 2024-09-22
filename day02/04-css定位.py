"""打开注册A页面
点击clickforconfirm按钮
等待三秒关闭
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")

# driver.find_element_by_css_selector('[value="Click For Prompt"]').click()
driver.find_element(By.CSS_SELECTOR, '[value="Click For Prompt"]').click()

sleep(3)
driver.quit()