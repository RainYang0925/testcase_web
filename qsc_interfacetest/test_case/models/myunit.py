# __author__ = 'zhangzhiyuan'
#-*-coding:utf-8-*-
import unittest
import logging
import time
'''
=====================说明======================
功能:自定义unittest框架,编写公用函数setup(),tearDown()
================================================
'''
class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # unittest.TestCase.__init__(cls, '__init__')
        print u'开始接口测试........'
    @classmethod
    def tearDownClass(cls):
        print u'.......接口测试结束'

if __name__ == '__main__':
    unittest.main()