"""打开注册A页面，点击prompt按钮
输入内容123456
"""
from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()
driver.get("file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html")
sleep(3)
driver.maximize_window()

driver.find_element_by_xpath('//input[@value="Click For Prompt"]').click()
prompt = driver.switch_to.alert

sleep(3)
prompt.send_keys('123456')

sleep(2)
prompt.accept()

sleep(3)
driver.quit()
