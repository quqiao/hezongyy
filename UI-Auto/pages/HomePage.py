# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class HomePage(BasePage):
    # 定位器，通过元素属性定位元素对象
    ad = (By.XPATH, "//*[@id='app']/div/div[1]/div/span/img")  # 点击关掉广告
    mzjxTitle = (By.XPATH, "//*[@id='mzjx']/div/div[1]/span[1]")  # 每周精选标题
    WeekContent = (By.XPATH, "//*[@id='mzjx']/div/div[2]/div[1]")  # 每周精选大图1
    CheckWeek = (By.XPATH, "//*[@id='jrgwc']")  # 检查每周精选
    zyzq = (By.XPATH, "//*[@id='app']/div/div[6]/div/ul/li[1]/a/img")  # 中药专区入口
    zyzq_check = (By.XPATH, "//*[@id='body']/div[4]/div[2]/ul/li[1]/a")  # 检查中药专区
    yxzq = (By.XPATH, "//*[@id='app']/div/div[6]/div/ul/li[2]/a/img")  # 院线专区入口
    Vipzq = (By.XPATH, "//*[@id='app']/div/div[6]/div/ul/li[3]/a/img")  # VIP专区入口
    cxzq = (By.XPATH, "//*[@id='app']/div/div[6]/div/ul/li[4]/a/img")  # 促销专区入口
    bjpzq = (By.XPATH, "//*[@id='app']/div/div[6]/div/ul/li[5]/a/img")  # 保健品专区入口
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
    wntjzh = (By.XPATH, "//*[@id='wntj-carousel']/ul[3]/li[1]/i")  # 为你推荐左滑
    wntjyh = (By.XPATH, "//*[@id='wntj-carousel']/ul[3]/li[2]/i")  # 为你推荐右滑
    wntjdt1 = (By.XPATH, "//*[@id='wntj-carousel']/ul[1]/li[2]/div/a[1]/div")  # 为你推荐大图1


    # Action
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 调用click，关掉广告
    def click_ad(self):
        self.find_element(*self.ad).click()

    # 调用click对象，点击每周精选
    def click_week(self):
        self.find_element(*self.WeekContent).click()

    # 调用scroll对象，滚动出现每周精选
    def scroll_mzjx(self):
        target = self.driver.find_element(*self.mzjxTitle)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 调用text文本，检查每周精选
    def check_week(self):
        return self.find_element(*self.CheckWeek).text

    # 调用click对象，点击中药专区
    def script_zyzq(self):
        # self.find_element(*self.zyzq).click()
        zyzq = self.find_element(*self.zyzq)
        self.script2("arguments[0].click();", zyzq)

    # 调用text文本，检查中药专区
    def check_zyzq(self):
        return self.find_element(*self.zyzq_check).text

    # 调用click对象，点击院线专区
    def script_yxzq(self):
        yxzq = self.find_element(*self.yxzq)
        self.script2("arguments[0].click();", yxzq)

    # 调用click对象，点击VIP专区
    def click_vip(self):
        self.find_element(*self.Vipzq).click()

    # 调用click对象，点击促销专区
    def click_cxzq(self):
        self.find_element(*self.cxzq).click()

    # 调用click对象，点击保健品专区
    def click_bjpzq(self):
        self.find_element(*self.bjpzq).click()

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

    # 调用windows_handles进行切换页面后的重定位
    def locate(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])



















