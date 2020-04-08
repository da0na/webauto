# coding=utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time


class GetCode:

    def __init__(self, driver):
        self.driver = driver

    # 获取图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left * 2, top * 2, right * 2, height * 2))
        img.save(file_name)
        time.sleep(2)

    # 解析图片获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "141834", "463bb49611294593a456ed5f2d2d368f")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)
        res = r.post()
        # print(res.text)
        text = res.json()['showapi_res_body']['Result']
        time.sleep(2)
        return text
