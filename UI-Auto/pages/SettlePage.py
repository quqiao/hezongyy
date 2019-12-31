# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class SettlePage(BasePage):
    # 定位器，通过元素属性定位元素对象
    fhsy = (By.XPATH, "//*[@id='app']/div/div[3]/a[1]")  # 金额不足200元时返回首页
    fhgwc = (By.XPATH, "//*[@id='app']/div/div[3]/a[2]")  # 金额不足200元时，返回购物车
    jsfhgwc = (By.XPATH, "//*[@id='app']/div/div[3]/div[1]/a")  # 结算界面返回购物车
    ddbz = (By.XPATH, "//*[@id='app']/div/div[3]/div[6]/div[2]/textarea")  # 结算界面，订单备注输入框
    tjdd = (By.XPATH, "//*[@id='btn']")  # 结算界面，提交订单
    ddxx = (By.CLASS_NAME, "weight")  # 订单信息列表
    wm200 = (By.XPATH, "//*[@id='app']/div/div[3]/p")  # 未满200元时的提示
    dj = (By.CLASS_NAME, "dj")  # 单价

    # 调用text，金额不满200元时的提示
    def text_wm200(self):
        return self.find_element(*self.wm200).text

    # 调用click，金额不足200元时，点击返回首页
    def click_fhsy(self):
        self.find_element(*self.fhsy).click()

    # 调用click,金额不足200元时，点击返回购物车
    def click_fhgwc(self):
        self.find_element(*self.fhgwc).click()

    # 调用click,结算界面返回购物车
    def click_jsfhgwc(self):
        self.find_element(*self.jsfhgwc).click()

    # 调用input， 订单备注中输入一些内容
    def input_ddbz(self, bz):
        self.find_element(*self.ddbz).send_keys(bz)

    # 调用click，提交订单
    def click_tjdd(self):
        self.find_element(*self.tjdd).click()

    # 调用text,获取订单信息列表
    def text_info(self, listNumber):
        return self.find_elements(*self.ddxx)[listNumber].text

    # 调用text，获取单价文本
    def text_dj(self):
        return self.find_element(*self.dj).click()

