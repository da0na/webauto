# coding=utf-8
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
sys.path.append(rootPath)
sys.path.append(PathProject)
from selenium import webdriver
import HTMLTestRunner
import unittest
import time
from log.user_log import UserLog
from business.register_business import RegisterBusiness
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# PathProject = os.path.split(rootPath)[0]
# sys.path.append(rootPath)
# sys.path.append(PathProject)


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        # cls.file_name = r"/Users/daona/PycharmProjects/webauto/image/test001.png"
        cls.file_name = r"/Users/daona/PycharmProjects/webauto/test007.png"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info("this is chrome")
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        # if sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
        # self.driver.save_screenshot()
        print("这个是case的后置条件")

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34', 'user999', '111111', self.file_name)
        self.assertFalse(email_error, "case执行了")
        # if email_error == True:
        #     print("注册成功了，此条case执行失败")
        # #通过assert判断是否为error

    def test_login_username_error(self):
        username_error = self.login.login_name_error('1024676@qq.com', 'ss', '111111', self.file_name)
        self.assertFalse(username_error, "case执行了")
        # if username_error == True:
        #     print("注册成功了，此条case执行失败")

    def test_login_code_error(self):
        code_error = self.login.login_code_error('1024676@qq.com', 'ss222', '111111', self.file_name)
        self.assertFalse(code_error, "case执行了")
        # if code_error == True:
        #     print("注册成功了，此条case执行失败")

    def test_login_password_error(self):
        password_error = self.login.login_password_error('1024676@qq.com', 'ss222', '111111', self.file_name)
        self.assertFalse(password_error, "case执行了")
        # if password_error == True:
        #     print("注册成功了，此条case执行失败")

    def test_login_success(self):
        self.login.user_base('1024676@qq.com', 'daona009', '111111', self.file_name)
        time.sleep(5)
        success = self.login.register_success()
        time.sleep(5)
        self.assertFalse(success, "case执行了")
        # if self.login.register_success() == True
        #     print("注册成功")



'''
def main():
    first = FirstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_username_error()
    first.test_login_success()
'''


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title="This is first report", description=u"这是我们第一次测试报告")
    runner.run(suite)
    time.sleep(5)
    f.close()






