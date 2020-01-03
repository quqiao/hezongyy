# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class ZhongYaoPage(BasePage):
    # 定位器，通过元素属性定位元素对象

    "购物车按钮"
    gwc = (By.CLASS_NAME, "gwc.fl")
    def click_gwc(self):
        self.find_element(*self.gwc).click()

    "立即抢购"
    ljqg = (By.CLASS_NAME, "btn")
    def click_ljqg1(self, ljqgList):
        self.find_elements(*self.ljqg)[ljqgList].click()




