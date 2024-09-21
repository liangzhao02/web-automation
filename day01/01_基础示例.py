# 导包
from time import sleep

from selenium import webdriver

# 连接驱动 类中 类名浏览器名称 实例化
driver = webdriver.Chrome()

# 进入百度页面 get('url')
driver.get('https://www.baidu.com')
driver.find_element_by_id("kw").send_keys("python")

# 等待三秒关闭
sleep(3)

# 关闭 quit()
driver.quit()

#测试