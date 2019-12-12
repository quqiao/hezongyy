# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage


# 继承BasePage类
class OrderPage(BasePage):
    cgts = (By.XPATH, "//*[@id='app']/div/div[4]/div[2]/div[1]/p")  # 提交订单后的成功提示
    fhsy = (By.XPATH, "//*[@id='app']/div/div[4]/div[3]/a[1]")  # 订单界面返回首页
    fhwdyyg = (By.XPATH, "//*[@id='app']/div/div[4]/div[3]/a[2]")  # 订单界面返回我的药易购


    # 获取该元素的文本文字
    def text_cgts(self):
        return self.find_element(*self.cgts).text

    # 调用click对象，点击返回首页
    def click_fhsy(self):
        self.find_element(*self.fhsy).click()

    # 调用click对象，点击返回我的药易购
    def click_fhwdyyg(self):
        self.find_element(*self.fhwdyyg)

