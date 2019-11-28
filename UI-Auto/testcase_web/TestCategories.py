# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.HomePage import HomePage
from selenium import webdriver
from time import sleep
from common.public import host

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(30)
        cls.url = host
        cls.phone = "18056558899"
        cls.password = "123456"
        # 声明LoginPage类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购反馈界面")
        cls.home_page.open()

    def test_Categories_01(self):
        """全部商品分类检查"""
        # 关掉广告
        # self.home_page.click_ad()
        # 点击呼吸系统用药列表
        self.home_page.click_list1()
        # 检查呼吸系统用药列表
        self.assertEqual(self.home_page.check_list1(), "呼吸系统用药")
        # 点击清热消炎列表
        self.home_page.click_list2()
        # 检查清热消炎列表
        self.assertEqual(self.home_page.check_list2(), "清热、消炎类")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
