# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.CategoriesPage import CategoriesPage
from pages.HomePage import HomePage
from pages.PuYaoPage import PuYaoPage
from pages.SettlePage import SettlePage
from pages.CartPage import CartPage
from common.public import PublicMethod
from selenium import webdriver
from time import sleep
from common.public import login_url

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.url = login_url
        cls.public_method = PublicMethod(cls.driver, cls.url, u"合纵药易购商品分类界面")  # 声明publicMethod类对象
        cls.categories_page = CategoriesPage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明categoriesPage类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明homepage类对象
        cls.puyao_page = PuYaoPage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明puyaopage类对象
        cls.settle_page = SettlePage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明settlepage类对象
        cls.cart_page = CartPage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明cartpage类对象
        cls.driver.implicitly_wait(30)
        cls.username = "测试05"
        cls.password = "123456"
        cls.ddbz = "订单备注"
        cls.public_method.get_url(cls.url)
        cls.public_method.login(cls.username, cls.password)
        # 关掉广告
        # cls.public_method.click_ad()

    @classmethod
    def tearDownClass(cls):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        # cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.quit()

    def test_settle_01(self):
        """不满200元时返回购物车"""
        sleep(0.5)
        self.categories_page.click_py()  # 点击进入普药列表
        sleep(0.5)
        self.puyao_page.click_addcart1()  # 第一件商品加入购物车
        sleep(2)
        self.puyao_page.click_addcart2()  # 第二件商品加入购物车
        sleep(0.5)
        self.home_page.check_script()  # 进入购物车界面
        sleep(0.5)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        self.settle_page.click_fhgwc()  # 返回购物车

    def test_settle_02(self):
        """不满200元时返回首页"""
        sleep(0.5)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        self.settle_page.click_fhgwc()  # 返回首页
        sleep(0.5)
        self.public_method.click_ad()  # 关闭广告

    def test_settle_03(self):
        """结算界面返回购物车"""
        sleep(0.5)
        self.categories_page.click_py()  # 点击进入普药列表
        sleep(0.5)
        self.puyao_page.click_addcart1()  # 第一件商品加入购物车
        sleep(2)
        self.puyao_page.click_addcart2()  # 第二件商品加入购物车
        sleep(0.5)
        self.home_page.check_script()  # 进入购物车界面
        sleep(0.5)
        self.cart_page.click_jiesuan()  # 进入结算界面
        sleep(0.5)
        self.settle_page.click_jsfhgwc()  # 结算界面返回购物车

    def test_settle_04(self):
        """输入备注，提交订单"""
        sleep(0.5)
        self.cart_page.click_jiesuan()  # 进入结算界面
        sleep(0.5)
        self.settle_page.input_ddbz(self.ddbz)  # 订单备注中输入内容
        sleep(0.5)
        self.settle_page.click_tjdd()  # 提交订单


