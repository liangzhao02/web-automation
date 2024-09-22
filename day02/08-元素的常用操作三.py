"""打开注册A页面
获取取消A按钮的可用状态
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(2)
# 获取取消A的可用状态false
print(driver.find_element_by_id('cancelA').is_enabled())
# 获取账号框的可用状态true
print(driver.find_element_by_id('userA').is_enabled())
# 获取span标签的可见状态faLse
print(driver.find_element_by_xpath('//span[@style="visibility: hidden;"]').is_displayed())
# 获取账号框的可见状态true
print(driver.find_element_by_id("userA").is_displayed())

sleep(3)
driver.quit()