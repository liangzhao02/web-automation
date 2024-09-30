from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()
wd.get('https://mail.qq.com/')
wd.maximize_window()
sleep(3)

wd.switch_to.frame("")