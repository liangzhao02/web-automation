from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
sleep(3)
driver.maximize_window()
sleep(5)
driver.add_cookie({"name":"BDUSS","value":"ldscnU1S2FSc2lEWTFWZHA3MnB-SzRWcXNyb2EteXFGWE1kVm0xV0NsY0ZHflZtRVFBQUFBJCQAAAAAAAAAAAEAAAC1SFdyTWFzaHUwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWOzWYFjs1mN"})
sleep(3)
driver.refresh()
sleep(3)
driver.quit()
