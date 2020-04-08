# coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# driver.get("http://www.5itest.cn/register")
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
email_element = driver.find_element_by_id("register_email")
driver.save_screenshot("22.png")
code_element = driver.find_element_by_id("getcode_num")
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
print(left, top, right, height)
im = Image.open("22.png")
img = im.crop((left*2, top*2, right*2, height*2))
img.save("3.png")

