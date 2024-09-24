"""打开注册实例页面
填写注册用户账号admin
填写注册用户A账号adminA
填写注册用户B账号adminB
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
sleep(3)
driver.maximize_window()

driver.find_element_by_id('user').send_keys('admin')
sleep(2)

driver.switch_to.frame('idframe1')
sleep(2)
driver.find_element_by_id('userA').send_keys('adminA')
sleep(2)

driver.switch_to.default_content()
sleep(2)

driver.switch_to.frame('myframe2')
driver.find_element_by_id('userB').send_keys('adminB')
sleep(2)

driver.quit()
