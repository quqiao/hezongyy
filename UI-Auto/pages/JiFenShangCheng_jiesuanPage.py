# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys


# 继承BasePage类
class JiFenShangCheng_jiesuanPage(BasePage):
    """兑换成功提示"""
    dhcg = (By.CLASS_NAME, "success_title")
    def text_dhcg(self):
        return self.find_element(*self.dhcg).text

    """确认提交"""
    submit = (By.ID, "btn")
    def click_submit(self):
        self.find_element(*self.submit).click()
    def text_submit(self):
        return self.find_element(*self.submit).text

    """返回礼品车"""
    fhlpc = (By.LINK_TEXT, "返回礼品车")
    def click_fhlpc(self):
        self.find_element(*self.fhlpc).click()
    def text_fhlpc(self):
        return self.find_element(*self.fhlpc).text
