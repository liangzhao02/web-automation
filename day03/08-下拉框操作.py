"""
打开注册A
使用下标选择重庆
使用vaLue值选择广州
使用文本选择上海
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(3)

# 定位下拉框元素
selectA = driver.find_element_by_id('selectA')

# 创建Select类对象
select = Select(selectA)

select.select_by_index(3)
sleep(2)
select.select_by_value('gz')
sleep(2)
select.select_by_visible_text('A上海')

sleep(3)
driver.quit()