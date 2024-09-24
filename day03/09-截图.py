"""
打开注册A页面
截图
"""
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(3)

driver.get_screenshot_as_file("./a.png")
driver.quit()