"""打开注册A
点击cLickforconfirm按钮，弹出警告框
点击取消
"""
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(3)
driver.maximize_window()

driver.find_element_by_xpath('//input[@value="Click For Confirm"]').click()

confirm = driver.switch_to.alert

confirm.dismiss()
sleep(3)

driver.quit()
