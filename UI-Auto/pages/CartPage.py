# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage


# 继承BasePage类
class CartPage(BasePage):

    # 定位器，通过元素属性定位元素对象
    ad = (By.XPATH, "//*[@id='app']/div/div[1]/div/span/img")  # 点击关掉广告
    """test01"""
    puyao = (By.XPATH, "//*[@id='app']/div/div[3]/div[3]/div/ul/li[2]/ul/li[2]/a")  # 商品列表中的普药

    jiesuan = (By.XPATH, "//*[@id='jiesuan-btn']")  # 购物车界面结算按钮
    """test02"""
    addNumber = (By.CLASS_NAME, "add")  # 购物车界面增加数量
    minNumber = (By.CLASS_NAME, "min")  # 购物车界面减少数量
    inputNumber = (By.CLASS_NAME, "com_text goods-number")  # 购物车界面输入数量
    """test03"""
    qxk = (By.XPATH, "//*[@id='form']/div/div[2]/table[1]/tbody/tr/td[1]/input")  # 购物车界面全选框（上面一个）
    """test04"""
    sc = (By.CLASS_NAME, "del")  # 购物车界面删除指定
    sctsksc = (By.XPATH, "//*[@id='layui-layer1']/div[3]/a[1]")  # 删除提示框删除
    """test05"""
    ydsc = (By.CLASS_NAME, "collect")  # 购物车界面移到收藏
    sctskqd = (By.XPATH, "//*[@id='layui-layer7']/div[3]/a[1]")  # 收藏提示框确定框
    """test06"""
    scxz = (By.XPATH, "//*[@id='form']/div/div[2]/table[3]/tbody/tr/td[1]/p[2]/a")  # 购物车界面删除选中
    shctskqd = (By.XPATH, "//*[@id='layui-layer11']/div[3]/a[1]")  # 购物车界面删除提示框确定
    """test07"""
    scxj = (By.XPATH, "//*[@id='form']/div/div[2]/table[3]/tbody/tr/td[1]/p[3]/a/text()")  # 购物车界面删除无库存和下架商品
    scxjtskqd = (By.XPATH, "//*[@id='layui-layer12']/div[3]/a[1]")  # 购物车界面删除下架提示框确定
    """test08"""


    # Action
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 调用click，关掉广告
    def click_ad(self):
        self.find_element(*self.ad).click()

    # 调用click对象，点击普药
    def click_puyao(self):
        self.find_element(*self.puyao).click()

    # 调用text对象，检查是否进入购物车界面
    def text_jiesuan(self):
        return self.find_element(*self.jiesuan).text

    # 调用click对象，点击添加数量
    def click_addNumber(self):
        self.find_element(*self.addNumber).click()

    # 调用click对象,点击减少数量
    def click_minNumber(self):
        self.find_element(*self.minNumber).click()

    # 调用click对象，点击输入数量
    def input_number2(self, shuliang):
        self.find_element(*self.inputNumber).send_keys(shuliang)

    # 调用click对象，点击全选框
    def click_qxk(self):
        self.find_element(*self.qxk).click()

    # 调用click对象，点击指定商品删除
    def click_sc(self):
        self.find_element(*self.sc).click()

    # 调用click对象，点击删除提示框确认删除
    def click_sctsksc(self):
        self.find_element(*self.sctsksc).click()

    # 调用click对象，点击收藏提示框确认
    def click_sctskqd(self):
        self.find_element(*self.sctskqd).click()

    # 调用click对象，点击移到收藏
    def click_ydsc(self):
        self.find_element(*self.ydsc).click()

    # 调用click对象，点击删除选中
    def click_scxz(self):
        self.find_element(*self.scxz).click()

    # 调用click对象，点击删除提示框确定
    def click_shctskqd(self):
        self.find_element(*self.shctskqd).click()

    # 调用click对象，点击删除下架和无库存
    def click_scxj(self):
        self.find_element(*self.scxj).click()

    # 调用click对象，点击删除下架和无库存提示框
    def click_scxjtskqd(self):
        self.find_element(*self.scxjtskqd).click()

    # 调用click对象，点击结算按钮
    def click_jiesuan(self):
        self.find_element(*self.jiesuan).click()
