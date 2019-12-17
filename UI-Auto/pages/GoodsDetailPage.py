# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage

# 继承BasePage类
class GoodsDetailPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    rhgm = (By.XPATH, "//*[@id='xiangqing']/div/div[2]/div[2]/div[1]/div[2]/a[1]/text()")  # 如何购买

    # 调用text，获取如何购买文本
    def text_rhgm(self):
        return self.find_element(*self.rhgm).text
