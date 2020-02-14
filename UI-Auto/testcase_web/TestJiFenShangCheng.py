# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""积分商城首页界面"""

import unittest
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.CategoriesPage import CategoriesPage
from pages.SettlePage import SettlePage
from pages.PuYaoPage import PuYaoPage
from pages.GoodsDetailPage import GoodsDetailPage
from pages.JiFenShangChengPage import JiFenShangChengPage
from pages.JiFenShangCheng_qiandaoPage import JiFenShangCheng_qiandaoPage
from pages.JiFenShangCheng_gerenzhonginPage import JiFenShangCheng_gerenzhongxinPage
from pages.JiFenShangCheng_lipinchePage import JiFenShangCheng_lipinchePage
from pages.JiFenShangCheng_ddxqPage import JiFenShangCheng_ddxqPage
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
        cls.jfscqd_page = JiFenShangCheng_qiandaoPage(cls.driver, cls.url,
                                                      u"合纵易购积分商城界面")  # 声明JiFenShangCheng_qiandaoPage类对象
        cls.jfscgrzx_page = JiFenShangCheng_gerenzhongxinPage(cls.driver, cls.url,
                                                     u"合纵易购积分商城界面")  # 声明JiFenShangCheng_grzxPage类对象
        cls.jfsclpc_page = JiFenShangCheng_lipinchePage(cls.driver, cls.url,
                                                        u"合纵易购积分商城界面")  # 声明JiFenShangCheng_lpcPage类对象
        cls.jfscddxq_page = JiFenShangCheng_ddxqPage(cls.driver, cls.url,
                                                     u"合纵易购积分商城界面")  # 声明积分商城订单界面类对象
        cls.public_page.get_url(cls.url)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jfsc_01(self):
        """进入签到界面"""
        self.categories_page.click_jfsc()  # 进入积分商城
        sleep(1)
        self.jfsc_page.click_qd()  # 点击签到
        sleep(1)
        self.assertEqual(self.jfscqd_page.getValue_qdButton(), "点击签到", msg="签到成功")

    def test_jfsc_02(self):
        """积分订单"""
        self.driver.back()  # 返回积分商城首页
        sleep(1)
        self.jfsc_page.click_jfdd()  # 点击积分订单
        sleep(1)
        self.assertEqual(self.jfscddxq_page.text_ddxq(), "积分订单", msg="积分订单界面没有进入成功")

    def test_jfsc_03(self):
        """去赚取积分"""
        self.driver.back()  # 返回积分商城首页
        sleep(1)
        self.jfsc_page.click_qzqjf()  # 点击去赚取积分
        sleep(1)
        self.assertEqual(self.home_page.text_tc(), "[退出]", msg="返回药易购失败")

    def test_jfsc_04(self):
        """礼品分类-热门兑换加入礼品车"""
        self.driver.back()  # 返回积分商城首页
        sleep(1)
        self.jfsc_page.click_rmdh()  # 点击热门兑换
        sleep(1)
        self.jfsc_page.click_spjrgwc(1)  # 第二个商品加入购物车
        sleep(1)
        self.assertEqual(self.jfsc_page.text_jrlpc(), "加入礼品车成功", msg="加入礼品车失败")

    def test_jfsc_05(self):
        """礼品分类-家用电器加入礼品车"""
        self.public_page.click_tckLeft()  # 继续兑换
        sleep(1)
        self.public_page.scroll_top()  # 滚动到顶部
        sleep(1)
        self.jfsc_page.click_jydq()  # 点击家用电器
        sleep(1)
        self.jfsc_page.click_spjrgwc(6)  # 该类第二个商品加入购物车
        sleep(1)
        self.assertEqual(self.jfsc_page.text_jrlpc(), "加入礼品车成功", msg="加入礼品车失败")

    def test_jfsc_06(self):
        """礼品分类-移动电器加入礼品车"""
        self.public_page.click_tckLeft()  # 继续兑换
        sleep(1)
        self.public_page.scroll_top()  # 滚动到顶部
        sleep(1)
        self.jfsc_page.click_jydq()  # 点击家用电器
        sleep(1)
        self.jfsc_page.click_spjrgwc(19)  # 该类第二个商品加入购物车
        sleep(1)
        self.assertEqual(self.jfsc_page.text_jrlpc(), "加入礼品车成功", msg="加入礼品车失败")

    def test_jfsc_07(self):
        """礼品分类-办公用品加入礼品车"""
        self.public_page.click_tckLeft()  # 继续兑换
        sleep(1)
        self.public_page.scroll_top()  # 滚动到顶部
        sleep(1)
        self.jfsc_page.click_jydq()  # 点击家用电器
        sleep(1)
        self.jfsc_page.click_spjrgwc(24)  # 该类第二个商品加入购物车
        sleep(1)
        self.assertEqual(self.jfsc_page.text_jrlpc(), "加入礼品车成功", msg="加入礼品车失败")

    def test_jfsc_08(self):
        """个人中心"""
        self.public_page.click_tckLeft()  # 继续兑换
        sleep(1)
        self.public_page.scroll_top()  # 滚动到顶部
        sleep(1)
        self.jfsc_page.click_grzx()  # 点击进入个人中心
        sleep(1)
        self.assertEqual(self.jfscgrzx_page.text_grzx(), "个人中心", msg="进入个人中心失败")

    def test_jfsc_09(self):
        """返回药易购"""
        self.driver.back()  # 返回积分商城
        sleep(1)
        self.jfsc_page.click_fhyyg()  # 返回药易购
        sleep(1)
        self.assertEqual(self.home_page.text_tc(), "[退出]", msg="返回药易购失败")

    def test_jfsc_10(self):
        """礼品车"""
        self.driver.back()  # 返回积分商城
        sleep(1)
        self.jfsc_page.click_lpc()  # 进入礼品车
        sleep(1)
        self.assertEqual(self.jfsclpc_page.get_jsButton(), "结算", msg="进入礼品车失败")



























