# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys


# 继承BasePage类
class JiFenShangCheng_lipinchePage(BasePage):
    """结算"""
    jsButton = (By.ID, "jiesuan")
    def get_jsButton(self):
        return self.find_element(*self.jsButton).get_attribute("value")

    """礼品车去逛逛"""
    qgg = (By.LINK_TEXT, "去逛逛")
    def click_qgg(self):
        self.find_element(*self.qgg).click()
    def text_qgg(self):
        return self.find_element(*self.qgg).text

    """判断购物车是否有商品"""
    sc = (By.CLASS_NAME, "delete")  # 礼品列表删除
    tsk = (By.CLASS_NAME, "layui-layer-btn0")  # 提示框确定
    def is_element_exist(self):
        for i in range(100):
            list = self.driver.find_elements(*self.gwclb)
            if len(list) == 0:
                # print('没有该元素')
                break
            elif len(list) >= 0:
                # print('共找到' + str(len(list)) + '个元素')
                self.find_element(*self.sc).click()
                sleep(1)
                self.find_element(*self.tsk).click()

    """判断购物车列表是否存在"""
    gwclb = (By.CLASS_NAME, "cart_list")
    def isElementPresent(self):
        """
        用来判断元素标签是否存在，
        """
        try:
            element = self.driver.find_element(*self.gwclb)
        # 原文是except NoSuchElementException, e:
        except NoSuchElementException as e:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True

    """数量增加"""
    sljia = (By.CLASS_NAME, "jia")  # 数量增加
    def click_sljia(self, sp):
        self.find_elements(*self.sljia)[sp].click()

    """数量减少"""
    sljian = (By.CLASS_NAME, "jian")  # 数量减
    def click_sljian(self, sp):
        self.find_elements(*self.sljian)[sp].click()

    """数量输入"""
    slInput = (By.CLASS_NAME, "input_val.goods_num")
    def input_number(self, shuliang, listNumber):
        self.find_elements(*self.slInput)[listNumber].click()
        self.find_elements(*self.slInput)[listNumber].send_keys(Keys.CONTROL, "a")
        self.find_elements(*self.slInput)[listNumber].send_keys(Keys.DELETE)
        self.find_elements(*self.slInput)[listNumber].clear()
        self.find_elements(*self.slInput)[listNumber].send_keys(shuliang)

    """单选"""
    dx = (By.CLASS_NAME, "danxuan")
    def click_dx(self, dxk):
        self.find_elements(*self.dx)[dxk].click()

    """全选"""
    qx = (By.CLASS_NAME, "quanxuan")
    def click_qx(self, qxk):
        self.find_elements(*self.qx)[qxk].click()

    """删除"""
    def click_sc(self, sc):
        self.find_elements(*self.sc)[sc].click()

    """结算"""
    jiesuan = (By.ID, "jiesuan")
    def click_jiesuan(self):
        self.find_element(*self.jiesuan).click()

    """提示请选择要购买的商品"""
    tsgmsp = (By.CLASS_NAME, "layui-layer-content.layui-layer-padding")
    def text_tsgmsp(self):
        return self.find_element(*self.tsgmsp).text