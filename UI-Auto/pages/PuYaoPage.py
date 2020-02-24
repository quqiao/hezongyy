# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class PuYaoPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    addNumber = (By.CLASS_NAME, "input_val")  # 商品列表中添加数量

    # 调用send_keys对象，输入购买数量
    def input_number(self, sp, shuliang):
        self.find_elements(*self.addNumber)[sp].send_keys(shuliang)

    # 调用click对象，第N件商品加入购物车,适用于精品专区，搜索等页面商品列表
    addCart = (By.CLASS_NAME, "datu-jrgwc")
    def click_addcart(self, shuliang):
        jrgwc = self.find_elements(*self.addCart)[shuliang]
        self.script2("arguments[0].click();", jrgwc)
