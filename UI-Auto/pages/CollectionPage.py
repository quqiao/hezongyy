# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep


# 继承BasePage类
class CollectionPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    qx = (By.CLASS_NAME, "quanxuan")  # 全选框
    def click_qx(self):
        self.find_element(*self.qx).click()

    jrgwc = (By.CLASS_NAME, "jrgwc")  # 加入购物车按钮
    def click_jrgwc(self):
        self.find_element(*self.jrgwc).click()

    qxsc = (By.CLASS_NAME, "qxsc")  # 取消收藏按钮
    def click_qxsc(self):
        self.find_element(*self.qxsc).click()

    dx = (By.CLASS_NAME, "danxuan")  # 每个单选框
    def click_dx(self, dxlist):
        self.find_elements(*self.dx)[dxlist].click()

    "检查是否存在删除选中商品和删除无库存商品"
    def is_sc_exist(self):
        list = self.driver.find_elements(*self.scxj)
        if len(list) == 0:
            # print('没有该元素')
            self.driver.back()
        elif len(list) >= 0:
            # print('共找到' + str(len(list)) + '个元素')
            self.find_elements(*self.scxj)[0].click()
            sleep(1)
            self.find_element(*self.shctskqd).click()
            sleep(1)
            self.driver.back()


    qb = (By.CSS_SELECTOR, "#sc1 > div.right_title > ul > a:nth-child(1) > li")  # 全部列表
    jpzq = (By.CSS_SELECTOR, "#sc1 > div.right_title > ul > a:nth-child(2) > li")  # 精品专区
    py = (By.CSS_SELECTOR, "#sc1 > div.right_title > ul > a:nth-child(3) > li")  #  普药
    zyyp = (By.CSS_SELECTOR, "#sc1 > div.right_title > ul > a:nth-child(4) > li")  # 中药饮片
    # pl_buy > table > tbody > tr:nth-child(2) > td.cz > img.jrgwc.fly_to_cart18059
