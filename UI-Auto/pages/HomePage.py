# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class HomePage(BasePage):
    """退出按钮"""
    tc = (By.LINK_TEXT, "[退出]")
    def text_tc(self):
        return self.find_element(*self.tc).text

    """订单查询"""
    ddcx = (By.CLASS_NAME, "dd")
    def click_ddcx(self):
        self.find_element(*self.ddcx).click()

    """我的药易购"""
    my = (By.XPATH, "//*[@id='carousel']/div/div/div[1]/div[2]/span/a")
    def click_my(self):
        self.find_element(*self.my).click()

    """购物车按钮"""
    gwc = (By.CLASS_NAME, "gwc")
    def click_gwc(self):
        button = self.find_element(*self.gwc)
        self.script2("arguments[0].click();", button)

    """专区列表，中药,院线,VIP,促销,保健品专区"""
    zqlist = (By.CLASS_NAME, "zq-list")
    zqtag = (By.TAG_NAME, "li")
    def click_zqlist(self, list):
        li = self.find_element(*self.zqlist)
        li.find_elements(*self.zqtag)[list].click()

    mzjxTitle = (By.XPATH, "//*[@id='mzjx']/div/div[1]/span[1]")  # 每周精选标题
    WeekContent = (By.XPATH, "//*[@id='mzjx']/div/div[1]/a/i")  # 每周精选查看更多
    ppzqtitle = (By.XPATH, "//*[@id='ppzq']/div/div[1]/span")  # 品牌专区标题
    ppzqhyh = (By.XPATH, "//*[@id='ppzq']/div/div[2]/ul/li[12]/img")  # 品牌专区换一换
    ppzqckqb = (By.XPATH, "//*[@id='ppzq']/div/div[1]/a/i")  # 品牌专区查看全部
    xpsjtitle = (By.XPATH, "//*[@id='xpsj']/div/div[1]/div[1]/span")  # 新品上架标题
    xpsjdt = (By.XPATH, "//*[@id='xpsj-carousel']/ul[1]/li[1]/a")  # 新品上架大图
    cptjdt = (By.XPATH, "//*[@id='cptj-carousel']/ul[1]/li/a")  # 产品推荐大图
    djrxtitle = (By.XPATH, "//*[@id='djrx']/div[1]/span")  # 当季热销标题
    djrxdt = (By.XPATH, "//*[@id='djrx']/div[2]/div[1]/ul[1]/li/a")  # 当季热销大图
    jtbjdt = (By.XPATH, "//*[@id='jtbj']/div[2]/div[1]/ul[1]/li/a")  # 家庭保健大图
    zyyptitle = (By.XPATH, "//*[@id='zyyp']/div[1]/span")  # 中药饮片标题
    zyypdt = (By.XPATH, "//*[@id='zyyp']/div[2]/div[1]/ul[1]/li/a/img")  # 中药饮片大图
    zstgdt = (By.XPATH, "//*[@id='zstg']/div[2]/div[1]/ul[1]/li/a/img")  # 诊所特供大图
    wntjtitle = (By.XPATH, "//*[@id='wntj-carousel']/div/span")  # 为你推荐标题
    wntjzh = (By.CLASS_NAME, "myicon1.lb_left_icon")  # 为你推荐左滑
    wntjyh = (By.CLASS_NAME, "myicon1.lb_right_icon")  # 为你推荐右滑
    wntjdt1 = (By.CSS_SELECTOR, "#wntj-carousel > ul.carousel-list > li.cur > div > a:nth-child(1) > div > div")  # 为你推荐大图

    "搜索出商品，将商品加入购物车"
    jrgwc_dt = (By.CLASS_NAME, "datu-jrgwc")  #
    def click_jrgwc_dt(self, sp):
        self.find_elements(*self.jrgwc_dt)[sp].click()

    "我的收藏按钮"
    wdsc = (By.LINK_TEXT, "我的收藏")
    "调用click,点击我的收藏按钮"
    def click_wdsc(self):
        self.find_element(*self.wdsc).click()


    # 调用click对象，点击每周精选
    def click_week(self):
        self.find_element(*self.WeekContent).click()

    # 调用scroll对象，滚动出现每周精选
    def scroll_mzjx(self):
        target = self.driver.find_element(*self.mzjxTitle)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 调用execute_script对象，滚动到品牌专区
    def scroll_ppzq(self):
        target = self.driver.find_element(*self.ppzqtitle)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 调用click对象，点击品牌专区换一换
    def click_ppzqhyh(self):
        self.find_element(*self.ppzqhyh).click()

    # 调用click对象，点击品牌专区查看全部
    def click_ppzqckqb(self):
        self.find_element(*self.ppzqckqb).click()

    # 调用execute_script对象，滚动到新品上架
    def scroll_xpsj(self):
        target = self.driver.find_element(*self.xpsjtitle)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 调用click对象，点击新品上架大图
    def click_xpsjdt(self):
        self.find_element(*self.xpsjdt).click()

    # 调用click对象，点击产品推荐大图
    def click_cptjdt(self):
        self.find_element(*self.cptjdt).click()

    # 调用execute_script对象，滚动到当季热销
    def scroll_djrx(self):
        target = self.driver.find_element(*self.djrxtitle)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 调用click对象，点击当季热销大图
    def click_djrxdt(self):
        self.find_element(*self.djrxdt).click()

    # 调用click对象，点击家庭保健大图
    def click_jtbjdt(self):
        self.find_element(*self.jtbjdt).click()

    # 调用execute_script对象，滚动到中药饮片
    def scroll_zyyp(self):
        target = self.driver.find_element(*self.zyyptitle)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 调用click对象，点击中药饮片大图
    def click_zyypdt(self):
        self.find_element(*self.zyypdt).click()

    # 调用click对象，点击诊所特供大图
    def click_zstgdt(self):
        self.find_element(*self.zstgdt).click()

    def scroll_wntjtitle(self):
        target = self.driver.find_element(*self.wntjtitle)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def click_wntjzh(self):
        self.find_element(*self.wntjzh).click()

    def click_wntjyh(self):
        self.find_element(*self.wntjyh).click()

    def click_wntjdt1(self):
        self.find_element(*self.wntjdt1).click()






