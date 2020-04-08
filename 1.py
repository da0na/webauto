# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

dr = webdriver.Chrome()
dr.get("https://pan.baidu.com/")
sleep(5)
# print(EC.title_contains("登陆"))

# element = dr.find_element_by_class_name("pass-text-input")

dr.find_element_by_class_name("pass-reglink").click()
# 切换窗口
for handle in dr.window_handles:
    dr.switch_to.window(handle)
    if "注册百度账号" in dr.title:
        break

locator = (By.ID, "TANGRAM__PSP_4__userName")

# print(WebDriverWait(dr, 1).until(EC.visibility_of_element_located(locator)))

# name_element = dr.find_element_by_id("TANGRAM__PSP_4__userName")
# print(name_element.get_attribute("placeholder"))
# name_element.send_keys("我太腩了")
# print(name_element.get_attribute("value"))

for i in range(5):
    user_name = ''.join(random.sample('1234567890abcdefg', 5))+"@163.com"
    print(user_name)


# dr.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("我太腩了")
# dr.find_element_by_css_selector("[class='pass-text-input pass-text-input-phone']").send_keys("17665285522")
# dr.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__password']").send_keys("Abc123456")
# sleep(20)
# dr.quit()
# dr.close()