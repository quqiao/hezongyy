# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage


# 继承BasePage类
class MyPage(BasePage):
    wddd = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[1]/li[1]/a")  # 我的订单
    jfdd = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[1]/li[2]/a")  # 积分订单
    yegl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[2]/li[1]/a")  # 余额管理
    yhqgl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[2]/li[2]/a")  # 优惠券管理
    jfgl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[2]/li[3]/a")   # 积分管理
    jfjbgl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[2]/li[4]/a")  # 积分金币管理
    jbxx = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[1]/a")  # 基本信息
    yqtzc = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[2]/a")  # 银企通注册
    wxbd = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[3]/a")  # 微信绑定
    wdsc = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[4]/a")  # 我的收藏
    zncg = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[5]/a")  # 智能采购
    dhygl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[6]/a")  # 多会员管理
    wdxx = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[7]/a")  # 我的消息
    wdqg = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[8]/a")  # 我的求购
    wdfk = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[9]/a")  # 我的反馈
    shdz = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[10]/a")  # 收货地址
    pswl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[11]/a")  # 配送物流

    # 定义点击我的订单
    def click_wddd(self):
        self.find_element(*self.wddd).click()

    # 定义点击积分订单
    def click_jfdd(self):
        self.find_element(*self.jfdd).click()

    # 定义点击余额管理
    def click_yegl(self):
        self.find_element(*self.yegl).click()

    # 定义点击优惠券管理
    def click_yhqgl(self):
        self.find_element(*self.yhqgl).click()

    # 定义点击积分管理
    def click_jfgl(self):
        self.find_element(*self.jfgl).click()

    # 定义点击积分金币管理
    def click_jfjbgl(self):
        self.find_element(*self.jfjbgl).click()

    # 定义点击基本信息
    def click_jbxx(self):
        self.find_element(*self.jbxx).click()

    # 定义点击银企通注册
    def click_yqtzc(self):
        self.find_element(*self.yqtzc).click()

    # 定义点击微信绑定
    def click_wxbd(self):
        self.find_element(*self.wxbd).click()

    # 定义点击我的收藏
    def click_wdsc(self):
        self.find_element(*self.wdsc).click()

    # 定义点击智能采购
    def click_zncg(self):
        self.find_element(*self.zncg).click()

    # 定义点击多会员管理
    def click_dhygl(self):
        self.find_element(*self.dhygl).click()

    # 定义点击我的消息
    def click_wdxx(self):
        self.find_element(*self.wdxx).click()

    # 定义点击我的求购
    def click_wdqg(self):
        self.find_element(*self.wdqg).click()

    # 定义点击我的反馈
    def click_wdfk(self):
        self.find_element(*self.wdfk).click()

    # 定义点击收货地址
    def click_shdz(self):
        self.find_element(*self.shdz).click()

    # 定义点击配送物流
    def click_pswl(self):
        self.find_element(*self.pswl).click()













