# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""购物车界面"""

import unittest
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.CategoriesPage import CategoriesPage
from pages.SettlePage import SettlePage
from pages.PuYaoPage import PuYaoPage
from pages.GoodsDetailPage import GoodsDetailPage
from selenium import webdriver
from time import sleep
from common.public import test_url, PublicMethod,  username, chromedriver

class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(5)  # 隐式等待
        cls.url = test_url
        cls.username = username
        cls.password = "123456"
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵易购购物车界面")  # 声明PublicMethod类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购购物车界面")  # 声明homePage类对象
        cls.cart_page = CartPage(cls.driver, cls.url, u"合纵易购购物车界面")  # 声明cartPage类对象
        cls.categories_page = CategoriesPage(cls.driver, cls.url, u"合纵易购购物车界面")  # 声明categoriesPage类对象
        cls.puyao_page = PuYaoPage(cls.driver, cls.url, u"合纵易购购物车界面")  # 声明puyaoPage类对象
        cls.settle_page = SettlePage(cls.driver, cls.url, u"合纵易购购物车界面")  # 声明settlePage类对象
        cls.goodsdetail_page = GoodsDetailPage(cls.driver, cls.url, u"合纵易购购物车界面")  # 声明goodsDetailPage类对象
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def setUp(cls):
    #     cls.cart_page.open()
    #     cls.cart_page.click_ad()  # 关闭广告
    #
    # def tearDown(cls):
    #     pass

    def test_cart_01(self):
        """测试购物车时检查清除购物车商品"""
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

    def test_cart_02(self):
        """进入购物车界面"""
        sleep(2)
        self.categories_page.click_py()  # 调用点击普药列表
        sleep(2)
        for i in range(3):
            self.puyao_page.click_addcart(i)  # 商品循环加入购物车
            sleep(2)
        sleep(3)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(0.5)
        self.assertEqual(self.cart_page.text_jiesuan(), "结算", msg="没有进入结算界面")  # 通过显示的结算判断是否进入购物车界面

    def test_cart_03(self):
        """数量增加"""
        sleep(1)
        a = self.cart_page.text_jiage()  # 数量变化前单个商品的价格
        sleep(1)
        self.cart_page.click_addNumber()  # 调用增加数量
        sleep(1)
        self.cart_page.click_minNumber()  # 调用减少数量
        sleep(1)
        self.cart_page.input_number1(50, 0)
        sleep(2)
        self.cart_page.click_jiage()  # 调用点击价格， 退出输入框
        sleep(1)
        b = self.cart_page.text_jiage()  # 数量变化后单个商品的价格
        sleep(1)
        self.assertNotEqual(a, b, msg="数量调整后价格依然一样")  # 判断数量调整后的价格不一样

    def test_cart_04(self):
        """全选与全不选"""
        sleep(1)
        self.cart_page.click_qxk()  # 调用全选框,取消全选
        sleep(1)
        self.assertEqual(self.cart_page.text_yxspsl(), "0", msg="商品数量不为0")

    def test_cart_05(self):
        """删除指定商品"""
        sleep(1)
        self.cart_page.click_sc()  # 调用删除指定商品
        sleep(1)
        self.public_page.click_tckLeft()  # 调用删除提示框中的删除
        sleep(1)
        self.assertEqual(self.cart_page.text_sccg(), "删除成功！", msg="删除失败")  # 判断删除是否成功

    def test_cart_06(self):
        """将商品移到收藏"""
        sleep(0.5)
        self.cart_page.click_ydsc()  # 调用移到收藏
        sleep(0.5)
        self.public_page.click_tckLeft()  # 调用收藏提示框收藏
        sleep(1)
        self.assertEqual(self.cart_page.text_ydsccg(), "移到我的收藏成功！", msg="移到收藏失败")  # 判断移到收藏是否成功

    def test_cart_07(self):
        """删除移除商品后返回普药界面再加入商品"""
        sleep(1)
        self.driver.back()  # 返回普药界面
        sleep(1)
        for i in range(3):
            self.puyao_page.click_addcart(i)  # 商品循环加入购物车
            sleep(1)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(1)
        self.assertEqual(self.cart_page.text_jiesuan(), "结算", msg="没有进入结算界面")  # 通过显示的结算判断是否进入购物车界面

    def test_cart_08(self):
        """没有这类商品时，删除无库存和下架商品"""
        sleep(0.5)
        self.cart_page.click_scxj(1)  # 调用删除无库存和下架商品
        sleep(0.5)
        self.public_page.click_tckLeft()  # 调用删除无库存和下架提示框确定
        sleep(1)
        self.assertEqual(self.cart_page.text_xjspwk(), "没有需要删除的商品！" or "删除成功!", msg="删除无库存和下架商品错误")  # 判断删除下架商品是否错误

    def test_cart_09(self):
        """删除选中商品"""
        sleep(1)
        self.cart_page.click_scxj(0)   # 调用删除选中商品
        sleep(1)
        self.public_page.click_tckLeft()  # 调用删除提示框确定按钮
        sleep(1)
        self.assertEqual(self.cart_page.text_gwcwk(), "购物车空空的哦~，去看看心仪的商品吧~", msg="购物车未为空")  # 判断购物车是否为空

    def test_cart_10(self):
        """删除选中商品后返回普药界面再加入商品"""
        sleep(1)
        self.driver.back()  # 返回普药界面
        sleep(1)
        self.puyao_page.click_addcart(0)  # 商品1加入购物车
        sleep(5)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(1)
        self.assertEqual(self.cart_page.text_jiesuan(), "结算", msg="没有进入结算界面")  # 通过显示的结算判断是否进入购物车界面

    def test_cart_11(self):
        """进入结算界面,商品不满200元时"""
        sleep(1)
        self.cart_page.click_jiesuan()  # 调用点击结算按钮
        sleep(1)
        self.assertEqual(self.settle_page.text_wm200(), "您购买的商品总价没有达到本店的最低起购金额￥200元的要求", msg="不满200元时出现错误")  # 判断不满200结算

    def test_cart_12(self):
        """加入满200的商品进入购物车界面"""
        sleep(1)
        self.settle_page.click_fhsy()  # 返回首页
        sleep(1)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(1)
        self.categories_page.click_py()  # 进入普药
        sleep(1)
        for i in range(3):
            self.puyao_page.click_addcart(i)  # 商品1加入购物车
            sleep(1)
        self.home_page.click_gwc()  # 进入购物车按钮
        sleep(1)
        self.assertEqual(self.cart_page.text_jiesuan(), "结算", msg="没有进入结算界面")

    def test_cart_13(self):
        """进入结算界面，商品满200元时"""
        for i in range(3):
            sleep(1)
            self.cart_page.input_number1(20, i)  # 第一个商品输入数量
        sleep(1)
        self.cart_page.click_jiesuan()  # 调用点击结算
        sleep(2)
        self.assertEqual(self.settle_page.text_info(0), "商品清单", msg="没有进入提交订单界面")  # 判断是否进入提交订单界面

    def test_cart_14(self):
        """为你推荐商品检查"""
        sleep(1)
        self.driver.back()
        sleep(1)
        self.cart_page.click_wntjyh()  # 为你推荐右滑
        sleep(1)
        self.cart_page.click_wntjzh()  # 为你推荐左滑
        sleep(1)
        self.cart_page.click_wntjdt1()  # 为你推荐第一个大图
        sleep(1)
        self.public_page.switch_secendPage()  # 句柄切换到第二页
        sleep(1)
        self.assertEqual(self.goodsdetail_page.text_jrgwc(), "加入购物车", msg="没有进入商品详情页")  # 判断是否进入商品详情页

    # def test_cart_12(self):
    #     """有这类商品时，删除无库存和下架商品"""
    #     sleep(0.5)
    #     self.cart_page.click_scxj()  # 调用删除无库存和下架商品
    #     sleep(0.5)
    #     self.cart_page.click_scxjtskqd()  # 调用删除无库存和下架提示框确定





