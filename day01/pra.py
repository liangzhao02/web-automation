"""需求：
    1. 打开注册A.html页面，使用name定位，自动填写(账号A：admin、密码A:123456)
    2. 3秒后关闭浏览器窗口"""
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('D:\软件测试学习资料\讲义\web自动化\素材\注册A.html')
# sleep(2)
#
# driver.find_element_by_name("userA").send_keys("admin")
# driver.find_element_by_name("passwordA").send_keys("123456")
#
# sleep(2)
# driver.quit()
"""
需求：
    1. 打开注册A.html页面，使用id定位，自动填写(账号A：admin、密码A:123456)
    2. 3秒后关闭浏览器窗口
"""
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('D:\软件测试学习资料\讲义\web自动化\素材\注册A.html')
# sleep(2)
#
# driver.find_element_by_id("userA").send_keys('admin')
# driver.find_element_by_id("passwordA").send_keys('123456')
# sleep(2)
#
# driver.quit()
"""需求：
    1. 打开注册A.html页面
    2. 通过class_name定位电话号码A，并输入：18611111111
    3. 通过class_name定位电子邮箱A，并输入：123@qq.com
    4. 3秒后关闭浏览器窗口
"""
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('D:\软件测试学习资料\讲义\web自动化\素材\注册A.html')
# sleep(2)
#
# driver.find_element_by_class_name('telA').send_keys('18611111111')
# driver.find_element_by_class_name('emailA').send_keys('123@qq.com')
# sleep(2)
#
# driver.quit()
"""需求：
    1. 打开注册A.html页面
    2. 使用tag_name定位用户名输入框，并输入：admin
    3. 3秒后关闭浏览器窗口
"""
# from selenium import webdriver
# from time import sleep
#
# wd = webdriver.Chrome()
# wd.get('D:\软件测试学习资料\讲义\web自动化\素材\注册A.html')
# sleep(2)
#
# # wd.find_element_by_tag_name('input').send_keys('admin')
# wd.find_elements_by_tag_name("input")[3].send_keys("123456")
# wd.find
# sleep(3)
#
# wd.quit()


