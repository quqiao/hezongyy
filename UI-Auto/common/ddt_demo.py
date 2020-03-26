# -*- coding: utf-8 -*-
__author__ = 'quqiao'

"""
数据驱动原理：
            1.测试数据为多个字典的list类型
            2.测试类前加修饰@ddt.ddt
            3.case前加修饰@ddt.data()
            4.运行后用例会自动加载成N个单独的用例
"""

import ddt
import unittest

# 测试数据
testdata = [{'username': 'zhangsan', 'psw': '123456'},
            {'username': 'lisi', 'psw': '345678'},
            {'username': 'wangwu', 'psw': '567890'}]

@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("start!")
    def tearDown(self):
        print("end!")
    @ddt.data(*testdata)
    def test_dd(self, data):
        print(data)

if __name__ == "__main__":
    unittest.main()