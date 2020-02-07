# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.LoginPage import LoginPage
from pages.TeJiaPage import TeJiaPage
from pages.GoodsDetailPage import GoodsDetailPage
from pages.HomePage import HomePage
from pages.CartPage import CartPage
from pages.SettlePage import SettlePage
from selenium import webdriver
from time import sleep
from common.public import login_url, PublicMethod, tejia_url, chromedriver

class TestLogin(unittest.TestCase):

    def setUp(self):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromedriver)
        self.driver.implicitly_wait(30)
        self.url1 = login_url
        self.url2 = tejia_url
        self.username1 = "测试05"  # 非区域会员
        self.username2 = "测试06"  # 非终端会员
        self.username3 = "测试07"  # 正常会员
        self.password = "123456"  # 密码
        self.public_page = PublicMethod(self.driver, self.url, u"合纵易购特价界面")  # 声明publicMethod类对象
        self.login_page = LoginPage(self.driver, self.url, u"合纵易购特价界面")  # 声明LoginPage类对象
        self.tejia_page = TeJiaPage(self.driver, self.url, u"合纵易购特价界面")  # 声明TeJiaPage类对象
        self.goodDetail_page = GoodsDetailPage(self.driver, self.url, u"合纵易购特价界面")  # 声明GoodsDetailPage
        self.cart_page = CartPage(self.driver, self.url, u"合纵易购特价界面")  # 声明cartPage
        self.home_page = HomePage(self.driver, self.url, u"合纵易购特价界面")  # 声明homePage
        self.settle_page = SettlePage(self.driver, self.url, u"合纵易购特价界面")  # 声明settlePage


    def tearDownClass(self):
        self.driver.quit()

    def test_tejia_01(self):
        """非区域内的会员"""
        self.public_page.get_url(login_url)  # 进入首页
        sleep(1)
        self.public_page.login(self.username1, self.password)  # 登录账号
        sleep(1)
        self.public_page.get_url(tejia_url)  # 进入特价页面
        sleep(1)
        self.assertEqual(self.tejia_page.text_qyts, "该活动针对非成都地区终端客户！")

    def test_tejia_02(self):
        """非终端会员"""
        self.public_page.get_url(login_url)  # 进入首页
        sleep(1)
        self.public_page.login(self.username1, self.password)  # 登录账号
        sleep(1)
        self.public_page.get_url(tejia_url)  # 进入特价页面
        sleep(1)
        self.assertEqual(self.tejia_page.text_zdts(), "只有终端可以参与活动!")

    def test_tejia_03(self):
        """加入购物车"""
        self.public_page.get_url(login_url)  # 进入首页
        sleep(1)
        self.public_page.login(self.username1, self.password)  # 登录账号
        sleep(1)
        self.public_page.get_url(tejia_url)  # 进入特价页面
        sleep(1)
        self.tejia_page.click_jrgwc()  # 加入购物车
        sleep(1)
        self.tejia_page.click_yxgpz()  # 进入已选购页面
        sleep(1)
        self.assertEqual(self.tejia_page.text_jrgwc(), "加入购物车")

    def test_tejia_04(self):
        """搜索相应商品"""
        self.public_page.get_url(login_url)  # 进入首页
        sleep(1)
        self.public_page.login(self.username1, self.password)  # 登录账号
        sleep(1)
        self.public_page.get_url(tejia_url)  # 进入特价页面
        sleep(1)
        self.tejia_page.input_ssk("川贝")
        sleep(1)
        self.tejia_page.click_ssButton()
        sleep(1)
        self.assertEqual(self.tejia_page.text_spTitle(), "川贝粉")

    def test_tejia_05(self):
        """商品详情中价格检查"""
        self.public_page.get_url(login_url)  # 进入首页
        sleep(1)
        self.public_page.login(self.username1, self.password)  # 登录账号
        sleep(1)
        self.public_page.get_url(tejia_url)  # 进入特价页面
        sleep(1)
        a = self.tejia_page.text_tj()  # 获取特价价格
        sleep(1)
        self.tejia_page.click_spdt()  # 点击商品大图
        sleep(1)
        b = self.goodDetail_page.text_tj()  # 获取特价价格
        sleep(1)
        self.assertEqual(a, b)  # 判断特价列表和商品详情的价格是否一致

    def test_tejia_06(self):
        """购物车中的价格检查"""
        self.public_page.get_url(login_url)  # 进入首页
        sleep(1)
        self.public_page.login(self.username1, self.password)  # 登录账号
        sleep(1)
        self.public_page.get_url(tejia_url)  # 进入特价页面
        sleep(1)
        a = self.tejia_page.text_tj()  # 获取特价价格
        sleep(1)
        self.tejia_page.click_spdt()  # 点击商品大图
        sleep(1)
        self.goodDetail_page.click_jrgwc()  # 点击加入购物车
        sleep(1)
        self.home_page.click_gwc()  # 点击购物车
        sleep(1)
        b = self.cart_page.text_dj()  # 获取单价
        sleep(1)
        self.assertEqual(a, b)

    def test_tejia07(self):
        """结算中的价格检查"""
        self.public_page.get_url(login_url)  # 进入首页
        sleep(1)
        self.public_page.login(self.username1, self.password)  # 登录账号
        sleep(1)
        self.public_page.get_url(tejia_url)  # 进入特价页面
        sleep(1)
        a = self.tejia_page.text_tj()  # 获取特价价格
        sleep(1)
        self.tejia_page.click_spdt()  # 点击商品大图
        sleep(1)
        self.goodDetail_page.click_jrgwc()  # 点击加入购物车
        sleep(1)
        self.home_page.click_gwc()  # 点击购物车
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算
        sleep(1)
        b = self.settle_page.text_dj()  # 获取单价
        sleep(1)
        self.assertAlmostEqual(a, b)













