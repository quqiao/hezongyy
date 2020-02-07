# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""结算界面"""

import unittest
from pages.CategoriesPage import CategoriesPage
from pages.HomePage import HomePage
from pages.PuYaoPage import PuYaoPage
from pages.SettlePage import SettlePage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage
from common.public import PublicMethod
from selenium import webdriver
from time import sleep
from common.public import test_url, username, chromedriver

class TestSettle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.url = test_url
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵药易购商品分类界面")  # 声明publicMethod类对象
        cls.categories_page = CategoriesPage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明categoriesPage类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明homepage类对象
        cls.puyao_page = PuYaoPage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明puyaopage类对象
        cls.settle_page = SettlePage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明settlepage类对象
        cls.cart_page = CartPage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明cartpage类对象
        cls.order_page = OrderPage(cls.driver, cls.url, u"合纵药易购结算界面")  # 声明orderpage类对象
        cls.driver.implicitly_wait(5)
        cls.username = username
        cls.password = "123456"
        cls.ddbz = "订单备注"
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        # cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.quit()

    def test_settle_01(self):
        """测试结算时检查清除购物车商品"""
        sleep(1)
        self.categories_page.click_py()  # 点击进入普药列表
        sleep(2)
        self.home_page.click_gwc()  # 进入购物车界面
        sleep(1)
        self.cart_page.is_scsp_exist()  # 判断是否存在商品


    def test_settle_02(self):
        """进入未满200元提示界面"""
        sleep(1)
        self.puyao_page.click_addcart(0)  # 第一件商品加入购物车
        sleep(2)
        self.home_page.click_gwc()  # 进入购物车界面
        sleep(0.5)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        self.assertEqual(self.settle_page.text_wm200(), "您购买的商品总价没有达到本店的最低起购金额￥200元的要求", msg="没有弹出未满200元提示")


    def test_settle_03(self):
        """不满200元时返回购物车"""
        self.settle_page.click_fhgwc()  # 返回购物车
        sleep(1)
        self.assertEqual(self.cart_page.text_jiesuan(), "结算", msg="返回购物车界面失败")  # 判断是否返回购物车界面

    def test_settle_04(self):
        """不满200元时返回首页"""
        sleep(0.5)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        self.settle_page.click_fhsy()  # 返回首页
        sleep(0.5)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(1)
        self.assertEqual(self.home_page.text_tc(), "[退出]", msg="返回首页界面失败")  # 判断是否返回首页界面

    def test_settle_05(self):
        """检查进入结算界面"""
        sleep(1)
        self.categories_page.click_py()  # 点击进入普药列表
        sleep(1)
        for i in range(3):
            self.puyao_page.click_addcart(i)  # 第一件商品加入购物车
            sleep(2)
        self.home_page.click_gwc()  # 进入购物车界面
        sleep(1)
        for i in range(3):
            sleep(1)
            self.cart_page.input_number1(20, i)  # 第一个商品输入数量
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(1)
        self.assertEqual(self.settle_page.text_info(0), "商品清单", msg="没有进入结算界面")

    def test_settle_06(self):
        """结算界面返回购物车"""
        sleep(3)
        self.settle_page.click_jsfhgwc()  # 结算界面返回购物车
        sleep(1)
        self.assertEqual(self.cart_page.text_jiesuan(), "结算", msg="返回购物车界面失败")  # 判断是否返回购物车界面

    def test_settle_07(self):
        """输入备注，提交订单"""
        sleep(0.5)
        self.cart_page.click_jiesuan()  # 进入结算界面
        sleep(0.5)
        self.settle_page.input_ddbz(self.ddbz)  # 订单备注中输入内容
        sleep(0.5)
        self.settle_page.click_tjdd()  # 提交订单
        sleep(1)
        self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！", msg="提交订单失败")  # 判断是否进入订单界面
