"""打开注册A页面
将浏览器最大化
将浏览器设置为600 600的大小
将浏览器放在600 600的位置
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(2)

# 将浏览器最大化
driver.maximize_window()
# 将浏览器设置为600 600的大小
sleep(3)
driver.set_window_size(600,600)
# 将浏览器放在600 600的位置
sleep(3)
driver.set_window_position(600,600)