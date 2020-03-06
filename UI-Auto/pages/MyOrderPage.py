# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.webdriver.support.select import Select


# 继承BasePage类
class MyOrderPage(BasePage):
    """全部订单，待付款，待收货"""
    order_nav1 = (By.CLASS_NAME, "right_top_title_nav")
    order_nav2 = (By.TAG_NAME, "li")
    def click_order_nav(self, shuzi):
        s1 = self.find_element(*self.order_nav1)
        s1.find_elements(*self.order_nav2)[shuzi].click()

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

    """获取订单号"""
    ddh1 = (By.CLASS_NAME, "ddh")
    ddh2 = (By.TAG_NAME, "a")
    def get_ddh(self, ddh_list):
        s1 = self.find_elements(*self.ddh1)[ddh_list]
        return s1.find_element(*self.ddh2).text

    """订单状态"""
    ddzt1 = (By.CLASS_NAME, "ddzt")
    ddzt2 = (By.TAG_NAME, "div")
    ddzt3 = (By.CLASS_NAME, "select_zt")
    ddzt4 = (By.TAG_NAME, "li")
    def click_ddzt(self, zt):
        d2 = self.find_element(*self.ddzt1)
        d2.find_element(*self.ddzt2).click()
        d2 = self.find_element(*self.ddzt3)
        d2.find_elements(*self.ddzt4)[zt].click()

    """订单跟踪"""
    ddgz = (By.CLASS_NAME, "zhuizong")
    def click_ddgz(self):
        self.find_element(*self.ddgz).click()

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

    """去逛逛"""
    qgg = (By.LINK_TEXT, "去逛逛")
    def text_qgg(self):
        return self.find_element(*self.qgg).text

    """订单详情"""
    ddxq1 = (By.CLASS_NAME, "right_title")
    ddxq2 = (By.TAG_NAME, "span")
    def text_ddxq(self):
        s1 = self.find_element(*self.ddxq1)
        return s1.find_element(*self.ddxq2).text

    """切换到回执页面"""
    def switch_frame(self, loc):
        self.switch_frame(loc)

    """回执图片"""
    hztp = (By.CLASS_NAME, "text-r")
    def text_hztp(self):
        return self.find_element(*self.hztp).text

    """加入购物车成功"""
    cgts1 = (By.CLASS_NAME, "ts_page")
    cgts2 = (By.TAG_NAME, "p")
    def text_cgts(self):
        s1 = self.find_element(*self.cgts1)
        return s1.find_element(*self.cgts2).text

    """前往购物车结算"""
    qwgwcjs = (By.LINK_TEXT, "前往购物车结算")
    def click_qwgwcjs(self):
        self.find_element(*self.qwgwcjs).click()

    """返回我的订单"""
    fhwddd = (By.LINK_TEXT, "返回我的订单")
    def click_fhwddd(self):
        self.find_element(*self.fhwddd).click()






