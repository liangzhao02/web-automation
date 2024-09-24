from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/handouts/web%E8%87%AA%E5%8A%A8%E5%8C%96/%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html')
sleep(3)

# 获取当前窗口句柄
# print(driver.current_window_handle)

# 新窗口跳转
# 点击打开新窗口超链接
driver.find_element_by_link_text('打开新窗口').click()
sleep(2)
# 获取当前窗口句柄
# print(driver.current_window_handle)
# 获取所有窗口句柄 列表返回的 打开顺序
handles = driver.window_handles

# 切换窗口 窗口句柄(id)
driver.switch_to.window(handles[-1])
# 填写账号adminB
sleep(3)
driver.find_element_by_id('userB').send_keys('adminB')

sleep(3)
driver.quit()