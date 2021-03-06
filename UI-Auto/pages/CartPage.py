# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep


# 继承BasePage类
class CartPage(BasePage):

    # 定位器，通过元素属性定位元素对象
    jiesuan = (By.XPATH, "//*[@id='jiesuan-btn']")  # 购物车界面结算按钮
    jiage = (By.CLASS_NAME, "tb2_td11.subtotal")  # 购物车界面，第一个商品总价
    yxspsl = (By.XPATH, "//*[@id='count']")  # 已选中商品数量
    sccg = (By.CLASS_NAME, "layui-layer-content.layui-layer-padding")  # 删除成功后的提示
    ydsccg = (By.CLASS_NAME, "layui-layer-content.layui-layer-padding")  # 移到收藏后的提示
    gwcwk = (By.XPATH, "//*[@id='form']/div/div[2]/div/p[1]")  # 购物车为空时的提示
    xjspwk = (By.CLASS_NAME, "layui-layer-content.layui-layer-padding")  # 下架商品为空时的提示
    addNumber = (By.CLASS_NAME, "add")  # 购物车界面增加数量
    minNumber = (By.CLASS_NAME, "min")  # 购物车界面减少数量
    # inputNumber = (By.CLASS_NAME, "com_text goods-number")  # 购物车界面输入数量
    # inputNumber = (By.ID, "goods-number23650994")  #
    # inputNumber = (By.TAG_NAME, "input")  # 通过tagName来进行定位
    inputNumber = (By.CLASS_NAME, "com_text.goods-number")  # 通过className进行定位
    qxk = (By.XPATH, "//*[@id='form']/div/div[2]/table[1]/tbody/tr/td[1]/input")  # 购物车界面全选框（上面一个）
    sc = (By.CLASS_NAME, "del")  # 购物车界面删除指定
    ydsc = (By.CLASS_NAME, "collect")  # 购物车界面移到收藏
    scxj = (By.CLASS_NAME, "ico.del_all")  # 购物车界面删除无库存和下架商品
    dj1 = (By.CLASS_NAME, "tb2_td9")  # 单价
    dj2 = (By.TAG_NAME, "span")  # 单价
    wntjzh = (By.CLASS_NAME, "myicon.lb_left_icon")  # 为你推荐左滑
    wntjyh = (By.CLASS_NAME, "myicon.lb_right_icon")  # 为你推荐右滑
    wntjdt1 = (By.CLASS_NAME, "wntj-cp")  # 为你推荐大图

    # 调用text对象，输出单价文本
    def text_dj(self):
        dj = self.find_element(*self.dj1).find_element(*self.dj2)
        return dj.text

    # 调用text对象，检查是否进入购物车界面
    def text_jiesuan(self):
        return self.find_element(*self.jiesuan).text

    # 调用text对象，检查数量变化后，价格发生变化
    def text_jiage(self):
        return self.find_element(*self.jiage).text

    # 调用click,点击切换出输入框
    def click_jiage(self):
        self.find_element(*self.jiage).click()

    # 调用text对象，检查选中与否后数量的变化
    def text_yxspsl(self):
        return self.find_element(*self.yxspsl).text

    # 调用text对象，检查删除成功
    def text_sccg(self):
        return self.find_element(*self.sccg).text

    # 调用text对象，检查移到收藏成功
    def text_ydsccg(self):
        return self.find_element(*self.ydsccg).text

    # 调用text对象，检查购物车为空时
    def text_gwcwk(self):
        return self.find_element(*self.gwcwk).text

    # 调用text对象，检查删除无下架商品时
    def text_xjspwk(self):
        return self.find_element(*self.xjspwk).text

    # 调用click对象，点击添加数量
    def click_addNumber(self):
        self.find_element(*self.addNumber).click()

    # 调用click对象,点击减少数量
    def click_minNumber(self):
        self.find_element(*self.minNumber).click()

    # 调用click对象，点击第一个商品输入数量
    def input_number2(self, shuliang):
        '''通过tagName找到一个列表后查询所有'''
        # inputs = self.find_elements(*self.inputNumber)
        # # 然后从中过滤出type为checkbox的元素，单击勾选
        # for i in inputs:
        #     if i.get_attribute("type") == "text":
        #         self.clear_text(*self.inputNumber)
        #         i.send_keys(shuliang)
        """通过ClassName来定位"""
        self.clear_text(*self.inputNumber)
        self.find_element(*self.inputNumber).send_keys(shuliang)

    def input_number1(self, shuliang, listNumber):
        self.find_elements(*self.inputNumber)[listNumber].click()
        self.find_elements(*self.inputNumber)[listNumber].send_keys(Keys.CONTROL, "a")
        self.find_elements(*self.inputNumber)[listNumber].send_keys(Keys.DELETE)
        self.find_elements(*self.inputNumber)[listNumber].clear()
        self.find_elements(*self.inputNumber)[listNumber].send_keys(shuliang)

    # 调用click对象，点击全选框
    def click_qxk(self):
        self.find_element(*self.qxk).click()

    # 调用click对象，点击指定商品删除
    def click_sc(self):
        self.find_element(*self.sc).click()

    # 调用click对象，点击移到收藏
    def click_ydsc(self):
        self.find_element(*self.ydsc).click()

    # 调用click对象，点击删除下架和无库存1，删除选中0
    def click_scxj(self, listNumber):
        self.find_elements(*self.scxj)[listNumber].click()

    # 检查是否存在删除选中商品和删除无库存商品
    shctskqd = (By.CLASS_NAME, "layui-layer-btn0")
    def is_scsp_exist(self):
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

    # 调用click对象，点击结算按钮
    def click_jiesuan(self):
        self.find_element(*self.jiesuan).click()

    # 调用click对象，点击为你推荐左滑
    def click_wntjzh(self):
        self.find_element(*self.wntjzh).click()

    # 调用click对象，点击为你推荐右滑
    def click_wntjyh(self):
        self.find_element(*self.wntjyh).click()

    # 调用click对象，点击为你推荐大图
    def click_wntjdt1(self):
        self.find_element(*self.wntjdt1).click()

