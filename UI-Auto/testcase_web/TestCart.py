# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.CartPage import CartPage
from selenium import webdriver
from time import sleep
from common.public import host

class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(30)
        cls.url = host
        # cls.username = "测试05"
        # cls.password = "123456"
        cls.shuliang = 10
        # 声明cartPage类对象
        cls.cart_page = CartPage(cls.driver, cls.url, u"合纵易购登录界面")
        cls.cart_page.open()


    def test_cart_01(self):
        """进入购物车界面"""
        self.cart_page.click_puyao()  # 调用点击普药列表
        sleep(0.5)
        self.cart_page.input_number(self.shuliang)  # 调用输入数量
        sleep(0.5)
        self.cart_page.click_addcart()  # 调用加入购物车
        sleep(0.5)
        self.cart_page.check_script()  # 调用进入购物车界面按钮
        sleep(0.5)
        self.assertEqual(self.cart_page.text_jiesuan(), "结算")  # 通过显示的结算判断是否进入购物车界面

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
