# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class HomePage(BasePage):
    """签到"""
    qd = (By.LINK_TEXT, "[签到]")
    def click_qd(self):
        self.find_element(*self.qd).click()

    """积分订单"""
    jfdd = (By.LINK_TEXT, "[积分订单]")
    def click_jfdd(self):
        self.find_element(*self.jfdd).click()

    """去赚取积分"""
    qzqjf = (By.LINK_TEXT, "[去赚取积分]")
    def click_qzqjf(self):
        self.find_element(*self.qzqjf).click()

    """"""

    """热门兑换商品加入购物车"""
    spjrgwc = (By.CLASS_NAME, "fr")
    def click_spjrgwc(self, splist):
        self.find_elements(*self.spjrgwc)[splist].click()