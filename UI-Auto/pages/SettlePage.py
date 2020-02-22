# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class SettlePage(BasePage):

    """金额不满200元时的提示文字内容"""
    wm200_1 = (By.CLASS_NAME, "ts_page")
    wm200_2 = (By.TAG_NAME, "p")
    def text_wm200(self):
        return self.find_element(*self.wm200_1).find_element(*self.wm200_2).text

    """金额不足200元时，点击返回首页"""
    fhsy = (By.LINK_TEXT, "返回首页")
    def click_fhsy(self):
        self.find_element(*self.fhsy).click()

    """金额不足200元时，点击返回购物车"""
    fhgwc = (By.LINK_TEXT, "返回购物车")
    def click_fhgwc(self):
        self.find_element(*self.fhgwc).click()

    """结算界面返回购物车"""
    jsfhgwc = (By.LINK_TEXT, "返回购物车")
    def click_jsfhgwc(self):
        self.find_element(*self.jsfhgwc).click()

    """订单备注输入框"""
    ddbz = (By.TAG_NAME, "textarea")
    def click_ddbz(self):
        self.find_element(*self.ddbz).click()
    def input_ddbz(self, bz):
        self.find_element(*self.ddbz).send_keys(bz)

    """提交订单"""
    tjdd = (By.ID, "btn")
    def click_tjdd(self):
        self.find_element(*self.tjdd).click()

    """获取订单信息列表"""
    ddxx = (By.CLASS_NAME, "weight")
    def text_info(self, listNumber):
        return self.find_elements(*self.ddxx)[listNumber].text
    def click_info(self, listNumber):
        self.find_element(*self.ddxx)[listNumber].click()
    def scroll_info(self, listNumber):
        target = self.driver.find_elements(*self.ddxx)[listNumber]
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    """获取单价文本"""
    dj = (By.CLASS_NAME, "dj")
    def text_dj(self):
        return self.find_element(*self.dj).click()

