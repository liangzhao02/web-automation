"""打开注册A页面
点击账号框
输入账号框admin
双击账号框
右击账号框
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(3)

# 创建鼠标类对象
action = ActionChains(driver)

# 定位账号框
userA = driver.find_element_by_id("userA")

# 点击账号框
sleep(3)
action.click(userA).perform()

# 输入账号admin
sleep(3)
userA.send_keys("admin")

# 双击账号框
sleep(3)
action.double_click(userA).perform()

# 右击账号框
sleep(3)
action.context_click(userA).perform()

sleep(3)
driver.quit()