"""
1)．输入用户名：admin1暂停2秒，删除1
2）．全选用户名：admin暂停2秒
3）．复制用户名：admin暂停2秒
4）．粘贴到密码框暂停2秒
5)．关闭浏览器
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(3)

userA = driver.find_element_by_id('userA')

userA.send_keys('admin1')
sleep(2)
userA.send_keys(Keys.BACK_SPACE)
userA.send_keys(Keys.CONTROL, 'a')
userA.send_keys(Keys.CONTROL, 'c')

driver.find_element_by_id('passwordA').send_keys(Keys.CONTROL, 'v')
sleep(2)

driver.quit()

