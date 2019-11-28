# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class HomePage(BasePage):
    # 定位器，通过元素属性定位元素对象
    ad = (By.XPATH, "//*[@id='app']/div/div[1]/div/span/img")  # 点击关掉广告
    mzjxTitle = (By.XPATH, "//*[@id='mzjx']/div/div[1]/span[1]")  # 每周精选标题
    WeekContent = (By.XPATH, "//*[@id='mzjx']/div/div[2]/div[1]")  # 每周精选内容
    CheckWeek = (By.XPATH, "//*[@id='jrgwc']")  # 检查每周精选



    # Action
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 调用click，关掉广告
    def click_ad(self):
        self.find_element(*self.ad).click()

    # 调用click对象，点击每周精选
    def click_week(self):
        self.find_element(*self.WeekContent).click()

    def scroll_page(self):
        target = self.driver.find_element_by_xpath(*self.mzjxTitle)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 调用text文本，检查每周精选
    def check_week(self):
        return self.find_element(*self.CheckWeek).text









