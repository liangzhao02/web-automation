"""需求：
    1. 通过脚本执行输入：
       用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
    2. 间隔3秒后，修改电话号码为：18600000000
    3. 间隔3秒，点击注册用户A
    4. 间隔3秒，关闭浏览器
    5. 元素定位方法不限
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(2)

driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')
telA = driver.find_element_by_id('telA')
telA.send_keys('18611111111')
driver.find_element_by_id('emailA').send_keys('123@qq.com')

sleep(3)
telA.clear()
telA.send_keys('18600000000')

sleep(3)
driver.find_element(By.XPATH, '//button').click()

sleep(3)
driver.quit()