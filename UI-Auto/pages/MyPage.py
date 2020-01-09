# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage


# 继承BasePage类
class MyPage(BasePage):
    wddd = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[1]/li[1]/a")  # 我的订单
    wdddbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div[1]/div/span")  # 我的订单标题
    jfdd = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[1]/li[2]/a")  # 积分订单
    jfddbt = (By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/span")  # 积分订单标题
    yegl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[2]/li[1]/a")  # 余额管理
    yeglbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div[1]/span")  # 余额管理标题
    yhqgl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[2]/li[2]/a")  # 优惠券管理
    yhqglbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div/span")  # 优惠券管理标题
    jfgl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[2]/li[3]/a")   # 积分管理
    jfglbt = (By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/span")  # 积分管理标题
    jfjbgl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[2]/li[4]/a")  # 积分金币管理
    jfjbglbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div[1]/div/span")  # 积分金币管理标题
    jbxx = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[1]/a")  # 基本信息
    jbxxbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div[1]/span")  # 基本信息标题
    yqtzc = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[2]/a")  # 银企通注册
    yqtzcbt = (By.XPATH, "//*[@id='user_center']/div[1]/div[3]/div[1]/span")  # 银企通注册标题
    wxbd = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[3]/a")  # 微信绑定
    wxbdbt = (By.XPATH, "//*[@id='user_center']/div[1]/div[3]/div[1]/span")  # 微信绑定标题
    wdsc = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[4]/a")  # 我的收藏
    wdscbt = (By.XPATH, "//*[@id='sc1']/div[1]/span")  # 我的收藏标题
    zncg = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[5]/a")  # 智能采购
    zncgbt = (By.XPATH, "//*[@id='sc1']/div[1]/span")  # 智能采购标题
    dhygl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[6]/a")  # 多会员管理
    dhyglbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div[1]/span")  # 多会员管理标题
    wdxx = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[7]/a")  # 我的消息
    wdxxbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div[1]/span")  # 我的消息标题
    wdqg = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[8]/a")  # 我的求购
    wdqgbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div[1]/span")  # 我的求购标题
    wdfk = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[9]/a")  # 我的反馈
    wdfkbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div[1]/span")  # 我的反馈标题
    shdz = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[10]/a")  # 收货地址
    shdzbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div[1]/span")  # 收货地址标题
    pswl = (By.XPATH, "//*[@id='user_center']/div/div[2]/ul[3]/li[11]/a")  # 配送物流
    pswlbt = (By.XPATH, "//*[@id='user_center']/div/div[3]/div[1]/span")  # 配送物流标题

    """我要反馈"""
    wyfk = (By.CLASS_NAME, "add_liuyan")
    def click_wyfk(self):
        self.find_element(*self.wyfk).click()

    # 定义点击我的订单
    def click_wddd(self):
        self.find_element(*self.wddd).click()

    def text_wdddbt(self):
        return self.find_element(*self.wdddbt).text

    # 定义点击积分订单
    def click_jfdd(self):
        self.find_element(*self.jfdd).click()

    def text_jfddbt(self):
        return self.find_element(*self.jfddbt).text

    # 定义点击余额管理
    def click_yegl(self):
        self.find_element(*self.yegl).click()

    def text_yeglbt(self):
        return self.find_element(*self.yeglbt).text

    # 定义点击优惠券管理
    def click_yhqgl(self):
        self.find_element(*self.yhqgl).click()

    def text_yhqglbt(self):
        return self.find_element(*self.yhqglbt).text

    # 定义点击积分管理
    def click_jfgl(self):
        self.find_element(*self.jfgl).click()

    def text_jfglbt(self):
        return self.find_element(*self.jfglbt).text

    # 定义点击积分金币管理
    def click_jfjbgl(self):
        self.find_element(*self.jfjbgl).click()

    def text_jfjbglbt(self):
        return self.find_element(*self.jfjbglbt).text

    # 定义点击基本信息
    def click_jbxx(self):
        self.find_element(*self.jbxx).click()

    def text_jbxxbt(self):
        return self.find_element(*self.jbxxbt).text

    # 定义点击银企通注册
    def click_yqtzc(self):
        self.find_element(*self.yqtzc).click()

    def text_yqtzcbt(self):
        return self.find_element(*self.yqtzc).text

    # 定义点击微信绑定
    def click_wxbd(self):
        self.find_element(*self.wxbd).click()

    def text_wxbdbt(self):
        return self.find_element(*self.wxbdbt).text

    # 定义点击我的收藏
    def click_wdsc(self):
        self.find_element(*self.wdsc).click()

    def text_wdscbt(self):
        return self.find_element(*self.wdscbt).text

    # 定义点击智能采购
    def click_zncg(self):
        self.find_element(*self.zncg).click()

    def text_zncgbt(self):
        return self.find_element(*self.zncgbt).text

    # 定义点击多会员管理
    def click_dhygl(self):
        self.find_element(*self.dhygl).click()

    def text_dhyglbt(self):
        return self.find_element(*self.dhyglbt).text

    # 定义点击我的消息
    def click_wdxx(self):
        self.find_element(*self.wdxx).click()

    def text_wdxxbt(self):
        return self.find_element(*self.wdxxbt).text

    # 定义点击我的求购
    def click_wdqg(self):
        self.find_element(*self.wdqg).click()

    def text_wdqgbt(self):
        return self.find_element(*self.wdqgbt).text

    # 定义点击我的反馈
    def click_wdfk(self):
        self.find_element(*self.wdfk).click()

    def text_wdfkbt(self):
        return self.find_element(*self.wdfkbt).text

    # 定义点击收货地址
    def click_shdz(self):
        self.find_element(*self.shdz).click()

    def text_shdzbt(self):
        return self.find_element(*self.shdzbt).text

    # 定义点击配送物流
    def click_pswl(self):
        self.find_element(*self.pswl).click()

    def text_pswlbt(self):
        return self.find_element(*self.pswlbt).text












