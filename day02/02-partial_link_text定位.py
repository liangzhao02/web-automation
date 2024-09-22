"""需求：
    1. 打开注册A.html页面
    2. 使用partial_link_text定位(访问 新浪 网站)超链接，并点击
    3. 3秒后关闭浏览器窗口
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(2)

driver.find_element_by_partial_link_text('网站').click()

sleep(3)
driver.quit()