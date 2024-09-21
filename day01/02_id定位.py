# 导包
from time import sleep

from selenium import webdriver

# 连接驱动 类中 类名浏览器名称 实例化
driver = webdriver.Chrome()

# 进入百度页面 get('url')
driver.get('D:\软件测试学习资料\讲义\web自动化\素材\注册A.html')

# 使用id定位到账号框
userA = driver.find_element_by_id('userA')

# 输入账号admin send.keys("xxxx")
userA.send_keys('admin')

# 使用id定位到密码框
passwordA = driver.find_element_by_id('passwordA')

# 输入密码123456
passwordA.send_keys('123456')
# 等待三秒关闭
sleep(3)

# 关闭 quit()
driver.quit()
