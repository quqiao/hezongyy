# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.HomePage import HomePage
from pages.MyPage import MyPage
from common.public import PublicMethod
from selenium import webdriver
from time import sleep
from common.public import host

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(30)
        cls.url = host
        cls.ddbj = "18056558899"
        cls.password = "123456"
        cls.xiangsu = "window.scrollBy(0, 700)"
        # 声明HomePage类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵药易购我的界面")
        # 声明MyPage类对象
        cls.my_page = MyPage(cls.driver, cls.url, u"合纵药易购我的界面")
        # 声明publicMethod类对象
        cls.public_method = PublicMethod(cls.driver, cls.url, u"合纵药易购我的界面")
        cls.public_method.open()
        # 关掉广告
        cls.public_method.click_ad()
        sleep(0.5)
        cls.home_page.click_my()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_my_01(self):
        """进入我的订单"""
        self.my_page.click_wddd()  # 点击我的订单
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_02(self):
        """进入积分订单"""
        self.my_page.click_jfdd()  # 点击积分订单
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_03(self):
        """进入余额管理"""
        self.my_page.click_yegl()  # 点击余额管理
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_04(self):
        """进入优惠券管理"""
        self.my_page.click_yhqgl()  # 点击优惠券管理
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_05(self):
        """进入积分管理"""
        self.my_page.click_jfgl()  # 点击积分管理
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_06(self):
        """进入积分金币管理"""
        self.my_page.click_jfjbgl()  # 点击积分金币管理
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_07(self):
        """进入基本信息"""
        self.my_page.click_jbxx()  # 点击基本信息
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_08(self):
        """进入银企通注册"""
        self.my_page.click_yqtzc()  # 点击银企通注册
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_09(self):
        """进入微信绑定"""
        self.my_page.click_wxbd()  # 点击微信绑定
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_10(self):
        """进入我的收藏"""
        self.my_page.click_wdsc()  # 点击我的收藏"
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_11(self):
        """进入智能采购"""
        self.my_page.click_zncg()  # 点击智能采购"
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_12(self):
        """进入多会员管理"""
        self.my_page.click_dhygl()  # 点击多会员管理"
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_13(self):
        """进入我的消息"""
        sleep(0.5)
        self.public_method.scroll_down(self.xiangsu)
        sleep(0.5)
        self.my_page.click_wdxx()  # 点击我的消息"
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_14(self):
        """进入我的求购"""
        self.my_page.click_wdqg()  # 点击我的求购"
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_15(self):
        """进入我的反馈"""
        self.my_page.click_wdfk()  # 点击我的反馈"
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_16(self):
        """进入收货地址"""
        self.my_page.click_shdz()  # 点击收货地址"
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

    def test_my_17(self):
        """进入配送物流"""
        self.my_page.click_pswl()  # 点击配送物流"
        sleep(0.5)
        self.driver.back()  # 返回我的药易购界面
        sleep(0.5)

