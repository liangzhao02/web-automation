from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
driver.get('https://www.baidu.com/')
# sleep(3)

# driver.find_element_by_xpath('//input[@value="Click For Confirm"]').click()
driver.find_element_by_xpath('//input[@name="wd"]').send_keys("北京天气")
sleep(2)
driver.find_element_by_xpath('//input[@value="百度一下"]').click()

sleep(3)
driver.quit()