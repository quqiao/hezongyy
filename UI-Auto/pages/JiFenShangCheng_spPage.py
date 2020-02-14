# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys


# 继承BasePage类

class JiFenShangCheng_spPage(BasePage):
    """数量减"""
    jian = (By.CLASS_NAME, "jian")
    def click_jian(self):
        self.find_element(*self.jian).click()

    """数量加"""
    jia = (By.CLASS_NAME, "jia")
    def click_jia(self):
        self.find_element(*self.jia).click()

    """输入数量"""
    srsl = (By.ID, "num_btn")
    def input_srsl(self, shuliang):
        self.clear_text(*self.srsl)
        self.find_element(*self.srsl).send_keys(shuliang)
    def text_srsl(self):
        return self.find_element(*self.srsl).text

    """立即兑换"""
    ljdh = (By.CLASS_NAME, "dh")
    def click_ljdh(self):
        self.find_element(*self.ljdh).click()

    """加入礼品车"""
    jrlpc = (By.CLASS_NAME, "jr")
    def click_jrlpc(self):
        self.find_element(*self.jrlpc).click()

    """礼品详情"""
    lpxq1 = (By.CLASS_NAME, "xiangqing_title")
    lpxq2 = (By.TAG_NAME, "span")
    def text_lpxq(self):
        return self.find_element(*self.lpxq1).find_element(*self.lpxq2).text

    """库存数量"""
    kc1 = (By.CLASS_NAME, "kucun")
    kc2 = (By.TAG_NAME, "span")
    def text_kc(self):
        return self.find_element(*self.kc1).find_element(*self.kc2).text