# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage

# 继承BasePage类
class GoodsDetailPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    bt = (By.CLASS_NAME, "biaoti")  # 标题
    hyj = (By.CSS_SELECTOR, "#xiangqing > div > div.xq_main > div.xq_main_top > div.mid > div.price-box > div.right > p.cx-tips > s")  # 会员价
    tj = (By.CSS_SELECTOR, "#xiangqing > div > div.xq_main > div.xq_main_top > div.mid > div.price-box > div.right > p.cx-tips")  # 特价
    jrgwc = (By.ID, "jrgwc")  # 加入购物车

    # 调用text，获取如何购买文本
    def text_bt(self):
        return self.find_element(*self.bt).text

    def text_hyj(self):
        return self.find_element(*self.hyj).text

    def text_tj(self):
        return self.find_element(*self.tj).text

    def click_jrgwc(self):
        self.find_element(*self.jrgwc).click()

