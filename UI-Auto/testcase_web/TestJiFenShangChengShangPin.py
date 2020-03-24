# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""积分商城商品详情界面"""

import unittest
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.CategoriesPage import CategoriesPage
from pages.SettlePage import SettlePage
from pages.PuYaoPage import PuYaoPage
from pages.GoodsDetailPage import GoodsDetailPage
from pages.JiFenShangChengPage import JiFenShangChengPage
from pages.JiFenShangCheng_qiandaoPage import JiFenShangCheng_qiandaoPage
from pages.JiFenShangCheng_spPage import JiFenShangCheng_spPage
from pages.JiFenShangCheng_jiesuanPage import JiFenShangCheng_jiesuanPage
from pages.JiFenShangCheng_gerenzhonginPage import JiFenShangCheng_gerenzhongxinPage
from selenium import webdriver
from time import sleep
from common.public import PublicMethod, test_url, username, chromedriver

class TestJiFenShangChengShangPin(unittest.TestCase):

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
        cls.jfscsp_page = JiFenShangCheng_spPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明商品页面类对象
        cls.jfscjs_page = JiFenShangCheng_jiesuanPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明结算页面类对象
        cls.jfscgrzx_page = JiFenShangCheng_gerenzhongxinPage(cls.driver, cls.url, u"合纵易购积分商城界面")  # 声明个人中心页面类对象
        cls.public_page.get_url(cls.url)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_jfscsp_01(self):
        """首页商品进入商品详情"""
        self.categories_page.click_jfsc()  # 点击进入积分商城
        sleep(1)
        self.jfsc_page.click_spdt(3)  # 点击商品大图
        sleep(1)
        self.public_page.switch_secendPage()  # 句柄切换到第二页
        sleep(1)
        self.assertEqual(self.jfscsp_page.text_lpxq(), "礼品详情", msg="没有进入礼品详情")

    def test_jfscsp_02(self):
        """增加数量"""
        for i in range(8):
            sleep(1)
            self.jfscsp_page.click_jia()
        sleep(1)

    def test_jfscsp_03(self):
        """增加减少"""
        for i in range(6):
            sleep(1)
            self.jfscsp_page.click_jian()
        sleep(1)

    def test_jfscsp_04(self):
        """正常兑换"""
        self.jfscsp_page.click_ljdh()  # 点击立即兑换
        sleep(1)
        self.public_page.scroll_bottom()  # 滚动到底部
        sleep(1)
        self.assertEqual(self.jfscjs_page.get_submit(), "确认提交", msg="没有跳转到结算页面")

    def test_jfscsp_05(self):
        """输入正常库存"""
        self.driver.back()  # 返回上一页
        sleep(1)
        self.jfscsp_page.input_srsl(5)  # 输入正常的库存
        sleep(1)
        self.assertEqual(self.jfscsp_page.getValue_srsl(), "5", msg="库存不一致")

    def test_jfscsp_06(self):
        """输入超过的库存"""
        sleep(1)
        self.jfscsp_page.input_srsl(100)  # 输入正常的库存
        sleep(1)
        self.assertEqual(self.jfscsp_page.getValue_srsl(), self.jfscsp_page.text_kc(), msg="库存不一致")

    def test_jfscsp_07(self):
        """积分不足立即兑换"""
        self.jfscsp_page.click_ljdh()  # 点击立即兑换
        sleep(1)
        self.assertEqual(self.jfscjs_page.text_fhlpc(), "返回礼品车", msg="没有进入结算页面")

    def test_jfscsp_08(self):
        """加入礼品车"""
        self.driver.back()  # 返回商品详情页
        sleep(1)
        self.jfscsp_page.click_jrlpc()  # 加入礼品车
        sleep(1)
        self.assertEqual(self.jfsc_page.text_jrlpc(), "加入礼品车成功", msg="没有加入礼品车")

    def test_jfscsp_09(self):
        """从推荐商品进入商品详情"""
        self.driver.close()  # 关闭当前页
        sleep(1)
        self.public_page.switch_home()  # 句柄切换到首页
        sleep(1)
        self.jfsc_page.click_grzx()  # 点击个人中心
        sleep(1)
        self.public_page.scroll_bottom()  # 滚动到底部
        sleep(1)
        self.jfscgrzx_page.click_wntj(7)  # 点击为你推荐商品
        sleep(1)
        self.public_page.switch_secendPage()  # 句柄切换到第二页
        sleep(1)
        self.assertEqual(self.jfscsp_page.text_lpxq(), "礼品详情", msg="没有进入商品详情")

    def test_jfscsp_10(self):
        """增加数量"""
        for i in range(8):
            sleep(1)
            self.jfscsp_page.click_jia()
        sleep(1)

    def test_jfscsp_11(self):
        """增加减少"""
        for i in range(6):
            sleep(1)
            self.jfscsp_page.click_jian()
        sleep(1)

    def test_jfscsp_12(self):
        """正常兑换"""
        self.jfscsp_page.click_ljdh()  # 点击立即兑换
        sleep(1)
        self.public_page.scroll_bottom()  # 滚动到底部
        sleep(1)
        self.assertEqual(self.jfscjs_page.get_submit(), "确认提交", msg="没有跳转到结算页面")

    def test_jfscsp_13(self):
        """输入正常库存"""
        self.driver.back()  # 返回上一页
        sleep(1)
        self.jfscsp_page.input_srsl(5)  # 输入正常的库存
        sleep(1)
        self.assertEqual(self.jfscsp_page.getValue_srsl(), "5" , msg="库存不一致")

    def test_jfscsp_14(self):
        """输入超过的库存"""
        sleep(1)
        self.jfscsp_page.input_srsl(100)  # 输入正常的库存
        sleep(1)
        self.assertEqual(self.jfscsp_page.getValue_srsl(), self.jfscsp_page.text_kc(), msg="库存不一致")

    def test_jfscsp_15(self):
        """积分不足立即兑换"""
        self.jfscsp_page.click_ljdh()  # 点击立即兑换
        sleep(1)
        self.assertEqual(self.jfscjs_page.text_fhlpc(), "返回礼品车", msg="没有进入结算页面")

    def test_jfscsp_16(self):
        """加入礼品车"""
        self.driver.back()  # 返回商品详情页
        sleep(1)
        self.jfscsp_page.click_jrlpc()  # 加入礼品车
        sleep(1)
        self.assertEqual(self.jfsc_page.text_jrlpc(), "加入礼品车成功", msg="没有加入礼品车")

