# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class TeJiaPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    qyts = (By.XPATH, "//*[@id='layui-layer']/div")  # 非区域会员
    zdts = (By.XPATH, "//*[@id='layui-layer2']/div")  # 非终端会员
    jrgwc = (By.CSS_SELECTOR, "#app > div.ivu-layout-content > div.tj > div.goods > div > div.goods-items > div:nth-child(1) > div.text-box > div > button:nth-child(1)")
    yxgpz = (By.CSS_SELECTOR, "#app > div.ivu-layout-content > div.tj > div.goods > div > div.classify > div > div.left > span:nth-child(8)")  # 已选购列表
    ssk = (By.CSS_SELECTOR, "#app > div.ivu-layout-content > div.tj > div.goods > div > div.classify > div > div.right > div > input[type=text]")  # 搜索框
    ssButton = (By.CSS_SELECTOR, "#app > div.ivu-layout-content > div.tj > div.goods > div > div.classify > div > div.right > div > button")  # 搜索按钮
    spTitle = (By.CLASS_NAME, "title")  # 商品名称
    yj = (By.CSS_SELECTOR, "#app > div.ivu-layout-content > div.tj > div.goods > div > div.goods-items > div:nth-child(1) > div.text-box > p.price > s")  # 原件
    tj = (By.CSS_SELECTOR, "#app > div.ivu-layout-content > div.tj > div.goods > div > div.goods-items > div:nth-child(1) > div.text-box > p.price")  # 特价
    spdt = (By.XPATH, "#app > div.ivu-layout-content > div.tj > div.goods > div > div.goods-items > div:nth-child(1) > div.img-box > img:nth-child(1)")  # 第一个商品的大图




    def text_qyts(self):
        return self.find_element(*self.qyts).text

    def text_zdts(self):
        return self.find_element(*self.zdts).text

    def text_jrgwc(self):
        return self.find_element(*self.jrgwc).text

    def click_jrgwc(self):
        self.find_element(*self.jrgwc).click()

    def click_yxgpz(self):
        self.find_element(*self.yxgpz).click()

    def input_ssk(self, content):
        self.find_element(*self.ssk).send_keys(content)

    def click_ssButton(self):
        self.find_element(*self.ssButton).click()

    def text_spTitle(self):
        return self.find_element(*self.spTitle).text

    def text_yj(self):
        return self.find_element(*self.yj).text

    def text_tj(self):
        return self.find_element(*self.tj).text

    def click_spdt(self):
        self.find_element(*self.spdt).click()



