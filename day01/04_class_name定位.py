"""需求：
    1. 打开注册A.html页面
    2. 通过class_name定位电话号码A，并输入：18611111111
    3. 通过class_name定位电子邮箱A，并输入：123@qq.com
    4. 3秒后关闭浏览器窗口
"""
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