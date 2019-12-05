# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.CategoriesPage import CategoriesPage
from common.public import PublicMethod
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
        cls.ddbj = "18056558899"
        cls.password = "123456"
        # 声明categoriesPage类对象
        cls.categories_page = CategoriesPage(cls.driver,cls.url, u"合纵药易购结算界面")
        # 声明publicMethod类对象
        cls.public_method = PublicMethod(cls.driver, cls.url, u"合纵药易购商品分类界面")
        cls.public_method.open()
        # 关掉广告
        cls.public_method.click_ad()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test_settle_01(self):
    #     """不满200元时返回购物车"""
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告
    #     sleep(0.5)
    #     self.categories_page.click_py()  # 点击进入普药列表
    #     sleep(0.5)
    #     self.driver.back()  # 点击回到首页
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告