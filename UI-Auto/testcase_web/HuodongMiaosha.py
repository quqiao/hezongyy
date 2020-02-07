# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.HomePage import HomePage
from pages.GoodsDetailPage import GoodsDetailPage
from selenium import webdriver
from time import sleep
from common.public import home_url, PublicMethod, chromedriver

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(30)
        cls.url = home_url
        cls.username = "测试05"
        cls.password = "123456"
        cls.ssnr = "感冒灵"
        cls.xiangsu1 = "window.scrollBy(0, 800)"
        cls.xiangsu2 = "window.scrollBy(0, 200)"
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵易购首页界面")  # 声明publicMethod类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购首页界面")  # 声明LoginPage类对象
        cls.goodsDetail_page = GoodsDetailPage(cls.driver, cls.url, "合纵易购首页界面")  # 声明GoodsDetailPage类对象
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        # cls.public_page.click_ad()  # 关闭广告

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_MiaoSha_01(self):
        """非区域内秒杀"""


    def test_MiaoSha_02(self):
        """非终端进行秒杀"""

    def test_MiaoSha_03(self):
        """极限秒杀"""

    def test_Miaosha_04(self):
        """一般秒杀抢购"""

    def test_Miaosha_05(self):
        """已抢购商品"""

    def test_Miaosha_06(self):
        """已抢完商品"""

    def test_Miaosha_07(self):
        """已售罄商品"""

