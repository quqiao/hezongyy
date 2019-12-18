# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage

# 继承BasePage类
class GoodsDetailPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    bt = (By.CLASS_NAME, "biaoti")  # 标题

    # 调用text，获取如何购买文本
    def text_bt(self):
        return self.find_element(*self.bt).text
