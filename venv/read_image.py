# coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4", "141834", "463bb49611294593a456ed5f2d2d368f")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"/Users/daona/PycharmProjects/webauto/test02.png")
res = r.post()
print(res.text)

# import pytesseract
# from PIL import Image
# #导入ShowapiRequest包：
# from ShowapiRequest import ShowapiRequest
# #生成图片的对象：
# # image = Image.open("C:/我的代码/selenium自动化测试/Selenium3 与 Python3 实战 Web自动化测试框架/imooc2.png")
# #使用图片转换成文字：
# # text = pytesseract.image_to_string(image)
# # print(text)
# # r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5")
# r = ShowapiRequest("http://route.showapi.com/184-5","85060","624075410c1f4901b124f1110b93b90e")
# r.addBodyPara("typeId","35")
# r.addBodyPara("convert_to_jpg","0")
# # 定义文件上传设置：
# r.addFilePara("image",r"/Users/daona/PycharmProjects/webauto/imooc1.png")
# res = r.post()
# # text = res.json()['showapi_res_body']['Result']
# print(res.text) #返回信息
# #
# # # 百度ocr提供了模板，我们直接复制就ok
# # # 下载通用文字识别的python sdk,一定要放在你写的代码的文件夹下面
# # # from aip import AipOcr
# # # from os import path
# # #
# # #
# # # def baiduOCR(picfile, outfile):  # picfile:图片文件名 outfile:输出文件
# # #     filename = path.basename(picfile)  # 图片名称
# # #     # 百度提供
# # #     """ 你的 APPID AK SK """
# # #     APP_ID = ''  # 这是你产品服务的appid
# # #     API_KEY = ''  # 这是你产品服务的appkey
# # #     SECRET_KEY = ''  # 这是你产品服务的secretkey
# # #     client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# # #     i = open(picfile, 'rb')
# # #     img = i.read()
# # #
# # #     print("正在识别图片：\t" + filename)
# # #     """ 调用通用文字识别（高精度版） """
# # #     message = client.basicAccurate(img)
# # #     print("识别成功！")
# # #     i.close()
# # #     with open(outfile, 'a+') as fo:  # 这边是写进.txt文件
# # #         fo.writelines("*" * 60 + '\n')  # 搞点花里胡哨的做区分
# # #         fo.writelines("识别图片：\t" + filename + "\n" * 2)
# # #         fo.writelines("文本内容：\n")
# # #         # 输出文本内容
# # #         for text in message.get('words_result'):  # 识别的内容
# # #             fo.writelines(text.get('words') + '\n')
# # #         fo.writelines('\n' * 2)
# # #     print("文本导出成功！")
# # #     print()
# # #
# # #
# # # if __name__ == '__main__':
# # #     outfile = '/Users/daona/PycharmProjects/webauto/export1.txt'  # 保存的文件
# # #     baiduOCR('/Users/daona/PycharmProjects/webauto/imooc1.png', outfile)
# # #     print('图片文本提取结束！文本输出结果位于 %s 文件中。' % outfile)
# # #
# # # from PIL import Image
# # # import pytesseract
# # #
# # # imageObject = Image.open('/Users/daona/PycharmProjects/webauto/imooc1.png')
# # # print(imageObject)
# # # print(pytesseract.image_to_string(imageObject))
# #
# #
# #
#
# #可用
# from PIL import Image
# import pytesseract
#
# imageObject = Image.open(r'/Users/daona/PycharmProjects/webauto/test02.png')
# print(imageObject)
# print(pytesseract.image_to_string(imageObject))
##可用end

