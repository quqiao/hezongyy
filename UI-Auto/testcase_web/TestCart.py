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
        cls.cart_page.click_ad()  # 关闭广告

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def setUp(cls):
    #     cls.cart_page.open()
    #     cls.cart_page.click_ad()  # 关闭广告
    #
    # def tearDown(cls):
    #     pass

    def test_cart_01(self):
        """进入购物车界面"""
        self.cart_page.click_puyao()  # 调用点击普药列表
        sleep(0.5)
        self.cart_page.input_number1(self.shuliang)  # 调用输入数量
        sleep(0.5)
        self.cart_page.click_addcart()  # 调用加入购物车
        sleep(0.5)
        self.cart_page.check_script()  # 调用进入购物车界面按钮
        sleep(0.5)
        self.assertEqual(self.cart_page.text_jiesuan(), "结算")  # 通过显示的结算判断是否进入购物车界面

    # def test_cart_02(self):
    #     """数量增加"""
    #     sleep(1)
    #     self.cart_page.click_addNumber()  # 调用增加数量
    #     sleep(1)
    #     self.cart_page.click_minNumber()  # 调用减少数量
    #     sleep(1)
    #     self.cart_page.input_number2(self.shuliang)  # 调用输入数量
    #
    # def test_cart_03(self):
    #     """全选与全不选"""
    #     self.cart_page.click_qxk()  # 调用全选框
    #
    # def test_cart_04(self):
    #     """删除指定商品"""
    #     sleep(1)
    #     self.cart_page.click_sc()  # 调用删除指定商品
    #     sleep(1)
    #     self.cart_page.click_sctsksc()  # 调用删除提示框中的删除
    #     sleep(1)


    def test_cart_05(self):
        """将商品移到收藏"""
        sleep(0.5)
        self.cart_page.click_ydsc()  # 调用移到收藏
        sleep(0.5)
        self.cart_page.click_sctskqd()  # 调用收藏提示框收藏

    def test_cart_06(self):
        """删除选中商品"""
        sleep(0.5)
        self.cart_page.click_scxz()  # 调用删除选中
        sleep(0.5)
        self.cart_page.click_sctskqd()  # 调用删除提示框确定按钮

    def test_cart_07(self):
        """删除无库存和下架商品"""
        sleep(0.5)
        self.cart_page.click_scxj()  # 调用删除无库存和下架商品
        sleep(0.5)
        self.cart_page.click_scxjtskqd()  # 调用删除无库存和下架提示框确定

    def test_cart_08(self):
        """进入结算界面"""
        self.cart_page.click_jiesuan()  # 调用点击结算按钮



