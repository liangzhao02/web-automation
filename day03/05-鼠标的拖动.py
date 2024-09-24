"""打开drag.html页面
将红色正方形拖动到蓝色正方形上面
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\drag.html")
sleep(2)

action = ActionChains(driver)

div1 = driver.find_element_by_id('div1')
div2 = driver.find_element_by_id('div2')

sleep(2)
action.drag_and_drop(div1, div2).perform()

sleep(2)
driver.quit()