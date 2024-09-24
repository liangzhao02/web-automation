"""打开注册A页面
填写账号admin
进行刷新
点击打开B页面
进行后退、前进
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(2)

driver.find_element_by_id('userA').send_keys('admin')

sleep(2)
driver.refresh()

sleep(2)
driver.find_element_by_link_text('打开B页面').click()

sleep(2)
driver.back()

sleep(2)
driver.forward()

sleep(2)
driver.quit()