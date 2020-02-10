# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""积分商城个人中心界面"""

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
from common.public import  PublicMethod, test_url, username, chromedriver

class TestJiFenShangCheng(unittest.TestCase):

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

    def test_jfsc_08(self):
        """订单详情"""
        self.jfsc_page.click_ddxq()  # 点击订单详情
        sleep(1)

    def test_jfsc_09(self):
        """我的积分"""
        self.jfsc_page.click_wdjf()  # 点击我的积分
        sleep(1)
        self.public_page.switch_secendPage()  # 句柄到第二页
        sleep(1)

    def test_jfsc_10(self):
        """为你推荐---立即兑换"""
        self.public_page.scroll_down("window.scrollBy(0, 700)")  # 下滑
        sleep(1)
        self.jfsc_page.click_wntj(6)  # 点击为你推荐
        sleep(1)
        self.jfsc_page.click_dh()  # 立即兑换
        sleep(1)

    def test_jfsc_11(self):
        """为你推荐---加入礼品车"""
        self.driver.back()
        sleep(1)
        self.jfsc_page.click_jr()  # 加入礼品购物车
        sleep(1)
        self.public_page.click_tckRight()  # 去结算

    def test_jfsc_12(self):
        """返回药易购"""
        self.jfsc_page.click_fhyyg()  # 返回药易购
        sleep(1)
        self.public_page.is_element_exist()