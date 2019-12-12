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
from common.public import login_url

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.url = login_url
        cls.public_method = PublicMethod(cls.driver, cls.url, u"合纵药易购订单界面")  # 声明publicMethod类对象
        cls.categories_page = CategoriesPage(cls.driver, cls.url, u"合纵药易购订单界面")  # 声明categoriesPage类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵药易购订单界面")  # 声明homepage类对象
        cls.puyao_page = PuYaoPage(cls.driver, cls.url, u"合纵药易购订单界面")  # 声明puyaopage类对象
        cls.jpzq_page = JingPinZhuanQuPage(cls.driver, cls.url, u"合纵药易购订单界面")  # 声明jingpinzhuanqu类对象
        cls.settle_page = SettlePage(cls.driver, cls.url, u"合纵药易购订单界面")  # 声明settlepage类对象
        cls.cart_page = CartPage(cls.driver, cls.url, u"合纵药易购订单界面")  # 声明cartpage类对象
        cls.order_page = OrderPage(cls.driver, cls.url, u"合纵药易购订单界面")  # 声明orderpage类对象
        cls.driver.implicitly_wait(30)


    def setUp(self):
        sleep(2)
        self.username = "测试05"
        self.password = "123456"
        self.ddbz = "订单备注"
        self.shuliang = 10
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
        print("test1")
        # sleep(10)
        # self.categories_page.click_py()  # 点击普药进入普药列表
        # sleep(0.5)
        # self.puyao_page.click_addcart1()  # 点击第一个商品加入购物车
        # sleep(2)
        # self.puyao_page.click_addcart2()  # 点击第二个商品加入购物车
        # sleep(2)
        # self.puyao_page.click_addcart3()  # 点击第三个商品加入购物车
        # sleep(2)
        # self.home_page.check_script()  # 进入购物车界面
        # sleep(0.5)
        # self.cart_page.click_jiesuan()  # 点击结算按钮
        # sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_02(self):
        """在精品专区中选择商品进行下单"""
        print("test2")
        # self.categories_page.click_jpzq()  # 点击精品专区进入精品列表
        # sleep(0.5)
        # self.jpzq_page.input_number1(self.shuliang)  # 输入第一个商品加入购物车的数量
        # sleep(0.5)
        # self.jpzq_page.click_addcart1()  # 第一个商品加入购物车
        # sleep(2)
        # self.jpzq_page.input_number2(self.shuliang)  # 输入第二个商品加入购物车的数量
        # sleep(0.5)
        # self.jpzq_page.click_addcart2()  # 第二个商品加入购物车
        # sleep(2)
        # self.jpzq_page.input_number3(self.shuliang)  # 输入第三个商品加入购物车的数量
        # sleep(0.5)
        # self.jpzq_page.click_addcart3()  # 第三个商品加入购物车
        # sleep(2)
        # self.home_page.check_script()  # 进入购物车界面
        # sleep(0.5)
        # self.cart_page.click_jiesuan()  # 点击结算按钮
        # sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")





