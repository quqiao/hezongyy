# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""积分商城个人中心界面"""

import unittest
from pages.CategoriesPage import CategoriesPage
from pages.HomePage import HomePage
from pages.JiFenShangChengPage import JiFenShangChengPage
from pages.JiFenShangCheng_lipinchePage import JiFenShangCheng_lipinchePage
from pages.JiFenShangCheng_qiandaoPage import JiFenShangCheng_qiandaoPage
from pages.JiFenShangCheng_gerenzhonginPage import JiFenShangCheng_gerenzhongxinPage
from pages.JiFenShangCheng_ddxqPage import JiFenShangCheng_ddxqPage
from selenium import webdriver
from time import sleep
from common.public import  PublicMethod, test_url, username, chromedriver

class TestJiFenShangChengGeRenZhongXin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(5)  # 隐式等待
        cls.url = test_url
        cls.username = username
        cls.password = "123456"
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明PublicMethod类对象
        cls.categories_page = CategoriesPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明categories类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购积分商城界面")
        cls.jfsc_page = JiFenShangChengPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明jifenshangchengPage类对象
        cls.jfscqd_page = JiFenShangCheng_qiandaoPage(cls.driver, cls.url,
                                                      u"合纵易购积分商城界面")  # 声明JiFenShangChennnnnnnnnnnnnnnnnnnnnnnnnnnnnnnng_qiandaoPage类对象
        cls.jfscgrzx_page = JiFenShangCheng_gerenzhongxinPage(cls.driver, cls.url,
                                                             u"合纵易购积分商城界面")  # 声明JiFenShangCheng_grzxPage类对象
        cls.jfscddxq_page = JiFenShangCheng_ddxqPage(cls.driver, cls.url,
                                                     u"合纵易购积分商城界面")  # 声明JiFenShangCheng_ddxqPage类对象
        cls.jfsclpc_page = JiFenShangCheng_lipinchePage(cls.driver, cls.url,
                                                        u"合纵易购积分商城界面")  # 声明JiFenShangCheng_lipinchePage类对象

        cls.public_page.get_url(cls.url)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jfscgrzx_01(self):
        """订单详情"""
        self.categories_page.click_jfsc()  # 进入积分商城
        sleep(1)
        self.jfsc_page.click_jfdd()  # 点击积分订单
        sleep(1)
        self.jfscgrzx_page.click_ddxq()  # 点击订单详情
        sleep(1)
        self.assertEqual(self.jfscddxq_page.text_ddxq(), "订单详情", msg="进入订单详情失败")

    def test_jfscgrzx_02(self):
        """我的积分"""
        self.jfscgrzx_page.click_wdjf()  # 点击我的积分
        sleep(1)
        self.assertEqual(self.jfscddxq_page.text_ddxq(), "我的积分", msg="进入我的积分失败")

    def test_jfscgrzx_03(self):
        """去兑换礼品"""
        self.jfscgrzx_page.click_dhlp()  # 点击兑换礼品
        sleep(1)
        self.assertEqual(self.jfsc_page.text_lpc(), "礼品车", msg="回到积分商城首页失败")

    def test_jfscgrzx_04(self):
        """去赚取积分"""
        self.driver.back()
        sleep(1)
        self.jfscgrzx_page.click_zqjf()  # 加入礼品购物车
        sleep(1)
        self.assertEqual(self.home_page.text_tc(), "[退出]", msg="去赚取积分失败")

    def test_jfscgrzx_05(self):
        """我的地址"""
        self.driver.back()
        sleep(1)
        self.jfscgrzx_page.click_wddd()
        sleep(1)
        self.assertEqual(self.jfscddxq_page.text_ddxq(), "收货地址", msg="进入我的地址页面失败")

    def test_jfscgrzx_06(self):
        """礼品车"""
        self.jfsc_page.click_lpc()  # 点击礼品车
        sleep(1)
        self.assertEqual(self.jfsclpc_page.get_jsButton(), "结算", msg="进入我的礼品车")
