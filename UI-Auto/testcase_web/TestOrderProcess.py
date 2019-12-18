# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.CategoriesPage import CategoriesPage
from pages.HomePage import HomePage
from pages.PuYaoPage import PuYaoPage
from pages.JingPinZhuanQuPage import JingPinZhuanQuPage
from pages.SettlePage import SettlePage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage
from common.public import PublicMethod
from selenium import webdriver
from time import sleep
from common.public import home_url

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
            pass


    def setUp(self):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromedriver)
        self.url = home_url
        self.public_method = PublicMethod(self.driver, self.url, u"合纵药易购订单界面")  # 声明publicMethod类对象
        self.categories_page = CategoriesPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明categoriesPage类对象
        self.home_page = HomePage(self.driver, self.url, u"合纵药易购订单界面")  # 声明homepage类对象
        self.puyao_page = PuYaoPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明puyaopage类对象
        self.jpzq_page = JingPinZhuanQuPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明jingpinzhuanqu类对象
        self.settle_page = SettlePage(self.driver, self.url, u"合纵药易购订单界面")  # 声明settlepage类对象
        self.cart_page = CartPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明cartpage类对象
        self.order_page = OrderPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明orderpage类对象
        self.driver.implicitly_wait(30)
        sleep(2)
        self.username = "测试05"
        self.password = "123456"
        self.ddbz = "订单备注"
        self.shuliang = 20
        self.public_method.get_url(self.url)
        self.public_method.login(self.username, self.password)
        # self.public_method.click_ad()  # 关掉广告

    def tearDown(self):
        self.driver.quit()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        # cls.driver = webdriver.Chrome(executable_path=chromedriver)
        # cls.driver.quit()
        pass

    def test_OrderProcess_01(self):
        """在普药中选择商品进行下单"""
        sleep(2)
        self.categories_page.click_py()  # 点击普药进入普药列表
        sleep(0.5)
        self.puyao_page.click_addcart1()  # 点击第一个商品加入购物车
        sleep(2)
        self.puyao_page.click_addcart2()  # 点击第二个商品加入购物车
        sleep(2)
        self.puyao_page.click_addcart3()  # 点击第三个商品加入购物车
        sleep(2)
        self.home_page.script_gwc()  # 进入购物车界面
        sleep(0.5)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        self.settle_page.click_tjdd()  # 点击提交订单
        sleep(0.5)
        self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_02(self):
        """在精品专区中选择商品进行下单"""
        sleep(2)
        self.categories_page.click_jpzq()  # 点击精品专区进入精品列表
        sleep(0.5)
        self.jpzq_page.input_number1(self.shuliang)  # 输入第一个商品加入购物车的数量
        sleep(0.5)
        self.jpzq_page.click_addcart1()  # 第一个商品加入购物车
        sleep(2)
        self.jpzq_page.input_number2(self.shuliang)  # 输入第二个商品加入购物车的数量
        sleep(0.5)
        self.jpzq_page.click_addcart2()  # 第二个商品加入购物车
        sleep(2)
        self.jpzq_page.input_number3(self.shuliang)  # 输入第三个商品加入购物车的数量
        sleep(0.5)
        self.jpzq_page.click_addcart3()  # 第三个商品加入购物车
        sleep(2)
        self.home_page.script_gwc()  # 进入购物车界面
        sleep(0.5)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        self.settle_page.click_tjdd()  # 点击提交订单
        sleep(0.5)
        self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")