# 可用
# import os
# import pytesseract
# from PIL import Image
# from collections import defaultdict
#
# # tesseract.exe所在的文件路径
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
#
#
# # 获取图片中像素点数量最多的像素
# def get_threshold(image):
#     pixel_dict = defaultdict(int)
#
#     # 像素及该像素出现次数的字典
#     rows, cols = image.size
#     for i in range(rows):
#         for j in range(cols):
#             pixel = image.getpixel((i, j))
#             pixel_dict[pixel] += 1
#
#     count_max = max(pixel_dict.values())  # 获取像素出现出多的次数
#     pixel_dict_reverse = {v: k for k, v in pixel_dict.items()}
#     threshold = pixel_dict_reverse[count_max]  # 获取出现次数最多的像素点
#
#     return threshold
#
#
# # 按照阈值进行二值化处理
# # threshold: 像素阈值
# def get_bin_table(threshold):
#     # 获取灰度转二值的映射table
#     table = []
#     for i in range(256):
#         rate = 0.1  # 在threshold的适当范围内进行处理
#         if threshold * (1 - rate) <= i <= threshold * (1 + rate):
#             table.append(1)
#         else:
#             table.append(0)
#     return table
#
#
# # 去掉二值化处理后的图片中的噪声点
# def cut_noise(image):
#     rows, cols = image.size  # 图片的宽度和高度
#     change_pos = []  # 记录噪声点位置
#
#     # 遍历图片中的每个点，除掉边缘
#     for i in range(1, rows - 1):
#         for j in range(1, cols - 1):
#             # pixel_set用来记录该店附近的黑色像素的数量
#             pixel_set = []
#             # 取该点的邻域为以该点为中心的九宫格
#             for m in range(i - 1, i + 2):
#                 for n in range(j - 1, j + 2):
#                     if image.getpixel((m, n)) != 1:  # 1为白色,0位黑色
#                         pixel_set.append(image.getpixel((m, n)))
#
#             # 如果该位置的九宫内的黑色数量小于等于4，则判断为噪声
#             if len(pixel_set) <= 4:
#                 change_pos.append((i, j))
#
#     # 对相应位置进行像素修改，将噪声处的像素置为1（白色）
#     for pos in change_pos:
#         image.putpixel(pos, 1)
#
#     return image  # 返回修改后的图片
#
#
# # 识别图片中的数字加字母
# # 传入参数为图片路径，返回结果为：识别结果
# def OCR_lmj(img_path):
#     image = Image.open(img_path)  # 打开图片文件
#     imgry = image.convert('L')  # 转化为灰度图
#
#     # 获取图片中的出现次数最多的像素，即为该图片的背景
#     max_pixel = get_threshold(imgry)
#
#     # 将图片进行二值化处理
#     table = get_bin_table(threshold=max_pixel)
#     out = imgry.point(table, '1')
#
#     # 去掉图片中的噪声（孤立点）
#     out = cut_noise(out)
#
#     # 保存图片
#     # out.save('E://figures/img_gray.jpg')
#
#     # 仅识别图片中的数字
#     # text = pytesseract.image_to_string(out, config='digits')
#     # 识别图片中的数字和字母
#     text = pytesseract.image_to_string(out)
#
#     # 去掉识别结果中的特殊字符
#     exclude_char_list = ' .:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥'
#     text = ''.join([x for x in text if x not in exclude_char_list])
#     # print(text)
#
#     return text
#
#
# def main():
#     # 识别指定文件目录下的图片
#     # 图片存放目录figures
#     dir = '/Users/daona/PycharmProjects/webauto/'
#
#     correct_count = 0  # 图片总数
#     total_count = 0  # 识别正确的图片数量
#
#     # 遍历figures下的png,jpg文件
#     for file in os.listdir(dir):
#         if file.endswith('.png') or file.endswith('.jpg'):
#             # print(file)
#             image_path = '%s/%s' % (dir, file)  # 图片路径
#
#             answer = file.split('.')[0]  # 图片名称，即图片中的正确文字
#             recognizition = OCR_lmj(image_path)  # 图片识别的文字结果
#
#             print((answer, recognizition))
#             if recognizition == answer:  # 如果识别结果正确，则total_count加1
#                 correct_count += 1
#
#             total_count += 1
#
#     print('Total count: %d, correct: %d.' % (total_count, correct_count))
#     '''
#     # 单张图片识别
#     image_path = 'E://figures/code (1).jpg'
#     OCR_lmj(image_path)
#     '''
#
#
# main()
# #可用end

#
# #!usr/bin/env python
# # coding:utf-8
#
# import tesserocr
# from PIL import Image
#
# image = Image.open(r'/Users/daona/PycharmProjects/webauto/imooc1.png')
# image = image.convert('L')  #转化为灰度图
# threshold = 127             #设定的二值化阈值
# table = []                  #table是设定的一个表，下面的for循环可以理解为一个规则，小于阈值的，就设定为0，大于阈值的，就设定为1
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# image = image.point(table,'1')  #对灰度图进行二值化处理，按照table的规则（也就是上面的for循环）
# result = tesserocr.image_to_text(image) #对去噪后的图片进行识别
# print(result)


