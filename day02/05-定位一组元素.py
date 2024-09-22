from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("D:\软件测试学习资料\handouts\web自动化\素材\注册A.html")
sleep(2)

inputs = driver.find_elements_by_tag_name('input')

inputs[1].send_keys('123456')

eles = driver.find_elements_by_name('checkbox')

if len(eles)==4:
    print('数量足够')
    for ele in eles:
        ele.click()
else:
    print('数量不足')

sleep(4)
driver.quit()