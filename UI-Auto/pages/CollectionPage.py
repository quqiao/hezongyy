# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep


# 继承BasePage类
class CollectionPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    """全选框"""
    qx = (By.CLASS_NAME, "quanxuan")
    def click_qx(self):
        self.find_element(*self.qx).click()

    """列表删除"""
    lbsc = (By.CLASS_NAME, "shanchu")
    def click_lbsc(self):
        self.find_element(*self.lbsc).click()

    """加入购物车"""
    jrgwc = (By.CLASS_NAME, "jrgwc")
    def click_jrgwc(self):
        self.find_element(*self.jrgwc).click()
    def text_jrgwc(self):
        return self.find_element(*self.jrgwc).text

    """取消收藏按钮"""
    qxsc = (By.CLASS_NAME, "qxsc")
    def click_qxsc(self):
        self.find_element(*self.qxsc).click()
    def text_qxsc(self):
        return self.find_element(*self.qxsc).text

    """每个单选框"""
    dx = (By.CLASS_NAME, "danxuan")
    def click_dx(self, dxlist):
        self.find_elements(*self.dx)[dxlist].click()

    "检查是否存在删除选中商品和删除无库存商品"
    def is_sc_exist(self):
        list = self.driver.find_elements(*self.jrgwc)
        if len(list) == 0:
            # print('没有该元素')
            pass
        elif len(list) >= 0:
            # print('共找到' + str(len(list)) + '个元素')
            self.find_element(*self.qx).click()
            sleep(1)
            self.find_element(*self.qxsc).click()

    """去逛逛"""
    qqq = (By.PARTIAL_LINK_TEXT, "去逛逛")
    def click_qqq(self):
        self.find_element(*self.qqq).click()
    def text_qqq(self):
        return self.find_element(*self.qqq).text

    """全部"""
    qb = (By.CSS_SELECTOR, "#sc1 > div.right_title > ul > a:nth-child(1) > li")
    def click_qb(self):
        self.find_element(*self.qb).click()

    """精品专区"""
    jpzq = (By.CSS_SELECTOR, "#sc1 > div.right_title > ul > a:nth-child(2) > li")
    def click_jpzq(self):
        self.find_element(*self.jpzq).click()

    """普药"""
    py = (By.CSS_SELECTOR, "#sc1 > div.right_title > ul > a:nth-child(3) > li")
    def click_py(self):
        self.find_element(*self.py).click()

    """中药饮片"""
    zyyp = (By.CSS_SELECTOR, "#sc1 > div.right_title > ul > a:nth-child(4) > li")
    def click_zyyp(self):
        self.find_element(*self.zyyp).click()
