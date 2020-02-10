# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""积分商城签到界面"""

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

class TestJiFenShangChengQianDao(unittest.TestCase):

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

    def test_jfscqd_01(self):
        """签到成功"""
        self.categories_page.click_jfsc()  # 进入积分商城
        sleep(1)
        self.jfsc_page.click_qd()  # 点击签到
        sleep(1)
        self.jfscqd_page.click_qdButton()  # 点击签到按钮
        sleep(1)
        self.assertEqual(self.jfscqd_page.text_qdcgts(), "签到成功,，获得积分+50", msg="签到成功")


    def test_jfscqd_02(self):
        """已签到"""
        sleep(1)
        self.public_page.click_tckLeft()  # 签到成功确认提示
        sleep(1)
        self.jfscqd_page.click_qdButton()  # 点击签到按钮
        sleep(1)
        self.assertEqual(self.jfscqd_page.text_qdcgts(), "您今天已经签到过了", msg="已签到")