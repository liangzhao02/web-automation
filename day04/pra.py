# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com/")
# # 输入奇迹课堂
# driver.find_element_by_id("kw").send_keys("奇技课堂")
# # 点击百度一下
# driver.find_element_by_id("su").click()
# # 强制等待
# sleep(3)
# # 点击奇技课堂 - 软件测试
# driver.find_element_by_link_text("奇技课堂 - 软件测试").click()
# sleep(3)
# driver.quit()
"""
打开注册A页面
使用id定位我的id是hiddd元素
"""
# from selenium import webdriver
# from time import sleep
#
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# driver.implicitly_wait(5)
# driver.find_element_by_id('ddddd')
#
# driver.quit()

# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# WebDriverWait(driver,10, 1).until(lambda x:x.find_element_by_id('ddddd'))
#
# driver.quit()


# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('http://info.itfeat.com/')
# driver.maximize_window()
# sleep(2)
#
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_id("mobile").send_keys("15296797153")
# driver.find_element_by_id("password").send_keys("123456")
#
# sleep(2)
# driver.find_element_by_xpath('//input[@value="登 录"]').click()
# sleep(2)
# assert driver.find_element_by_id('nick_name').text == "天天向上"
#
# sleep(2)
# driver.quit()

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('http://info.itfeat.com/')
driver.maximize_window()
sleep(2)

driver.find_element_by_link_text('登录').click()
driver.find_element_by_id("mobile").send_keys("15296797153")
driver.find_element_by_id("password").send_keys("12345")

driver.find_element_by_xpath('//input[@value="登 录"]').click()
sleep(2)
alert = driver.switch_to.alert
assert alert.text == '用户名或者密码错误'

sleep(2)
driver.quit()