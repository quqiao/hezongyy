# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep


# 继承BasePage类
class SearchPage(BasePage):
    """搜索选择框"""
    ssxzk = (By.ID, "search_select")
    def click_ssxzk(self):
        self.find_element(*self.ssxzk).click()

    """搜索框"""
    ssk = (By.CLASS_NAME, "search-input")
    def click_ssk(self):
        self.find_element(*self.ssk).click()
    def input_ssk(self, ssnr):
        self.find_element(*self.ssk).send_keys(ssnr)

    """搜索按钮"""
    ssButton = (By.CLASS_NAME, "search-btn")
    def click_ssButton(self):
        self.find_element(*self.ssButton).click()

    """药名"""
    ym = (By.CSS_SELECTOR, "# app > div > div.header-box > div.search-nav > div > div.search-box > div.search > div > ul > li:nth-child(1)")
    def click_ym(self):
        self.find_element(*self.ym).click()

    """厂家"""
    cj = (By.CSS_SELECTOR, "#app > div > div.header-box > div.search-nav > div > div.search-box > div.search > div > ul > li:nth-child(2)")
    def click_cj(self):
        self.find_element(*self.cj).click()

    "搜索为空"
    sswk = (By.CLASS_NAME, "link")
    def text_sswk(self):
        return self.find_element(*self.sswk).text

    "搜索列表第N个"
    # ssList1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.search-nav > div > div.search-box > div.search > ul > li:nth-child(1)")  #
    ssList1 = (By.CLASS_NAME, "search-list")
    sstag = (By.TAG_NAME, "li")
    "调用click,点击搜索列表第一个"
    def click_ssList1(self, listNumber):
        li = self.find_element(*self.ssList1)
        li.find_elements(*self.sstag)[listNumber].click()

    "搜索出商品的大图名字"
    spmz = (By.CLASS_NAME, "datu-mingzi")
    def text_spmz(self):
        return self.find_element(*self.spmz).text

    """搜索出商品的大图公司"""
    spgs = (By.CLASS_NAME, "datu-compamy")
    def text_spgs(self):
        return self.find_element(*self.spgs).text


