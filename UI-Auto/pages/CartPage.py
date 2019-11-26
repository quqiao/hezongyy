# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage

# 继承BasePage类
class CartPage(BasePage):

    # 定位器，通过元素属性定位元素对象
    usernameloc = (By.XPATH, "//*[@id='username']")
    passwordloc = (By.XPATH, "//*[@id='password']")
    submit = (By.XPATH, "//*[@id='right_1']/a")
    errorMsg1 = (By.CLASS_NAME, "prompt2")  # 用户名出现的提示
    errorMsg2 = (By.XPATH, "//*[@id='right_1']/p[2]/span[2]")  # 密码错误出现的提示
    loginuser = (By.XPATH, "//*[@id='app']/div/div[1]/div[1]/div/ul[1]/li[4]/a")
    puyao = (By.XPATH, "//*[@id='app']/div/div[1]/div[3]/div/ul/li[2]/ul/li[2]")  # 商品列表中的普药
    addShuliang = (By.XPATH, "//*[@id='goods_number_2190_0']")   # 商品列表中添加数量
    addCart = (By.XPATH, "//*[@id='datu']/div/ul/li[2]/div[8]/div[1]")  # 普药列表中加入购物车

    # 调用send_keys对象，输入用户名
    def input_username(self, username):
        self.find_element(*self.usernameloc).send_keys(username)

    # 调用send_keys对象，输入密码
    def input_password(self, password):
        self.find_element(*self.passwordloc).send_keys(password)

    # 调用click对象，点击登录
    def click_submit(self):
        self.find_element(*self.submit).click()

    # 调用click对象，点击普药
    def click_puyao(self):
        self.find_element(*self.puyao).click()

    # 调用send_keys对象，输入购买数量
    def input_number(self,shuliang):
        self.find_element(*self.addShuliang).send_keys(shuliang)

    # 调用click对象，点击加入购物车
    def add_cart(self):
        self.find_element(*self.addCart).click()