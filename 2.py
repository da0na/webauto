"""
@author: luyefei
@file:skip_captcha.py
@time:2019/2/20
"""
from selenium import webdriver
import time


class SkipCaptcha(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.cookie = {"domain": ".baidu.com",
                       'name': "BAIDUID",
                       'value': "777DDDB3D7FCC909D29A0D06C9F44166CA8:FG=1",
                       "expires": "2039-02-15T08:24:00.000Z",
                       'path': '/',
                       'httpOnly': False,
                       'HostOnly': False,
                       'Secure': True}

    def login(self):
        driver = self.driver
        driver.get("http://www.baidu.com/")
        time.sleep(2)
        driver.add_cookie(self.cookie)
        time.sleep(2)
        driver.get("https://i.baidu.com/")


if __name__ == '__main__':
    r = SkipCaptcha()
    r.login()