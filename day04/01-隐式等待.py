"""打开注册A页面
使用id定位我的id是hiddd元素
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')

# 隐式等待 1.等待时间内不会报错 2.加载完毕停止等待继续执行
# 3.超过等待时间没有加载完毕会报错
driver.implicitly_wait(30)

driver.find_element_by_id('ddddd')

driver.quit()