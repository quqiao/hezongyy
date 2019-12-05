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

