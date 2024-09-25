from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# driver.get('http://info.itfeat.com/')
driver.get('http://192.168.1.21:9999')
driver.maximize_window()
driver.implicitly_wait(20)


driver.find_element_by_link_text('登录').click()

driver.find_element_by_id('mobile').send_keys('15296797153')
# 登录成功
driver.find_element_by_id('password').send_keys('123456')

driver.find_element_by_xpath('//input[@value="登 录"]').click()

assert driver.find_element_by_id("nick_name").text == '天天向上'

sleep(3)
driver.quit()