# #
# #
# #
# #
# #
# #
# #
# #
# # import re  # 用于正则
# # from PIL import Image  # 用于打开图片和对图片处理
# # import pytesseract  # 用于图片转文字
# # from selenium import webdriver  # 用于打开网站
# # import time  # 代码运行停顿
# #
# #
# # class VerificationCode:
# #     def __init__(self):
# #         self.driver = webdriver.Firefox()
# #         self.find_element = self.driver.find_element_by_css_selector
# #
# #     def get_pictures(self):
# #         self.driver.get('http://www.5itest.cn/register')  # 打开登陆页面
# #         self.driver.save_screenshot('pictures.png')  # 全屏截图
# #         page_snap_obj = Image.open('pictures.png')
# #         img = self.find_element('#pic')  # 验证码元素位置
# #         time.sleep(1)
# #         location = img.location
# #         size = img.size  # 获取验证码的大小参数
# #         left = location['x']
# #         top = location['y']
# #         right = left + size['width']
# #         bottom = top + size['height']
# #         image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
# #         image_obj.show()  # 打开切割后的完整验证码
# #         self.driver.close()  # 处理完验证码后关闭浏览器
# #         return image_obj
# #
# #     def processing_image(self):
# #         image_obj = self.get_pictures()  # 获取验证码
# #         img = image_obj.convert("L")  # 转灰度
# #         pixdata = img.load()
# #         w, h = img.size
# #         threshold = 160
# #         # 遍历所有像素，大于阈值的为黑色
# #         for y in range(h):
# #             for x in range(w):
# #                 if pixdata[x, y] < threshold:
# #                     pixdata[x, y] = 0
# #                 else:
# #                     pixdata[x, y] = 255
# #         return img
# #
# #     def delete_spot(self):
# #         images = self.processing_image()
# #         data = images.getdata()
# #         w, h = images.size
# #         black_point = 0
# #         for x in range(1, w - 1):
# #             for y in range(1, h - 1):
# #                 mid_pixel = data[w * y + x]  # 中央像素点像素值
# #                 if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
# #                     top_pixel = data[w * (y - 1) + x]
# #                     left_pixel = data[w * y + (x - 1)]
# #                     down_pixel = data[w * (y + 1) + x]
# #                     right_pixel = data[w * y + (x + 1)]
# #                     # 判断上下左右的黑色像素点总个数
# #                     if top_pixel < 10:
# #                         black_point += 1
# #                     if left_pixel < 10:
# #                         black_point += 1
# #                     if down_pixel < 10:
# #                         black_point += 1
# #                     if right_pixel < 10:
# #                         black_point += 1
# #                     if black_point < 1:
# #                         images.putpixel((x, y), 255)
# #                     black_point = 0
# #         # images.show()
# #         return images
# #
# #     def image_str(self):
# #         image = self.delete_spot()
# #         pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"  # 设置pyteseract路径
# #         result = pytesseract.image_to_string(image)  # 图片转文字
# #         resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
# #         result_four = resultj[0:4]  # 只获取前4个字符
# #         # print(resultj)  # 打印识别的验证码
# #         return result_four
# #
# #
# # if __name__ == '__main__':
# #     a = VerificationCode()
# #     a.image_str()
#
# #!usr/bin/env python
# # coding:utf-8
# #
# # from PIL import Image
# # '''
# # 获取图片
# # '''
# # def getImage():
# #     fileName = '1.png'
# #     img = Image.open()
# #     # 打印当前图片的模式以及格式
# #     print('未转化前的: ', img.mode, img.format)
# #     # 使用系统默认工具打开图片
# #     # img.show()
# #     return img
# #
# # '''
# # 1) 将图片进行降噪处理, 通过二值化去掉后面的背景色并加深文字对比度
# # '''
# # def convert_Image(img, standard=127.5):
# #     '''
# #     【灰度转换】
# #     '''
# #     image = img.convert('L')
# #
# #     '''
# #     【二值化】
# #     根据阈值 standard , 将所有像素都置为 0(黑色) 或 255(白色), 便于接下来的分割
# #     '''
# #     pixels = image.load()
# #     for x in range(image.width):
# #         for y in range(image.height):
# #             if pixels[x, y] > standard:
# #                 pixels[x, y] = 255
# #             else:
# #                 pixels[x, y] = 0
# #     return image
# #
# # import pytesseract
# # '''
# # 使用 pytesseract 库来识别图片中的字符
# # '''
# # def change_Image_to_text(img):
# #     '''
# #     如果出现找不到训练库的位置, 需要我们手动自动
# #     语法: tessdata_dir_config = '--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
# #     '''
# #     testdata_dir_config = '--tessdata-dir "/usr/local/bin/Tesseract"'
# #     textCode = pytesseract.image_to_string(img, lang='eng', config=testdata_dir_config)
# #     # 去掉非法字符，只保留字母数字
# #     textCode = re.sub("\W", "", textCode)
# #     return textCode
# #
# # def main():
# #     img = convert_Image(getImage(fileName))
# #     print('识别的结果：', change_Image_to_text(img))
# #
# # if __name__ == '__main__':
# #     main()
#
#
# from PIL import Image
# img = Image.open(r'/Users/daona/PycharmProjects/webauto/imooc1.png') # Your image here!
# img = img.convert("RGBA")
# pixdata = img.load()
# width,height = img.size
# print('imgsize: %dx %d' % (width, height))
# print('pixel[2,4]:', pixdata[2, 4])#eg,(0xD3,0xD3,0xD3,0xFF))

# #coding=utf-8
# import requests
# from ShowapiRequest import ShowapiRequest
#
#
#
# r = ShowapiRequest("http://route.showapi.com/184-5","85060","624075410c1f4901b124f1110b93b90e" )
# r.addBodyPara("img_base64", "")
# r.addBodyPara("typeId", "35")
# r.addBodyPara("convert_to_jpg", "0")
# r.addBodyPara("needMorePrecise", "0")
# r.addFilePara("imge", r"/Users/daona/PycharmProjects/webauto/imooc1.png") #文件上传时设置
# res = r.post()
# print(res.text) # 返回信息
