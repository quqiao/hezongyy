# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""积分商城礼品车界面"""

import unittest
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.CategoriesPage import CategoriesPage
from pages.SettlePage import SettlePage
from pages.PuYaoPage import PuYaoPage
from pages.GoodsDetailPage import GoodsDetailPage
from pages.JiFenShangChengPage import JiFenShangChengPage
from pages.JiFenShangCheng_qiandaoPage import JiFenShangCheng_qiandaoPage
from selenium import webdriver
from time import sleep
from common.public import PublicMethod, test_url, username, chromedriver

class TestJiFenShangChengLiPinChe(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(5)  # 隐式等待
        cls.url = test_url
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
        cls.jfscqd_page = JiFenShangCheng_qiandaoPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明JiFenShangCheng_qiandaoPage类对象
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jfsclpc_01(self):
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

    def test_jfsclpc_02(self):
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


    def test_jfsclpc_03(self):
        """商品数量加减"""
        self.jfsc_page.click_sljia(0)
        sleep(1)
        self.jfsc_page.click_sljia(1)
        sleep(1)
        self.jfsc_page.click_sljian(0)
        sleep(1)
        self.jfsc_page.click_sljian(1)

    def test_jfsclpc_04(self):
        """商品数量输入"""
        self.jfsc_page.input_number(1, 0)
        sleep(1)
        self.jfsc_page.input_number(2, 1)
        sleep(1)

    def test_jfsclpc_05(self):
        """单选一个删除"""
        self.jfsc_page.click_dx(0)  # 选择单选
        sleep(1)
        self.jfsc_page.click_sc(1)  # 点击删除
        sleep(1)
        self.public_page.click_tckLeft()  # 提示框确定删除

    def test_jfsclpc_06(self):
        """全选结算"""
        self.jfsc_page.click_qx(0)  # 全选
        sleep(1)
        self.jfsc_page.click_jiesuan()  # 结算
        sleep(1)
        self.public_page.scroll_down("window.scrollBy(0, 700)")
        sleep(1)
        self.jfsc_page.click_submit()  # 确认提交
        sleep(1)
        self.assertEqual(self.jfsc_page.text_dhcg(), "恭喜您，您的礼品已兑换成功！", msg="兑换成功")

