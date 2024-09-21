from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('D:\软件测试学习资料\讲义\web自动化\素材\注册A.html')
sleep(2)

telA = driver.find_element_by_class_name("telA")
telA.send_keys("18611111111")

emailA = driver.find_element_by_class_name("emailA")
emailA.send_keys("123@qq.com")

sleep(2)
driver.quit()