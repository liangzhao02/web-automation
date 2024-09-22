"""需求：
    1. 打开注册A.html页面
    2. 使用link_text定位(访问 新浪 网站)超链接，并点击
    3. 3秒后关闭浏览器窗口
"""
from ast import Bytes

from selenium.webdriver.common.by import By

# from time import sleep
#
# from selenium import webdriver
#
# wd = webdriver.Chrome()
# wd.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
# 全部文本
# sleep(2)
#
# wd.find_element_by_link_text('访问 新浪 网站').click()
# sleep(2)
#
# wd.quit()

"""需求：
    1. 打开注册A.html页面
    2. 使用partial_link_text定位(访问 新浪 网站)超链接，并点击 
    3. 3秒后关闭浏览器窗口
"""
# from time import sleep
#
# from selenium import webdriver
#
# wd = webdriver.Chrome()
# wd.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
# sleep(1)
#
# wd.find_element_by_partial_link_text('新浪').click()
# # 部分并且连续的文本
# sleep(1)
#
# wd.quit()
"""
打开注册A页面
使用xpath定位click for prompt按钮
等待三秒，关闭
"""
# from selenium import webdriver
# from time import sleep
#
# wd = webdriver.Chrome()
# wd.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
# sleep(1)
# wd.find_element(By.XPATH, '//input[@onclick="showConfirm()"]').click()
# sleep(2)
#
# wd.quit()
"""
打开注册A页面
点击click for confirm按钮
等待三秒关闭
# """
# from selenium import webdriver
# from time import sleep
#
# wd = webdriver.Chrome()
# wd.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
# sleep(1)
# # wd.find_element_by_css_selector('[value="Click For Confirm"]').click()
# wd.find_element(By.CSS_SELECTOR,'[value="Click For Confirm"]' ).click()
# sleep(1)
#
# wd.quit()
"""
使用tag_name定位到密码框进行输入123456
"""
# from selenium import webdriver
# from time import sleep
#
# wd = webdriver.Chrome()
# wd.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
# sleep(2)
# # inputs = wd.find_elements_by_tag_name("input")
# # inputs[1].send_keys("123456")
# wd.find_elements_by_tag_name('input')[1].send_keys('654321')
# sleep(2)
#
# wd.quit()
"""
需求：
    1. 通过脚本执行输入：
       用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
    2. 间隔3秒后，修改电话号码为：18600000000
    3. 间隔3秒，点击注册用户A
    4. 间隔3秒，关闭浏览器
    5. 元素定位方法不限
"""
# from selenium import webdriver
# from time import sleep
#
# wd = webdriver.Chrome()
# wd.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
# sleep(2)
#
# wd.find_element_by_id('userA').send_keys('admin')
# wd.find_element_by_id('passwordA').send_keys('123456')
# telA = wd.find_element_by_id('telA')
# telA.send_keys('18611111111')
# wd.find_element_by_id('emailA').send_keys('123@qq.com')
#
# sleep(3)
# telA.clear()
# telA.send_keys('18600000000')
# sleep(3)
# # wd.find_element(By.XPATH, '//button').click()
# wd.find_element(By.CSS_SELECTOR, '[value="注册A"]').click()
# sleep(3)

# wd.quit()
"""
打开注册A页面
获取注册A按钮的文本、大小、title属性值、位置
"""
# from selenium import webdriver
# from time import sleep
#
# wd = webdriver.Chrome()
# wd.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
# sleep(2)
#
# button = wd.find_element(By.CSS_SELECTOR, '[value="注册A"]')
# # button = wd.find_element(By.XPATH, '//button')
# # 文本
# print(button.text)
# # 大小
# print(button.size)
# # title属性值
# print(button.get_attribute('title'))
# # 位置
# print(button.location)
#
# sleep(2)
# wd.quit()
"""
打开注册A页面
获取取消A按钮的可用状态
"""
# from selenium import webdriver
# from time import sleep
#
# wd = webdriver.Chrome()
# wd.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
# sleep(2)
# # 获取取消A的可用状态 false
# print(wd.find_element_by_xpath('//input[@value="取消A"]').is_enabled())
# # 获取账号框的可用状态 true
# print(wd.find_element_by_id('userA').is_enabled())
# # 获取span标签的可见状态 false
# print(wd.find_element(By.XPATH, '//span[@style="visibility: hidden;"]').is_displayed())
# wd.find_element_by_xpath('//span[@style="visibility: hidden;"]').is_displayed()
# print(wd.find_element_by_xpath('//span').is_displayed())
# print(wd.find_element(By.XPATH, '//span').is_displayed())
# # 获取账号框的可见状态 true
# print(wd.find_element_by_id('userA').is_displayed())
#
# sleep(2)
# wd.quit()
"""
打开注册A页面
将浏览器最大化
将浏览器设置为600 600的大小
将浏览器放在600 600的位置
"""
from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()
wd.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(2)

wd.maximize_window()
sleep(2)
wd.set_window_size(600,600)
sleep(2)
wd.set_window_position(600,600)
sleep(2)
wd.quit()