# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class HomePage(BasePage):

    # 定位器，通过元素属性定位元素对象
    ad = (By.XPATH, "//*[@id='app']/div/div[1]/div/span/img")  # 点击关掉广告
    list1 = (By.XPATH, "//*[@id='app']/div/div[1]/div[3]/div/ul/li[1]/div[2]/div/div[1]/div[1]/div[2]")  # 呼吸系统用药列表
    CheckList1 = (By.XPATH, "//*[@id='app']/div/div[1]/div[3]/div/ul/li[1]/div[2]/div/div[1]/div[2]/div[1]")    # 检查呼吸系统用药检查
    list2 = (By.XPATH, "//*[@id='app']/div/div[1]/div[3]/div/ul/li[1]/div[2]/div/div[2]/div[1]/div[2]")  # 清热消炎列表
    CheckList2 = (By.XPATH, "//*[@id='app']/div/div[1]/div[3]/div/ul/li[1]/div[2]/div/div[2]/div[2]/div[1]")  # 检查清热消炎检查


    # Action
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 调用click，关掉广告
    def click_ad(self):
        self.find_element(*self.ad).click()

    # 调用click对象，点击呼吸系统用药列表
    def click_list1(self):
        self.find_element(*self.list1).click()

    # 调用text文本，检查列表显示
    def check_list1(self):
        return self.find_element(*self.CheckList1).text

    # 调用click对象，点击清热消炎列表
    def click_list2(self):
        self.find_element(*self.list2).click()

    # 调用text文本，检查清热消炎列表显示
    def check_list2(self):
        return self.find_element(*self.CheckList2).text
