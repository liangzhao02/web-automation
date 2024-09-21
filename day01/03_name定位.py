from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('D:\软件测试学习资料\讲义\web自动化\素材\注册A.html')
sleep(2)

userA = driver.find_element_by_name('userA')
userA.send_keys('admin')

passwordA = driver.find_element_by_name('passwordA')
passwordA.send_keys('123456')

sleep(2)
driver.quit()
