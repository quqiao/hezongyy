# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys


# 继承BasePage类
class JiFenShangChengPage(BasePage):
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

    """礼品分类-热门兑换"""
    rmdh = (By.LINK_TEXT, "热门兑换")
    def click_rmdh(self):
        self.find_element(*self.rmdh).click()

    """礼品分类-家用电器"""
    jydq = (By.LINK_TEXT, "家用电器")
    def click_jydq(self):
        self.find_element(*self.jydq).click()

    """礼品分类-移动电器"""
    yddq = (By.LINK_TEXT, "移动电器")
    def click_yddq(self):
        self.find_element(*self.yddq).click()

    """礼品分类-办公用品"""
    bgyp = (By.LINK_TEXT, "办公用品")
    def click_bgyp(self):
        self.find_element(*self.bgyp).click()

    """积分首页"""
    jfsy = (By.LINK_TEXT, "积分首页")
    def click_jfsy(self):
        self.find_element(*self.jfsy).click()

    """个人中心"""
    grzx = (By.LINK_TEXT, "个人中心")
    def click_grzx(self):
        self.find_element(*self.grzx).click()

    """返回药易购"""
    fhyyg = (By.LINK_TEXT, "返回药易购")
    def click_fhyyg(self):
        self.find_element(*self.fhyyg).click()

    """商品加入购物车"""
    spjrgwc = (By.CLASS_NAME, "fr")
    def click_spjrgwc(self, splist):
        self.find_elements(*self.spjrgwc)[splist].click()

    """礼品车"""
    lpc = (By.CLASS_NAME, "lp_cart")
    def click_lpc(self):
        self.find_element(*self.lpc).click()

    """加入礼品车成功提示"""
    jrlpc = (By.CLASS_NAME, "layui-layer-content.layui-layer-padding")
    def text_jrlpc(self):
        return self.find_element(*self.jrlpc).text

    """商品大图"""
    spdt = (By.CLASS_NAME, "img_box")

    def click_spdt(self, tupian):
        self.find_elements(*self.spdt)[tupian].click()


