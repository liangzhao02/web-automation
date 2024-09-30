from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
driver.maximize_window()
sleep(2)

#主窗口
driver.find_element_by_id('user').send_keys('admin')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('tel').send_keys('18600000000')
driver.find_element_by_id('email').send_keys('123@qq.com')
sleep(2)

#注册A
driver.switch_to.frame('idframe1')
driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')
driver.find_element_by_id('telA').send_keys('18600000000')
driver.find_element_by_id('emailA').send_keys('123@qq.com')
sleep(2)

#切换回主界面
driver.switch_to.default_content()

#注册B
driver.switch_to.frame('myframe2')
driver.find_element_by_id('userB').send_keys('admin')
driver.find_element_by_id('passwordB').send_keys('123456')
driver.find_element_by_id('telB').send_keys('18600000000')
driver.find_element_by_id('emailB').send_keys('123@qq.com')

sleep(3)
driver.quit()