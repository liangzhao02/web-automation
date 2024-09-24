"""
打开注册A页面
填写账号admin
进行刷新
点击打开B页面
进行后退、前进
"""
from select import select

# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# driver.find_element_by_id('userA').send_keys('admin')
# sleep(2)
# driver.refresh()
# sleep(2)
#
# driver.find_element_by_link_text('打开B页面').click()
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.quit()
"""获取标题和地址"""
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# print(driver.title)
# print(driver.current_url)
#
# driver.quit()
"""
打开注册A页面
点击账号框
输入账号框admin
双击账号框
右击账号框
"""
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# action = ActionChains(driver)
# userA = driver.find_element_by_id('userA')
# action.click(userA).perform()
# userA.send_keys('admin')
# sleep(2)
#
# action.double_click(userA).perform()
# sleep(2)
#
# action.context_click(userA).perform()
# sleep(2)
#
# driver.quit()
"""
打开drag.html页面
将红色正方形拖动到蓝色正方形上面
"""
# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/drag.html")
# sleep(2)
# driver.maximize_window()
#
# actions = ActionChains(driver)
#
# div1 = driver.find_element_by_id("div1")
# div2 = driver.find_element_by_id("div2")
# actions.drag_and_drop(div1,div2).perform()
# sleep(2)
#
# driver.quit()
"""
打开百度页面
将鼠标悬停在设置上
点击高级搜索
"""
# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# driver.maximize_window()
# sleep(3)
#
# action = ActionChains(driver)
#
# setting = driver.find_element_by_id('s-usersetting-top')
#
# action.move_to_element(setting).perform()
# sleep(3)
# advanced_search = driver.find_element_by_xpath('//a[@href="//www.baidu.com/gaoji/advanced.html"]/span')
#
# action.click(advanced_search).perform()
# sleep(3)
#
# driver.quit()
"""
需求：
    1). 输入用户名：admin1     暂停2秒，删除1
    2). 全选用户名：admin      暂停2秒
    3). 复制用户名：admin      暂停2秒
    4). 粘贴到密码框           暂停2秒
    5). 关闭浏览器
"""
# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# userA = driver.find_element_by_id('userA')
# userA.send_keys('admin1')
# sleep(2)
# userA.send_keys(Keys.BACKSPACE)
#
# userA.send_keys(Keys.CONTROL,'a')
# sleep(2)
#
# userA.send_keys(Keys.CONTROL,'c')
# sleep(2)
#
# driver.find_element_by_id('passwordA').send_keys(Keys.CONTROL,'v')
# sleep(2)
#
# driver.quit()
"""
打开注册A
使用下标选择重庆
使用value值选择广州
使用文本选择上海
"""
# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# selectA = driver.find_element_by_id('selectA')
#
# # 创建Select类对象
# select = Select(selectA)
#
# select.select_by_index(3)
# sleep(2)
# select.select_by_value('gz')
# sleep(2)
# select.select_by_visible_text('A上海')
#
# sleep(3)
# driver.quit()
"""
打开注册A页面
截图
"""
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# driver.get_screenshot_as_file('./aa.png')
#
# driver.quit()
"""
打开注册A页面
点击alerta按钮，弹出警告框
获取文本，点击确定
"""
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# driver.find_element_by_id('alerta').click()
# alert = driver.switch_to.alert
#
# print(alert.text)
# sleep(2)
# alert.accept()
# sleep(2)
# driver.quit()
"""
打开注册A
点击click for confirm按钮，弹出警告框
点击取消
"""
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# driver.find_element_by_xpath('//input[@value="Click For Confirm"]').click()
# sleep(2)
# Confirm = driver.switch_to.alert
# Confirm.dismiss()
# sleep(2)
#
# driver.quit()
"""
打开注册A页面，点击prompt按钮
输入内容123456
"""
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# driver.find_element_by_xpath('//input[@value="Click For Prompt"]').click()
# sleep(2)
# prompt = driver.switch_to.alert
# prompt.send_keys('123456')
# sleep(2)
# prompt.accept()
# sleep(2)
# driver.quit()
"""
打开注册A页面
滑动屏幕
"""
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# js = "window.scrollTo(0, 2000)"
# driver.execute_script(js)
#
# sleep(2)
# driver.quit()
"""
打开注册实例页面
填写注册用户账号admin
填写注册用户A账号adminA
填写注册用户B账号adminB
"""
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
# driver.maximize_window()
# sleep(2)
#
# driver.find_element_by_id('user').send_keys('admin')
# sleep(2)
#
# driver.switch_to.frame("idframe1")
# sleep(2)
# driver.find_element_by_id('userA').send_keys('adminA')
# sleep(2)
# driver.switch_to.default_content()
# sleep(2)
# driver.switch_to.frame("myframe2")
# driver.find_element_by_id('userB').send_keys('adminB')
# sleep(2)
#
# driver.quit()

# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
# driver.maximize_window()
# sleep(2)
#
# # 获取当前窗口句柄
# # print(driver.current_window_handle)
#
# # 新窗口跳转
# # 点击打开新窗口超链接
# driver.find_element_by_link_text("打开新窗口").click()
#
# # 获取当前窗口句柄
# # print(driver.current_window_handle)
#
# # 获取所有窗口句柄 列表返回的 打开顺序
# handles = driver.window_handles
#
# # 切换窗口 窗口句柄(id)
# driver.switch_to.window(handles[-1])
#
# # 填写账号adminB
# sleep(3)
# driver.find_element_by_id("userB").send_keys("adminB")

# 原窗口跳转
# # 点击打开B页面超链接
# driver.find_element_by_link_text("打开B页面").click()
#
# # 填写账号adminB
# sleep(3)
# driver.find_element_by_id("userB").send_keys("adminB")
# sleep(3)
# # driver.quit()
# driver.close()
# sleep(2)
# driver.quit()

# 登录百度账号
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# 打开百度首页
driver.get("https://www.baidu.com/")
sleep(3)
# 浏览器最大化
driver.maximize_window()
# 暂停两秒
sleep(5)
# 自动登录 添加cookie
driver.add_cookie({"name": "BDUSS","value": "ldscnU1S2FSc2lEWTFWZHA3MnB-SzRWcXNyb2EteXFGWE1kVm0xV0NsY0ZHflZtRVFBQUFBJCQAAAAAAAAAAAEAAAC1SFdyTWFzaHUwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWOzWYFjs1mN"})

# 刷新
sleep(2)
driver.refresh()

# # 定位百度登录并且进行点击
# driver.find_element_by_id("s-top-loginbtn").click()
# # 暂停两秒
# sleep(5)
# # 勾选协议
# driver.find_element_by_id("TANGRAM__PSP_11__isAgree").click()
# # 输入账号
# driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys(username)
# # 输入密码
# driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys(password)
# # 点击登录
# driver.find_element_by_id("TANGRAM__PSP_11__submit").click()

