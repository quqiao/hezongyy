# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.CategoriesPage import CategoriesPage
from pages.SettlePage import SettlePage
from pages.PuYaoPage import PuYaoPage
from pages.GoodsDetailPage import GoodsDetailPage
from pages.JiFenShangChengPage import JiFenShangChengPage
from selenium import webdriver
from time import sleep
from common.public import xianshang_url, PublicMethod, home_url, username

class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(5)  # 隐式等待
        cls.url = xianshang_url
        cls.username = username
        cls.password = "123456"
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明PublicMethod类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明homePage类对象
        cls.cart_page = CartPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明cartPage类对象
        cls.categories_page = CategoriesPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明categoriesPage类对象
        cls.puyao_page = PuYaoPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明puyaoPage类对象
        cls.settle_page = SettlePage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明settlePage类对象
        cls.goodsdetail_page = GoodsDetailPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明goodsDetailPage类对象
        cls.jfsc_page = JiFenShangChengPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明jifenshangchengPage类对象
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jfsc_01(self):
        """签到"""
        self.categories_page.click_jfsc()  # 进入积分商城
        sleep(1)
        self.jfsc_page.click_qd()  # 点击签到
        sleep(1)
        self.jfsc_page.click_qdButton()  # 点击签到
        sleep(1)
        self.assertEqual(self.jfsc_page.text_qdcgts(), "签到成功,，获得积分", msg="签到成功")
        # self.assertEqual(self.jfsc_page.text_qdcgts(), "您今天已经签到过了", msg="已签到")

    def test_jfsc_02(self):
        """检查礼品车"""
        self.public_page.click_tckLeft()  # 提示框确定
        sleep(1)
        self.driver.back()  # 回到积分商城首页
        sleep(1)
        self.jfsc_page.click_lpc()  # 点击礼品车
        sleep(1)
        self.jfsc_page.is_element_exist()  # 判断商品是否存在
        sleep(1)
        self.assertEqual(self.jfsc_page.text_qgg(), "去逛逛", msg="礼品车中没有商品")


    def test_jfsc_03(self):
        """商品兑换"""
        sleep(1)
        self.driver.back()  # 回到积分商城首页
        sleep(1)
        self.jfsc_page.click_spjrgwc(2)  # 将兑换商品加入购物车
        sleep(1)
        self.jfsc_page.click_spjrgwc(3)  #
        sleep(1)
        self.jfsc_page.click_lpc()  # 进入礼品车
        sleep(1)
        self.jfsc_page.isElementPresent()  # 判断购物车中是否存在


    def test_jfsc_04(self):
        """商品数量加减"""
        self.jfsc_page.click_sljia(0)
        sleep(1)
        self.jfsc_page.click_sljia(1)
        sleep(1)
        self.jfsc_page.click_sljian(0)
        sleep(1)
        self.jfsc_page.click_sljian(1)

    def test_jfsc_05(self):
        """商品数量输入"""
        self.jfsc_page.input_number(30, 0)
        sleep(1)
        self.jfsc_page.input_number(40, 1)
        sleep(1)

    def test_jfsc_06(self):
        """单选一个删除"""
        self.jfsc_page.click_dx(0)
        sleep(1)
        self.jfsc_page.click_sc

    def test_jfsc_02(self):
        """积分订单"""

        self.jfsc_page.click_jfdd()  # 点击进入积分订单
        sleep(1)

