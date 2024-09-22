"""打开注册A页面
获取注册A按钮的文本、大小、title属性值、位置
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(2)

button = driver.find_element(By.XPATH, '//button')
print(button.text)
print(button.size)
print(button.location)
print(button.get_attribute('title'))
sleep(2)

driver.quit()