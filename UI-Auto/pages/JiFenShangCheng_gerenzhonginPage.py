# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys


# 继承BasePage类
class JiFenShangCheng_gerenzhongxinPage(BasePage):
    """订单详情"""
    ddxq = (By.LINK_TEXT, "订单详情")
    def click_ddxq(self):
        self.find_element(*self.ddxq).click()

    """我的积分"""
    wdjf = (By.LINK_TEXT, "我的积分")
    def click_wdjf(self):
        self.find_element(*self.wdjf).click()

    """去兑换礼品"""
    dhlp = (By.LINK_TEXT, "去兑换礼品")
    def click_dhlp(self):
        self.find_element(*self.dhlp).click()

    """去赚取积分"""
    zqjf = (By.LINK_TEXT, "去赚取积分")
    def click_zqjf(self):
        self.find_element(*self.zqjf).click()

    """我的地址"""
    wddd = (By.LINK_TEXT, "收货地址")
    def click_wddd(self):
        self.find_element(*self.wddd).click()

    """为你推荐"""
    wntj = (By.CLASS_NAME, "wntj-cp")
    def click_wntj(self, list):
        self.find_elements(*self.wntj)[list].click()

    """个人中心"""
    grzx = (By.CLASS_NAME, "vip_left_title")
    def text_grzx(self):
        return self.find_element(*self.grzx).text