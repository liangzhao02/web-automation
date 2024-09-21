"""需求：
    1. 打开注册A.html页面，使用name定位，自动填写(账号A：admin、密码A:123456)
    2. 3秒后关闭浏览器窗口
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('D:\软件测试学习资料\讲义\web自动化\素材\注册A.html')
sleep(2)

userA = driver.find_element_by_name('userA')
userA.send_keys('admin')

passwordA = driver.find_element_by_name('passwordA')
passwordA.send_keys('123456')

sleep(2)
driver.quit()
