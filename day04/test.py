from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('http://info.itfeat.com/')
driver.maximize_window()
# 登录失败
driver.find_element_by_link_text('登录').click()
# 输入账号
driver.find_element_by_id('mobile').send_keys('15296797153')
# 输入密码
driver.find_element_by_id('password').send_keys('1234')
# 点击登录
driver.find_element_by_css_selector('[value="登 录"]').click()
# 切换警告框
sleep(3)
alert = driver.switch_to.alert
# 判断
assert alert.text == '用户名或者密码错误'
sleep(3)
driver.quit()