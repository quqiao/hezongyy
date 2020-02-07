# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""收藏界面"""

import unittest
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.CategoriesPage import CategoriesPage
from pages.SettlePage import SettlePage
from pages.PuYaoPage import PuYaoPage
from pages.GoodsDetailPage import GoodsDetailPage
from pages.CollectionPage import CollectionPage
from pages.ZhongYaoPage import ZhongYaoPage
from selenium import webdriver
from time import sleep
from common.public import PublicMethod, test_url, username, chromedriver

class TestCollection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(5)  # 隐式等待
        cls.url = test_url
        cls.username = username
        cls.password = "123456"
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵易购收藏界面")  # 声明PublicMethod类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购收藏界面")  # 声明homePage类对象
        cls.cart_page = CartPage(cls.driver, cls.url, u"合纵易购收藏界面")  # 声明cartPage类对象
        cls.categories_page = CategoriesPage(cls.driver, cls.url, u"合纵易购收藏界面")  # 声明categoriesPage类对象
        cls.puyao_page = PuYaoPage(cls.driver, cls.url, u"合纵易购收藏界面")  # 声明puyaoPage类对象
        cls.settle_page = SettlePage(cls.driver, cls.url, u"合纵易购收藏界面")  # 声明settlePage类对象
        cls.goodsdetail_page = GoodsDetailPage(cls.driver, cls.url, u"合纵易购收藏界面")  # 声明goodsDetailPage类对象
        cls.collection_page = CollectionPage(cls.driver, cls.url, u"合纵易购收藏界面")  # 声明collectionPage类对象
        cls.zhongyao_page = ZhongYaoPage(cls.driver, cls.url, u"合纵易购收藏界面")  # 声明ZhongYaoPage类对象
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_collection_01(self):
        """测试收藏时检查清除购物车商品"""
        sleep(1)
        self.categories_page.click_py()  # 点击进入普药列表
        sleep(2)
        self.home_page.click_gwc()  # 进入购物车界面
        sleep(1)
        self.cart_page.is_scsp_exist()  # 判断是否存在商品
        sleep(1)
        self.driver.back()  # 返回首页
        sleep(1)
        self.public_page.is_element_exist()  # 判断广告也是否弹出，弹出自动关闭

    def test_collection_02(self):
        """检查收藏列表中全部为空"""
        sleep(1)
        self.home_page.click_wdsc()  # 进入我的收藏
        sleep(1)
        self.collection_page.is_sc_exist()  # 判断收藏栏中是否有收藏商品
        sleep(1)
        self.assertEqual(self.collection_page.text_qqq(), "去逛逛", msg="全部没有为空")  # 判断收藏栏是否为空了

    def test_collection_03(self):
        """检查精品专区为空"""
        sleep(1)
        self.collection_page.click_jpzq()  # 进入精品专区
        sleep(1)
        self.assertEqual(self.collection_page.text_qqq(), "去逛逛", msg="精品专区没有为空")

    def test_collection_04(self):
        """检查普药为空"""
        sleep(1)
        self.collection_page.click_py()  # 进入普药列表
        sleep(1)
        self.assertEqual(self.collection_page.text_qqq(), "去逛逛", msg="普药列表为空")

    def test_collection_05(self):
        """检查中药饮片为空"""
        sleep(1)
        self.collection_page.click_zyyp()  # 进入中药列表
        sleep(1)
        self.assertEqual(self.collection_page.text_qqq(), "去逛逛")

    def test_collection_06(self):
        """普药加入收藏"""
        sleep(1)
        self.categories_page.click_py()  # 点击普药
        sleep(1)
        self.public_page.click_jrsc(0)  # 加入收藏夹
        sleep(1)
        self.puyao_page.click_cksc()  # 查看收藏夹
        sleep(1)
        self.collection_page.click_py()  # 查看普药列表
        sleep(1)
        self.assertEqual(self.collection_page.text_qxsc(), "取消收藏", msg="普药中没有收藏成功")

    def test_collection_07(self):
        """精品专区加入收藏"""
        sleep(1)
        self.categories_page.click_jpzq()  # 点击精品专区
        sleep(1)
        self.public_page.click_jrsc(0)  # 加入收藏夹
        sleep(1)
        self.puyao_page.click_cksc()  # 查看收藏夹
        sleep(1)
        self.collection_page.click_jpzq()  # 查看精品专区列表
        sleep(1)
        self.assertEqual(self.collection_page.text_qxsc(), "取消收藏", msg="精品专区中没有收藏成功")

    def test_collection_08(self):
        """中药饮片加入收藏"""
        sleep(1)
        self.categories_page.click_zyzq()  # 点击中药饮片
        sleep(1)
        self.zhongyao_page.click_ljqg(0)  # 点击立即抢购
        sleep(1)
        self.public_page.switch_secendPage()  # 切换到当前页
        sleep(1)
        self.goodsdetail_page.click_jrsc()  # 点击加入收藏
        sleep(1)
        self.public_page.click_tckLeft()  # 提示框确定删除
        sleep(1)
        self.collection_page.click_zyyp()  # 点击中药饮片列表
        sleep(1)
        self.assertEqual(self.collection_page.text_qxsc(), "取消收藏", msg="中药饮片没有收藏成功")

    def test_collection_09(self):
        """列表加入购物车"""
        sleep(1)
        self.collection_page.click_qb()  # 点击全部列表
        sleep(1)
        self.collection_page.click_jrgwc(0)  # 点击列表加入购物车
        sleep(1)

    def test_collection_10(self):
        """列表删除"""
        sleep(1)
        self.collection_page.click_qb()  # 点击全部
        sleep(1)
        self.collection_page.click_lbsc()  # 点击列表删除
        sleep(1)
        self.public_page.click_tckLeft()  # 提示框确定删除
        sleep(1)
        self.assertEqual(self.cart_page.text_sccg(), "删除成功", msg="删除失败")  # 判断删除是否成功

    def test_collection_11(self):
        """单选加入购物车"""
        sleep(1)
        self.collection_page.click_dx(0)  # 单选一个商品
        sleep(1)
        self.collection_page.click_jrgwc(2)  # 加入购物车
        # sleep(1)
        # self.cart_page.click_sctskqd()  # 提示框确定删除
        sleep(1)
        self.assertEqual(self.collection_page.text_jrcg(), "前往购物车结算", msg="加入购物车失败！")

    def test_collection_12(self):
        """单选删除"""
        sleep(6)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(1)
        self.home_page.click_wdsc()  # 进入我的购物车
        sleep(1)
        self.collection_page.click_dx(0)  # 单选一个商品
        sleep(1)
        self.collection_page.click_qxsc()  # 取消收藏
        sleep(1)
        self.public_page.click_tckLeft()  # 提示框确定删除
        sleep(1)
        self.assertEqual(self.cart_page.text_sccg(), "删除成功", msg="删除失败")  # 判断删除是否成功

    def test_collection_13(self):
        """全选加入购物车"""
        sleep(1)
        self.collection_page.click_qx()
        sleep(1)
        self.collection_page.click_jrgwc(1)
        sleep(1)
        self.assertEqual(self.collection_page.text_jrcg(), "前往购物车结算", msg="加入购物车失败！")

    def test_collection_14(self):
        """全选取消收藏"""
        sleep(5)
        self.public_page.is_element_exist()
        sleep(1)
        self.home_page.click_wdsc()  # 进入我的购物车
        sleep(1)
        self.collection_page.click_qx()  # 全选商品
        sleep(1)
        self.collection_page.click_qxsc()  # 取消收藏
        sleep(1)
        self.public_page.click_tckLeft()  # 提示框确定删除
        sleep(1)
        self.assertEqual(self.cart_page.text_sccg(), "删除成功", msg="删除失败")  # 判断删除是否成功