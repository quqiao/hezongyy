# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage

# 继承BasePage类
class GoodsDetailPage(BasePage):
    """标题"""
    bt = (By.CLASS_NAME, "biaoti")
    # 调用text，获取如何购买文本
    def text_bt(self):
        return self.find_element(*self.bt).text

    """会员价"""
    hyj = (By.CSS_SELECTOR,"#xiangqing > div > div.xq_main > div.xq_main_top > div.mid > div.price-box > div.right > p.cx-tips > s")
    def text_hyj(self):
        return self.find_element(*self.hyj).text

    """特价"""
    tj = (By.CSS_SELECTOR, "#xiangqing > div > div.xq_main > div.xq_main_top > div.mid > div.price-box > div.right > p.cx-tips")
    def text_tj(self):
        return self.find_element(*self.tj).text

    """加入购物车"""
    jrgwc = (By.ID, "jrgwc")  # 加入购物车
    def text_jrgwc(self):
        return self.find_element(*self.jrgwc).text
    def click_jrgwc(self):
        self.find_element(*self.jrgwc).click()

    """加入收藏"""
    jrsc = (By.ID, "jrsc")
    def text_jrsc(self):
        return self.find_element(*self.jrsc).text
    def click_jrsc(self):
        self.find_element(*self.jrsc).click()

    """购物车"""
    gwc = (By.CLASS_NAME, "gwc")
    def click_gwc(self):
        self.find_element(*self.gwc).click()