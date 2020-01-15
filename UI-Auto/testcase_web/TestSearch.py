# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.SearchPage import SearchPage
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.CategoriesPage import CategoriesPage
from pages.SettlePage import SettlePage
from pages.PuYaoPage import PuYaoPage
from pages.GoodsDetailPage import GoodsDetailPage
from selenium import webdriver
from time import sleep
from common.public import PublicMethod, test_url,username

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(5)  # 隐式等待
        cls.url = test_url
        cls.username = username
        cls.password = "123456"
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵易购搜索界面")  # 声明PublicMethod类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购搜索界面")  # 声明homePage类对象
        cls.cart_page = CartPage(cls.driver, cls.url, u"合纵易购搜索界面")  # 声明cartPage类对象
        cls.categories_page = CategoriesPage(cls.driver, cls.url, u"合纵易购搜索界面")  # 声明categoriesPage类对象
        cls.puyao_page = PuYaoPage(cls.driver, cls.url, u"合纵易购搜索界面")  # 声明puyaoPage类对象
        cls.settle_page = SettlePage(cls.driver, cls.url, u"合纵易购搜索界面")  # 声明settlePage类对象
        cls.goodsdetail_page = GoodsDetailPage(cls.driver, cls.url, u"合纵易购搜索界面")  # 声明goodsDetailPage类对象
        cls.search_page = SearchPage(cls.driver, cls.url, u"合纵易购搜索界面")  # 声明SearchPage类对象
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search_01(self):
        """搜索药名没有的内容查询"""
        self.categories_page.click_py()  # 点击进入普药
        sleep(1)
        self.search_page.input_ssk("@#$%^")  # 搜索框中输入内容
        sleep(0.5)
        self.search_page.click_ssButton()  # 点击搜索按钮
        sleep(1)
        self.assertEqual(self.search_page.text_sswk(), "发布求购", msg="搜索没有的内容错误")  # 判断没有的内容搜索查询时

    def test_search_02(self):
        """搜索厂家没有的内容查询"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()   # 点击进入普药
        sleep(1)
        self.search_page.click_ssxzk()  # 点击搜索选择框
        sleep(1)
        self.search_page.click_cj()  # 点击厂家
        sleep(1)
        self.search_page.input_ssk("@#$%^")  # 搜索框中输入内容
        sleep(1)
        self.search_page.click_ssButton()  # 点击搜索按钮
        sleep(1)
        self.assertEqual(self.search_page.text_sswk(), "发布求购", msg="搜索没有的内容错误")  # 判断没有的内容搜索查询时

    def test_search_03(self):
        """搜索框药名正确查询"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()   # 点击进入普药
        sleep(2)
        self.search_page.input_ssk("感冒灵")  # 搜索框中输入内容
        sleep(2)
        self.search_page.click_ssButton()  # 点击搜索按钮
        sleep(2)
        mingzi = self.search_page.text_spmz()
        sleep(1)
        self.assertTrue(u"感冒灵" in mingzi)

    def test_search_04(self):
        """搜索框厂家正确查询"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()   # 点击进入普药
        sleep(1)
        self.search_page.click_ssxzk()  # 点击搜索选择框
        sleep(1)
        self.search_page.click_cj()  # 点击厂家
        sleep(2)
        self.search_page.input_ssk("科伦")  # 搜索框中输入内容
        sleep(2)
        self.search_page.click_ssButton()  # 点击搜索按钮
        sleep(2)
        mingzi = self.search_page.text_spgs()
        sleep(1)
        self.assertTrue(u"科伦" in mingzi)

    def test_search_05(self):
        """品种名称首字母搜索"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()   # 点击进入普药
        sleep(1)
        self.search_page.input_ssk("amxl")  # 搜索框中输入内容
        sleep(1)
        self.search_page.click_ssList1(1)  # 点击模糊查找的第一个商品
        sleep(1)


    def test_search_06(self):
        """品种名称拼音"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()   # 点击进入普药
        sleep(1)
        self.search_page.input_ssk("amoxilin")  # 搜索框中输入内容
        sleep(1)
        self.search_page.click_ssList1(1)  # 点击模糊查找的第一个商品
        sleep(1)

    def test_search_07(self):
        """品种名称"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()   # 点击进入普药
        sleep(1)
        self.search_page.input_ssk("阿莫")  # 搜索框输入内容
        sleep(1)
        self.search_page.click_ssList1(1)  # 点击模糊查找的第一个商品
        sleep(1)

    def test_search_08(self):
        """厂家名称首字母"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()   # 点击进入普药
        sleep(1)
        self.search_page.click_ssxzk()  # 点击搜索选择框
        sleep(1)
        self.search_page.click_cj()  # 点击厂家
        sleep(1)
        self.search_page.input_ssk("hy")  # 搜索框输入内容
        sleep(1)
        self.search_page.click_ssList1(1)  # 点击模糊查找的第一个商品
        sleep(1)

    def test_search_09(self):
        """厂家名称拼音"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()  # 点击进入普药
        sleep(1)
        self.search_page.click_ssxzk()  # 点击搜索选择框
        sleep(1)
        self.search_page.click_cj()  # 点击厂家
        sleep(1)
        self.search_page.input_ssk("hayao")  # 搜索框输入内容
        sleep(1)
        self.search_page.click_ssList1(1)  # 点击模糊查找的第一个商品
        sleep(1)

    def test_search_10(self):
        """厂家名称"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()   # 点击进入普药
        sleep(1)
        self.search_page.click_ssxzk()  # 点击搜索选择框
        sleep(1)
        self.search_page.click_cj()  # 点击厂家
        sleep(1)
        self.search_page.input_ssk("哈药")  # 搜索框输入内容
        sleep(1)
        self.search_page.click_ssList1(1)  # 点击模糊查找的第一个商品
        sleep(1)

    def test_search_11(self):
        """药品中输入厂家名"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()  # 点击进入普药
        sleep(1)
        self.search_page.input_ssk("哈药")  # 搜索框输入内容
        sleep(1)
        self.search_page.click_ssList1(1)  # 点击模糊查找的第一个商品
        sleep(1)

    def test_search_12(self):
        """厂家中输入药品名"""
        # sleep(1)
        # self.driver.back()
        # sleep(1)
        # self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        self.categories_page.click_py()  # 点击进入普药
        sleep(1)
        self.search_page.click_ssxzk()  # 点击搜索选择框
        sleep(1)
        self.search_page.click_cj()  # 点击厂家
        sleep(1)
        self.search_page.input_ssk("阿莫西林")  # 搜索框输入内容
        sleep(1)
        self.search_page.click_ssk()  # 点击模糊查找的第一个商品
        sleep(1)

