# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage

# 继承BasePage类
class CategoriesPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    """商品列表中普药"""
    py = (By.LINK_TEXT, "普药")
    def click_py(self):
        self.find_element2(*self.py).click()

    """商品列表中诊所专区"""
    zszq = (By.LINK_TEXT, "诊所专区")
    def click_zszq(self):
        self.find_element(*self.zszq).click()

    """商品列表中器械"""
    qx = (By.LINK_TEXT, "器械")  # 商品列表中的器械
    def click_qx(self):
        self.find_element(*self.qx).click()

    """商品列表中中药专区"""
    zyzq = (By.LINK_TEXT, "中药专区")
    def click_zyzq(self):
        self.find_element(*self.zyzq).click()

    """商品列表中的品牌专区"""
    ppzq = (By.LINK_TEXT, "品牌专区")
    def click_ppzq(self, list):
        self.find_elements(*self.ppzq)[list].click()

    """商品列表中的促销专区"""
    cxzq = (By.LINK_TEXT, "促销专区")
    def click_cxzq(self, list):
        self.find_elements(*self.cxzq)[list].click()

    """商品列表中的精品专区"""
    jpzq = (By.LINK_TEXT, "精品专区")
    def click_jpzq(self):
        self.find_element(*self.jpzq).click()

    """商品列表中的积分商城"""
    jfsc = (By.LINK_TEXT, "积分商城")
    def click_jfsc(self):
        self.find_element(*self.jfsc).click()

    """全部商品分类,从1----12选择不同的分类"""
    qbspfl = (By.CLASS_NAME, "menu_title")
    def click_qbspfl(self, list):
        self.find_elements(*self.qbspfl)[list].click()

    list1_1 = (By.LINK_TEXT, "抗感冒类")
    def click_list1_1(self):
        self.find_element(*self.list1_1).click()

    list2_1 = (By.LINK_TEXT, "青霉素及头孢类")
    def click_list2_1(self):
        self.find_element(*self.list2_1).click()

    list3_1 = (By.LINK_TEXT, "眼科类")
    def click_list3_1(self):
        self.find_element(*self.list3_1).click()

    list4_1 = (By.LINK_TEXT, "解痉镇痛类")
    def click_list4_1(self):
        self.find_element(*self.list4_1).click()

    list5_1 = (By.LINK_TEXT, "调节免疫力类")
    def click_list5_1(self):
        self.find_element(*self.list5_1).click()

    list6_1 = (By.LINK_TEXT, "避孕类")
    def click_list6_1(self):
        self.find_element(*self.list6_1).click()

    list7_1 = (By.LINK_TEXT, "促白细胞增生类")
    def click_list7_1(self):
        self.find_element(*self.list7_1).click()

    list8_1 = (By.LINK_TEXT, "甾体激素类")
    def click_list8_1(self):
        self.find_element(*self.list8_1).click()

    list9_1 = (By.LINK_TEXT, "抗风湿类")
    def click_list9_1(self):
        self.find_element(*self.list9_1).click()

    list10_1 = (By.LINK_TEXT, "血液制品")
    def click_list10_1(self):
        self.find_element(*self.list10_1).click()

    list11_1 = (By.LINK_TEXT, "配方中药饮片")
    def click_list11_1(self):
        self.find_element(*self.list11_1).click()

    list12_1 = (By.LINK_TEXT, "功能性贴膏")
    def click_list12_1(self):
        self.find_element(*self.list12_1).click()



