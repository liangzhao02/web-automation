"""打开百度页面
将鼠标悬停在设置上
点击高级搜索
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
sleep(2)

action = ActionChains(driver)

driver.maximize_window()
seting = driver.find_element_by_id('s-usersetting-top')
sleep(2)

action.move_to_element(seting).perform()
sleep(2)

advanced_search = driver.find_element(By.XPATH, '//a[@href="//www.baidu.com/gaoji/advanced.html"]/span')
action.click(advanced_search).perform()
sleep(2)

driver.quit()