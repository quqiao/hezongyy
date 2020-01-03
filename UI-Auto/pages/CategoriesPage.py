# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep


# 继承BasePage类
class CategoriesPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    # py = (By.XPATH, "//*[@id='app']/div/div[1]/div[3]/div/ul/li[2]/ul/li[2]/a,,,,//*[@id="app"]/div/div[3]/div[3]/div/ul/li[2]/ul/li[2]/a")  # 商品列表中的普药
    py = (By.LINK_TEXT, "普药")  # 商品列表普药
    zszq = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.nav > ul > li:nth-child(3) > a")  # 商品列表中的诊所专区
    qx = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.nav > ul > li:nth-child(4) > a")  # 商品列表中的器械
    zyzq = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.nav > ul > li:nth-child(5) > a")  # 商品列表中的中药专区
    ppzq = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.nav > ul > li:nth-child(6) > a")  # 商品列表中的品牌专区
    cxzq = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.nav > ul > li:nth-child(7) > a")  # 商品列表中的促销专区
    jpzq = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.nav > ul > li:nth-child(8) > a")  # 商品列表中的精品专区
    jfsc = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.nav > ul > li:nth-child(9) > a")  # 商品列表中的积分商城

    list1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(1) > div.text > div.menu_title")  # 呼吸系统用药列表
    list1_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(1) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 抗感冒类

    list2 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(2) > div.text > div.menu_title")  # 清热消炎列表
    list2_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(2) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 青霉素及头孢

    list3 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(3) > div.text > div.menu_title")  # 五官皮肤及外用列表
    list3_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(3) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 眼科类

    list4 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(4) > div.text > div.menu_title")  # 消化肝胆系统列表
    list4_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(4) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 解痉阵痛类

    list5 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(5) > div.text > div.menu_title")  # 补益安神及维矿类列表
    list5_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(5) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 调节免疫力类

    list6 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(6) > div.text > div.menu_title")  #  妇，儿科列表
    list6_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(6) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 避孕类

    list7 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(7) > div.text > div.menu_title")  # 心脑血管及神经类用药列表
    list7_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(7) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 促白细胞增生类

    list8 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(8) > div.text > div.menu_title")  # 内分泌系统列表
    list8_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(8) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 甾体激素类

    list9 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(9) > div.text > div.menu_title")  # 风湿骨伤及其他药品列表
    list9_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(9) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 抗风湿类

    list10 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(10) > div.text > div.menu_title")  # 特殊复方制剂，生物制品列表
    list10_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(10) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 血液制品

    list11 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(11) > div.text > div.menu_title")  # 中药饮片列表
    list11_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(11) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 配方中药饮片

    list12 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(12) > div.text > div.menu_title")  # 非药品列表
    list12_1 = (By.CSS_SELECTOR, "#app > div > div.header-box > div.classify-nav > div > ul > li.all.all-hover > div.site_content > div > div:nth-child(12) > div.category_list > div:nth-child(2) > div > a:nth-child(1)")  # 功能性贴膏



    # # Action
    # def open(self):
    #     # 调用page中的_open打开连接
    #     self._open(self.base_url, self.pagetitle)
    #
    # # 调用click，关掉广告
    # def click_ad(self):
    #     self.find_element(*self.ad).click()

    # 调用click,点击进入普药列表
    def click_py(self):
        self.find_element2(*self.py).click()

    # 调用click,点击诊所专区列表
    def click_zszq(self):
        self.find_element(*self.zszq).click()

    # 调用click,点击器械列表
    def click_qx(self):
        self.find_element(*self.qx).click()

    # 调用click，点击中药专区列表
    def click_zyzq(self):
        self.find_element(*self.zyzq).click()

    # 调用click，点击品牌专区列表
    def click_ppzq(self):
        self.find_element(*self.ppzq).click()

    # 调用click，点击促销专区列表
    def click_cxzq(self):
        self.find_element(*self.cxzq).click()

    # 调用click,点击精品专区列表
    def click_jpzq(self):
        self.find_element(*self.jpzq).click()

    # 调用click,点击积分商城列表
    def click_jfsc(self):
        self.find_element(*self.jfsc).click()

    # 调用click对象，点击呼吸系统用药列表
    def click_list1(self):
        self.find_element(*self.list1).click()

    # 调用click,点击抗感冒类
    def click_list1_1(self):
        self.find_element(*self.list1_1).click()

    # 调用text文本，检查列表显示
    def check_list1(self):
        return self.find_element(*self.CheckList1).text

    # 调用click对象，点击清热消炎列表
    def click_list2(self):
        self.find_element(*self.list2).click()

    # 调用text文本，检查清热消炎列表显示
    def check_list2(self):
        return self.find_element(*self.CheckList2).text

    # 调用click,点击青霉素及头孢类
    def click_list2_1(self):
        self.find_element(*self.list2_1).click()

    # 调用click,点击五官皮肤及外用列表
    def click_list3(self):
        self.find_element(*self.list3).click()

    # 调用click,眼科类
    def click_list3_1(self):
        self.find_element(*self.list3_1).click()

    # 调用click,消化肝胆系统列表
    def click_list4(self):
        self.find_element(*self.list4).click()

    # 调用click,解痉阵痛类
    def click_list4_1(self):
        self.find_element(*self.list4_1).click()

    # 调用click,补益安神及维矿类列表
    def click_list5(self):
        self.find_element(*self.list5).click()

    # 调用click,调节免疫力类
    def click_list5_1(self):
        self.find_element(*self.list5_1).click()

    # 调用click,妇，儿科列表
    def click_list6(self):
        self.find_element(*self.list6).click()

    # 调用click,避孕类
    def click_list6_1(self):
        self.find_element(*self.list6_1).click()

    # 调用click,心脑血管及神经类用药列表
    def click_list7(self):
        self.find_element(*self.list7).click()

    # 调用click,促白细胞增生类
    def click_list7_1(self):
        self.find_element(*self.list7_1).click()

    # 调用click,内分泌系统列表
    def click_list8(self):
        self.find_element(*self.list8).click()

    # 调用click,甾体激素类
    def click_list8_1(self):
        self.find_element(*self.list8_1).click()

    # 调用click,风湿骨伤及其他药品列表
    def click_list9(self):
        self.find_element(*self.list9).click()

    # 调用click,抗风湿类
    def click_list9_1(self):
        self.find_element(*self.list9_1).click()

    # 调用click,特殊复方制剂，生物制品列表
    def click_list10(self):
        self.find_element(*self.list10).click()

    # 调用click,血液制品
    def click_list10_1(self):
        self.find_element(*self.list10_1).click()

    # 调用click,中药饮片列表
    def click_list11(self):
        self.find_element(*self.list11).click()

    # 调用click,配方中药饮片
    def click_list11_1(self):
        self.find_element(*self.list11_1).click()

    # 调用click,非药品列表
    def click_list12(self):
        self.find_element(*self.list12).click()

    # 调用click,功能性贴膏
    def click_list12_1(self):
        self.find_element(*self.list12_1).click()



