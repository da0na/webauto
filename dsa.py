# import sys
# import unittest
# class UserCase(unittest.TestCase):
#
#     def testAddUser(self):
#         print("add a user")
#
#     def testDelUser(self):
#         print("delete a user")
#
# if __name__ == '__main__':
#     result = unittest.TextTestResult(sys.stdout,'test result',1)
#     testcase = UserCase('testAddUser')
#     testcase.run(result)    #我们只需要传入一个result对象即可

# import unittest
#
# class TEST1(unittest.TestCase):
#
#     def setUp(self):
#         print("\n")
#         print("test_case_start")
#
#     def test_1_step(self):
#         print("test_1_step_start")
#
#     def test_2_step(self):
#         print("test_2_step_start")
#
# def test1_suit():
#     suite = unittest.TestSuite()
#     suite.addTest(TEST1("test_1_step"))
#     # suite.addTest(TEST1("test_2_step"))
#     unittest.TextTestRunner().run(suite)


# coding=utf-8

import unittest

import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        pass
    def test_login_blog(self):

        print("登录博客园")

    def test_add_essay(self):

        print("添加随笔")
    def test_release_essay(self):

        print("发布随笔")
    def test_quit_blog(self):

        print("退出博客园")

    def tearDown(self):
        pass
if __name__ == '__main__':
 # 启动单元测试
 # unittest.main()

 # 获取TestSuite的实例对象
    suite = unittest.TestSuite()

    # 将测试用例添加到测试容器中
    suite.addTest(TestLogin('test_login_blog'))
    suite.addTest(TestLogin('test_add_essay'))
    suite.addTest(TestLogin('test_release_essay'))
    suite.addTest(TestLogin('test_quit_blog'))

    # 创建TextTestRunner类的实例对象
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #unittest.TextTestRunner(verbosity=3).run(suite)
