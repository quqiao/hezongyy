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
        cls.url = host + "/auth/login"
        cls.username = "测试05"
        cls.password = "123456"
        cls.shuliang = 10
        # 声明LoginPage类对象
        cls.cart_page = CartPage(cls.driver, cls.url, u"合纵易购登录界面")
        cls.cart_page.open()


    def test_cart_01(self):
        """进入购物车界面"""
        # 首先登陆
        self.cart_page.clear_text(self.cart_page.usernameloc)
        self.cart_page.clear_text(self.cart_page.passwordloc)
        self.cart_page.input_username(self.username)  # 调用输入用户名
        self.cart_page.input_password(self.password)  # 调用输入密码
        self.cart_page.click_submit()  # 调用登录提交
        self.cart_page.click_puyao()  # 调用点击普药列表
        self.cart_page.input_number(self.shuliang)  # 调用输入数量

