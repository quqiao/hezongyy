# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class ZhongYaoPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    gwc = (By.CLASS_NAME, "gwc.fl")  # 购物车按钮
    ljqg = (By.CLASS_NAME, "btn")  # 立即抢购

    def click_gwc(self):
        self.find_element(*self.gwc).click()

    def click_ljqg1(self):
        self.find_elements(*self.ljqg)[0].click()

    def click_ljqg2(self):
        self.find_elements(*self.ljqg)[1].click()



