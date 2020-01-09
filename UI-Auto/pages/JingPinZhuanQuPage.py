# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class JingPinZhuanQuPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    inputNumber1 = (By.XPATH, "//*[@id='goods_number_31505_0']")  # 第一个商品添加数量
    inputNumber2 = (By.XPATH, "//*[@id='goods_number_20560_0']")  # 第二个商品添加数量
    inputNumber3 = (By.XPATH, "//*[@id='goods_number_21788_0']")  # 第三个商品添加数量


    """第N件商品输入数量"""
    inputNumber = (By.CLASS_NAME, "input_val")
    def click_inputNumber(self, sp, shuliang):
        self.find_elements(*self.inputNumber)[sp].send_keys(shuliang)

    """第N件商品加入购物车"""
    addCart = (By.CLASS_NAME, "datu-jrgwc")
    def click_addcart(self, shuliang):
        jrgwc = self.find_elements(*self.addCart)[shuliang]
        self.script2("arguments[0].click();", jrgwc)
