# coding=utf-8
import ddt
import unittest
import time
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import os
import sys
import traceback
from util.excel_util import  ExcelUtil
# 邮箱，用户名，密码，验证码， 错误信息定位元素，错误提示信息

ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        # if sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        print("这个是case的后置条件")
        self.driver.close()
        # self.driver.save_screenshot()

    # @ddt.data(['email', 'username', 'password', 'code', 'assertCode', '请输入有效的电子邮箱地址'])
    '''
    @ddt.data(
        ['12', 'Mushishi01', '111111', 'code', 'user_email_error', 'assertText'],
        ['@qq.com', 'Mushishi01', '111111', 'code', 'user_email_error', 'assertText'],
        ['12@qq.com', 'Mushishi01', '111111', 'code', 'user_email_error', 'assertText']
    )
    @ddt.unpack
    
    '''
    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.login.register_function(email, username, password, code, assertCode, assertText)
        self.assertFalse(email_error, "测试失败")


if __name__ == 'main':
    unittest.main()





