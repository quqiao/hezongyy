# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys


# 继承BasePage类

class JiFenShangCheng_qiandaoPage(BasePage):
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

    """立即兑换"""
    ljdh = (By.CLASS_NAME, "dh")
    def click_ljdh(self):
        self.find_element(*self.ljdh).click()

    """加入礼品车"""
    jrlpc = (By.CLASS_NAME, "jr")
    def click_jrlpc(self):
        self.find_element(*self.jrlpc).click()