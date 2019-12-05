# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.CategoriesPage import CategoriesPage
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
        cls.phone = "18056558899"
        cls.password = "123456"
        # 声明categoriesPage类对象
        cls.categories_page = CategoriesPage(cls.driver,cls.url, u"合纵药易购商品分类界面")
        # 声明publicMethod类对象
        cls.public_method = PublicMethod(cls.driver, cls.url, u"合纵药易购商品分类界面")
        cls.public_method.open()
        # 关掉广告
        cls.public_method.click_ad()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test_Categories_01(self):
    #     """进入普药列表"""
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告
    #     sleep(0.5)
    #     self.categories_page.click_py()  # 点击进入普药列表
    #     sleep(0.5)
    #     self.driver.back()  # 点击回到首页
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告


    # def test_Categories_02(self):
    #     """进入诊所专区"""
    #     sleep(0.5)
    #     self.categories_page.click_zszq()  # 点击进入诊所专区
    #     sleep(0.5)
    #     self.driver.back()  # 点击返回首页
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告
    #
    # def test_Categories_03(self):
    #     """进入器械"""
    #     sleep(0.5)
    #     self.categories_page.click_qx()  # 点击进入器械专区
    #     sleep(0.5)
    #     self.driver.back()  # 点击返回首页
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告
    #
    # def test_Categories_04(self):
    #     """进入中药专区"""
    #     sleep(0.5)
    #     self.categories_page.click_zyzq()  # 点击进入中药专区
    #     sleep(0.5)
    #     self.driver.back()  # 点击返回首页
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告
    #
    # def test_Categories_05(self):
    #     """进入品牌专区"""
    #     sleep(0.5)
    #     self.categories_page.click_ppzq()  # 点击进入品牌专区
    #     sleep(0.5)
    #     self.driver.back()  # 点击返回首页
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告
    #
    # def test_Categories_06(self):
    #     """进入促销专区"""
    #     sleep(0.5)
    #     self.categories_page.click_cxzq()  # 点击进入促销专区
    #     sleep(0.5)
    #     self.driver.back()  # 点击返回首页
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告
    #
    # def test_Categories_07(self):
    #     """进入精品专区"""
    #     sleep(0.5)
    #     self.categories_page.click_jpzq()  # 点击进入精品专区
    #     sleep(0.5)
    #     self.driver.back()  # 点击返回首页
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告
    #
    # def test_Categories_08(self):
    #     """进入积分商城"""
    #     sleep(0.5)
    #     self.categories_page.click_jfsc()  # 点击进入积分商城
    #     sleep(0.5)
    #     self.driver.back()  # 点击返回首页
    #     sleep(1)
    #     self.public_method.click_ad()  # 关掉广告
    #
    # def test_Categories_09(self):
    #     """商品分类——呼吸系统列表"""
    #     sleep(5)
    #     self.categories_page.click_list1()  # 点击进入呼吸系统分类选择
    #     sleep(0.5)
    #     self.categories_page.click_list1_1()  #点击进入抗感冒类界面
    #     sleep(1)
    #     self.public_method.switch_secendPage()  # 句柄切换到第二页上
    #     sleep(0.5)
    #     self.driver.close()  # 退出当前页面
    #     sleep(0.5)
    #     self.public_method.switch_home()  # 句柄切换回首页
    #
    # def test_Categories_10(self):
    #     """商品分类——清热，消炎列表"""
    #     sleep(0.5)
    #     self.categories_page.click_list2()  # 点击进入呼吸系统分类选择
    #     sleep(0.5)
    #     self.categories_page.click_list2_1()  #点击进入抗感冒类界面
    #     sleep(0.5)
    #     self.public_method.switch_secendPage()  # 句柄切换到第二页上
    #     sleep(0.5)
    #     self.driver.close()  # 退出当前页面
    #     sleep(0.5)
    #     self.public_method.switch_home()  # 句柄切换回首页
    #
    # def test_Categories_11(self):
    #     """商品分类——五官，皮肤及外用列表"""
    #     sleep(0.5)
    #     self.categories_page.click_list3()  # 点击进入呼吸系统分类选择
    #     sleep(0.5)
    #     self.categories_page.click_list3_1()  # 点击进入抗感冒类界面
    #     sleep(0.5)
    #     self.public_method.switch_secendPage()  # 句柄切换到第二页上
    #     sleep(0.5)
    #     self.driver.close()  # 退出当前页面
    #     sleep(0.5)
    #     self.public_method.switch_home()  # 句柄切换回首页
    #
    # def test_Categories_12(self):
    #     """商品分类——消化，肝胆系统列表"""
    #     sleep(0.5)
    #     self.categories_page.click_list4()  # 点击进入呼吸系统分类选择
    #     sleep(0.5)
    #     self.categories_page.click_list4_1()  #点击进入抗感冒类界面
    #     sleep(0.5)
    #     self.public_method.switch_secendPage()  # 句柄切换到第二页上
    #     sleep(0.5)
    #     self.driver.close()  # 退出当前页面
    #     sleep(0.5)
    #     self.public_method.switch_home()  # 句柄切换回首页

    def test_Categories_13(self):
        """商品分类——补益安神及维矿类列表"""
        sleep(0.5)
        self.categories_page.click_list5()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list5_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_method.switch_secendPage()  # 句柄切换到第二页上
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_method.switch_home()  # 句柄切换回首页

    def test_Categories_14(self):
        """商品分类——妇、儿科列表"""
        sleep(0.5)
        self.categories_page.click_list6()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list6_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_method.switch_secendPage()  # 句柄切换到第二页上
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_method.switch_home()  # 句柄切换回首页

    def test_Categories_15(self):
        """商品分类——心脑血管及神经类用药列表"""
        sleep(0.5)
        self.categories_page.click_list7()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list7_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_method.switch_secendPage()  # 句柄切换到第二页上
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_method.switch_home()  # 句柄切换回首页

    def test_Categories_16(self):
        """商品分类——内分泌系统（含糖尿病）列表"""
        sleep(0.5)
        self.categories_page.click_list8()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list8_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_method.switch_secendPage()  # 句柄切换到第二页上
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_method.switch_home()  # 句柄切换回首页

    def test_Categories_17(self):
        """商品分类——风湿骨伤及其他药品列表"""
        sleep(0.5)
        self.categories_page.click_list9()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list9_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_method.switch_secendPage()  # 句柄切换到第二页上
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_method.switch_home()  # 句柄切换回首页

    def test_Categories_18(self):
        """商品分类——特殊复方制剂、生物制品列表"""
        sleep(0.5)
        self.categories_page.click_list10()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list10_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_method.switch_secendPage()  # 句柄切换到第二页上
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_method.switch_home()  # 句柄切换回首页

    def test_Categories_19(self):
        """商品分类——中药饮片列表"""
        sleep(0.5)
        self.categories_page.click_list11()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list11_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_method.switch_secendPage()  # 句柄切换到第二页上
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_method.switch_home()  # 句柄切换回首页

    def test_Categories_20(self):
        """商品分类——非药品列表"""
        sleep(0.5)
        self.categories_page.click_list12()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list12_1()  #点击进入抗感冒类界面
        sleep(0.5)
        self.public_method.switch_secendPage()  # 句柄切换到第二页上
        sleep(0.5)
        self.driver.close()  # 退出当前页面
        sleep(0.5)
        self.public_method.switch_home()  # 句柄切换回首页





# if __name__ == "__main__":
#     unittest.main()
