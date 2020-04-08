# coding=utf-8

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://passport.baidu.com/v2/?reg&tt=1581220730185&overseas=undefined&gid=65E3D1E-2C09-4E6D-85E8-7726DD3FA49C&tpl=netdisk&u=https%3A%2F%2Fpan.baidu.com%2Fdisk%2Fhome")
element = driver.find_element_by_id('TANGRAM__PSP_4__userNameLabel')
print(element.text)
# print(element.get_attribute('value'))


sleep(5)
driver.close()
