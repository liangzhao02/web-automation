"""打开注册A页面
使用id定位我的id是hiddd元素
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')

 # 显式等待 1.等待时间内不会报错 2.元素加载出来, 在检测时间点上停止等待继续执行3.如果没有加载出来，在报错timeout
WebDriverWait(driver, 30, 10).until(lambda x:x.find_element_by_id("ddddd"))

# driver.find_element_by_id('ddddd')
driver.quit()