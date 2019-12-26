# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class JingPinZhuanQuPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    inputNumber1 = (By.XPATH, "//*[@id='goods_number_31505_0']")  # 第一个商品添加数量
    inputNumber2 = (By.XPATH, "//*[@id='goods_number_20560_0']")  # 第二个商品添加数量
    inputNumber3 = (By.XPATH, "//*[@id='goods_number_21788_0']")  # 第三个商品添加数量
    addCart1 = (By.XPATH, "//*[@id='datu']/div/ul/li[1]/div[8]/div[1]")  # 普药列表中第一个商品加入购物车
    addCart2 = (By.XPATH, "//*[@id='datu']/div/ul/li[2]/div[8]/div[1]")  # 普药列表中第二个商品加入购物车
    addCart3 = (By.XPATH, "//*[@id='datu']/div/ul/li[3]/div[8]/div[1]")  # 普药列表中第三个商品加入购物车



    # 调用send_keys对象，输入第一件商品数量
    def input_number1(self, shuliang):
        self.find_element(*self.inputNumber1).send_keys(shuliang)

    # 调用send_keys对象，输入第二件商品数量
    def input_number2(self, shuliang):
        self.find_element(*self.inputNumber2).send_keys(shuliang)

    # 调用send_keys对象，输入第三件商品数量
    def input_number3(self, shuliang):
        self.find_element(*self.inputNumber3).send_keys(shuliang)

    # 调用click对象，第一件商品加入购物车
    def click_addcart1(self):
        self.find_element(*self.addCart1).click()

    # 调用click对象，第二件商品加入购物车
    def click_addcart2(self):
        self.find_element(*self.addCart2).click()

    # 调用click对象，第三件商品加入购物车
    def click_addcart3(self):
        self.find_element(*self.addCart3).click()