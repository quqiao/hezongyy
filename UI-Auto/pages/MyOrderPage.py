# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.webdriver.support.select import Select


# 继承BasePage类
class MyOrderPage(BasePage):
    """全部订单"""
    qbdd = (By.LINK_TEXT, "全部订单")
    def click_qbdd(self):
        self.find_element(*self.qbdd).click()

    """待付款"""
    dfk = (By.LINK_TEXT, "待付款")
    def click_dfk(self):
        self.find_element(*self.dfk).click()

    """待收货"""
    dsh = (By.LINK_TEXT, "待收货")
    def click_dsh(self):
        self.find_element(*self.dsh).click()

    """近三个月，今年内，往年订单"""
    sj_select = (By.NAME, "dates")
    def sj_select_by_value(self, valueNumber):
        s1 = Select(self.find_element(*self.sj_select))
        s1.select_by_value(valueNumber)

    """订单编号输入框"""
    ddInput = (By.CLASS_NAME, "num.num")
    def input_ddInput(self, content):
        self.clear_text(*self.ddInput)
        self.find_element(*self.ddInput).send_keys(content)

    """查询按钮"""
    cx = (By.ID, "btn")
    def click_cx(self):
        self.find_element(*self.cx).click()

    """订单状态"""
    ddzt1 = (By.CLASS_NAME, "select_zt")
    ddzt2 = (By.TAG_NAME, "li")
    def click_ddzt(self):
        d1 = self.find_element(*self.ddzt1)
        d1.self.find_element(*self.ddzt2).click()

    """再次购买"""
    zcgm = (By.LINK_TEXT, "再次购买")
    def click_zcgm(self):
        self.find_element(*self.zcgm).click()

    """查看详情"""
    ckxq = (By.LINK_TEXT, "查看详情")
    def click_ckxq(self):
        self.find_element(*self.ckxq).click()

    """回执"""
    hz = (By.LINK_TEXT, "回执")
    def click_hz(self):
        self.find_element(*self.hz).click()





