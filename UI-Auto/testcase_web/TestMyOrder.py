# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""我的界面"""

import unittest
from common.public import PublicMethod
from selenium import webdriver
from time import sleep
from pages.HomePage import HomePage
from common.public import test_url, username, chromedriver
from pages.MyOrderPage import MyOrderPage

class TestMyOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(5)  # 隐式等待
        cls.url = test_url
        cls.username = username
        cls.password = "123456"
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵药易购我的订单界面")  # 声明HomePage类对象
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵药易购我的订单界面")  # 声明publicMethod类对象
        cls.order_page = MyOrderPage(cls.driver, cls.url, u"合纵药易购我的订单界面")
        cls.public_page.get_url(cls.url)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_MyOrder_01(self):
        """全部订单"""
        self.home_page.click_ddcx()  # 点击订单查询
        sleep(1)
        self.order_page.click_order_nav(0)  # 点击全部订单
        sleep(1)

    def test_MyOrder_02(self):
        """待付款"""
        self.order_page.click_order_nav(1)  # 点击待付款列表

    def test_MyOrder_03(self):
        """待收货"""
        self.order_page.click_order_nav(2)  # 点击待收货列表

    def test_MyOrder_04(self):
        """查询最近三个月订单"""
        self.order_page.sj_select_by_value("1")  # 点击近三个月订单
        sleep(1)
        self.order_page.click_cx()  # 点击查询

    def test_MyOrder_05(self):
        """查询今年内"""
        self.order_page.sj_select_by_value("2")  # 点击今年内
        sleep(1)
        self.order_page.click_cx()  # 点击查询

    def test_MyOrder_06(self):
        """往年订单"""
        self.order_page.click_order_nav(0)
        sleep(1)
        self.order_page.sj_select_by_value("3")  # 点击今年内
        sleep(1)
        self.order_page.click_cx()  # 点击查询

    def test_MyOrder_07(self):
        """订单编号为已有订单"""
        a = self.order_page.get_ddh(1)
        sleep(1)
        self.order_page.input_ddInput(a)  # 输入已有订单号
        sleep(1)
        self.order_page.click_cx()  # 点击查询
        sleep(1)
        self.assertIsNotNone(self.order_page.get_ddh(1))  # 判断订单号是否存在

    def test_MyOrder_08(self):
        """订单编号为没有的订单号"""
        self.order_page.input_ddInput("111")  # 输入没有订单号
        sleep(1)
        self.order_page.click_cx()  # 点击查询
        sleep(1)
        self.assertEqual(self.order_page.text_qgg(), "去逛逛", msg="输入错误")

    def test_MyOrder_09(self):
        """订单状态，待付款"""
        self.order_page.click_order_nav(0)  # 点击全部订单
        sleep(1)
        self.order_page.click_ddzt(0)  # 点击待付款

    def test_MyOrder_10(self):
        """订单状态，待收货"""
        self.order_page.click_order_nav(0)  # 点击全部订单
        sleep(1)
        self.order_page.click_ddzt(1)  # 点击待收货

    def test_MyOrder_11(self):
        """订单状态，待发货"""
        self.order_page.click_order_nav(0)  # 点击全部订单
        sleep(1)
        self.order_page.click_ddzt(2)  # 点击待发货

    def test_MyOrder_12(self):
        """订单状态，已完成"""
        self.order_page.click_order_nav(0)  # 点击全部订单
        sleep(1)
        self.order_page.click_ddzt(3)  # 点击已完成

    def test_MyOrder_13(self):
        """订单状态，已取消"""
        self.order_page.click_order_nav(0)  # 点击全部订单
        sleep(1)
        self.order_page.click_ddzt(4)  # 点击已取消

    def test_MyOrder_14(self):
        """订单跟踪"""
        self.order_page.click_order_nav(0)  # 点击全部订单
        sleep(1)
        self.order_page.click_ddgz()  # 点击订单跟踪

    def test_MyOrder_15(self):
        """再次购买"""
        self.order_page.click_zcgm()  # 点击再次购买
        sleep(1)
        self.assertEqual(self.order_page.text_cgts(), "加入购物车成功", msg="没有再次购买")

    def test_MyOrder_16(self):
        """订单详情"""
        self.order_page.click_fhwddd()  # 点击返回我的订单
        sleep(1)
        self.order_page.click_ckxq()  # 点击查看详情
        sleep(1)
        self.assertEqual(self.order_page.text_ddxq(), "订单详情", msg="没有进入订单详情界面")

    def test_MyOrder_17(self):
        """回执"""
        self.driver.back()
        sleep(1)
        self.order_page.click_hz()  # 点击回执
        sleep(1)
        self.assertEqual(self.order_page.text_hztp(), "回执图片:", msg="没有进入回执图片")












