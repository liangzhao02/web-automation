from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(2)

driver.find_element_by_link_text('打开新窗口').click()

sleep(3)
driver.close() #默认关闭get打开的窗口
# driver.quit()