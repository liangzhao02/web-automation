"""需求：
    1. 打开注册A.html页面
    2. 使用tag_name定位用户名输入框，并输入：admin
    3. 3秒后关闭浏览器窗口
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(2)

driver.find_element_by_tag_name('input').send_keys('admin')
sleep(2)

driver.quit()