"""打开注册A页面
点击alerta按钮，弹出警告框
获取文本，点击确定
"""
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(3)
driver.maximize_window()

driver.find_element_by_id("alerta").click()
sleep(3)

alert = driver.switch_to.alert
sleep(3)

print(alert.text)

alert.accept()
sleep(3)

driver.quit()