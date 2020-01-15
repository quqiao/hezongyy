# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.CategoriesPage import CategoriesPage
from common.public import PublicMethod
from selenium import webdriver
from time import sleep
from common.public import test_url, username

class TestCategories(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(5)  # 隐式等待
        cls.url = test_url
        cls.username = username
        cls.password = "123456"
        # 声明categoriesPage类对象
        cls.categories_page = CategoriesPage(cls.driver,cls.url, u"合纵药易购商品分类界面")
        # 声明publicMethod类对象
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵药易购商品分类界面")
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_Categories_01(self):
        """进入普药列表"""
        sleep(2)
        self.categories_page.click_py()  # 点击进入普药列表
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药

    def test_Categories_02(self):
        """进入诊所专区"""
        sleep(1)
        self.driver.back()  # 点击回到首页
        sleep(1)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(2)
        self.categories_page.click_zszq()  # 点击进入诊所专区
        sleep(0.5)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"诊所专区" in title)

    def test_Categories_03(self):
        """进入器械"""
        sleep(1)
        self.driver.back()  # 点击返回首页
        sleep(1)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(1.5)
        self.categories_page.click_qx()  # 点击进入器械专区
        sleep(0.5)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"器械专区" in title)

    def test_Categories_04(self):
        """进入中药专区"""
        sleep(1)
        self.driver.back()  # 点击返回首页
        sleep(1)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(0.5)
        self.categories_page.click_zyzq()  # 点击进入中药专区
        sleep(0.5)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"中药专区" in title)

    def test_Categories_05(self):
        """进入品牌专区"""
        sleep(1)
        self.driver.back()  # 点击返回首页
        sleep(1)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(0.5)
        self.categories_page.click_ppzq(1)  # 点击进入品牌专区
        sleep(0.5)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"品牌专区" in title)

    def test_Categories_06(self):
        """进入促销专区"""
        sleep(1)
        self.driver.back()  # 点击返回首页
        sleep(1)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(0.5)
        self.categories_page.click_cxzq(1)  # 点击进入促销专区
        sleep(0.5)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"促销专区" in title)

    def test_Categories_07(self):
        """进入精品专区"""
        sleep(1)
        self.driver.back()  # 点击返回首页
        sleep(1)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(0.5)
        self.categories_page.click_jpzq()  # 点击进入精品专区
        sleep(0.5)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"精品专区" in title)

    def test_Categories_08(self):
        """进入积分商城"""
        sleep(1)
        self.driver.back()  # 点击返回首页
        sleep(1)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(0.5)
        self.categories_page.click_jfsc()  # 点击进入积分商城
        sleep(0.5)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"积分商城" in title)

    def test_Categories_09(self):
        """商品分类——呼吸系统列表"""
        sleep(1)
        self.driver.back()  # 点击返回首页
        sleep(1)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(2)
        self.categories_page.click_qbspfl(0)  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list1_1()  #点击进入抗感冒类界面
        sleep(1)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药

    def test_Categories_10(self):
        """商品分类——清热，消炎列表"""
        sleep(1)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(1)  # 点击进入清热，消炎
        sleep(0.5)
        self.categories_page.click_list2_1()  # 点击进入青霉素及头孢类
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药

    def test_Categories_11(self):
        """商品分类——五官，皮肤及外用列表"""
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(2)  # 点击进入五官皮肤及外用
        sleep(0.5)
        self.categories_page.click_list3_1()  # 点击进入眼科类
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药

    def test_Categories_12(self):
        """商品分类——消化，肝胆系统列表"""
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(3)  # 点击进入消化，肝胆系统
        sleep(0.5)
        self.categories_page.click_list4_1()  # 点击进入解痉镇痛类
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药

    def test_Categories_13(self):
        """商品分类——补益安神及维矿类列表"""
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(4)  # 点击进入补益安神及维矿类
        sleep(0.5)
        self.categories_page.click_list5_1()  # 点击进入调节免疫力类
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药


    def test_Categories_14(self):
        """商品分类——妇、儿科列表"""
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(5)  # 点击进入妇，儿科类
        sleep(0.5)
        self.categories_page.click_list6_1()  # 点击进入避孕类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药

    def test_Categories_15(self):
        """商品分类——心脑血管及神经类用药列表"""
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(6)  # 点击进入心脑血管及神经类用药
        sleep(0.5)
        self.categories_page.click_list7_1()  # 点击促白细胞增生类
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药

    def test_Categories_16(self):
        """商品分类——内分泌系统（含糖尿病）列表"""
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(7)  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list8_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药

    def test_Categories_17(self):
        """商品分类——风湿骨伤及其他药品列表"""
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(8)  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list9_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药

    def test_Categories_18(self):
        """商品分类——特殊复方制剂、生物制品列表"""
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(9)  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list10_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药

    def test_Categories_19(self):
        """商品分类——中药饮片列表"""
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(10)  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list11_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"中药专区" in title)  # 判断标题中包含有普药

    def test_Categories_20(self):
        """商品分类——非药品列表"""
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_page.switch_home()  # 句柄切换回首页
        sleep(0.5)
        self.categories_page.click_qbspfl(11)  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list12_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"普药" in title)  # 判断标题中包含有普药
