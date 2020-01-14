# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys


# 继承BasePage类
class JiFenShangChengPage(BasePage):
    """签到"""
    qd = (By.LINK_TEXT, "[签到]")
    def click_qd(self):
        self.find_element(*self.qd).click()

    """"签到成功/失败提示文本"""
    qdcgts = (By.CLASS_NAME, "layui-layer-content.layui-layer-padding")
    def text_qdcgts(self):
        return self.find_element(*self.qdcgts).text

    """礼品车去逛逛"""
    qgg = (By.LINK_TEXT, "去逛逛")
    def click_qgg(self):
        self.find_element(*self.qgg).click()
    def text_qgg(self):
        return self.find_element(*self.qgg).text

    """判断购物车是否有商品"""
    sc = (By.CLASS_NAME, "delete")  # 礼品列表删除
    tsk = (By.CLASS_NAME, "layui-layer-btn0")  # 提示框确定
    def is_element_exist(self):
        list = self.driver.find_elements(*self.gwclb)
        if len(list) == 0:
            # print('没有该元素')
            return 0
        elif len(list) >= 0:
            # print('共找到' + str(len(list)) + '个元素')
            self.find_element(*self.sc).click()
            sleep(1)
            self.find_element(*self.tsk).click()

    """判断购物车列表是否存在"""
    gwclb = (By.CLASS_NAME, "cart_list")
    def isElementPresent(self):
        """
        用来判断元素标签是否存在，
        """
        try:
            element = self.driver.find_element(*self.gwclb)
        # 原文是except NoSuchElementException, e:
        except NoSuchElementException as e:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True

    """数量增加"""
    sljia = (By.CLASS_NAME, "jia")  # 数量增加
    def click_sljia(self, sp):
        self.find_elements(*self.sljia)[sp].click()

    """数量减少"""
    sljian = (By.CLASS_NAME, "jian")  # 数量减
    def click_sljian(self, sp):
        self.find_elements(*self.sljian)[sp].click()

    """数量输入"""
    slInput = (By.CLASS_NAME, "input_val.goods_num")
    def input_number(self, shuliang, listNumber):
        self.find_elements(*self.slInput)[listNumber].click()
        self.find_elements(*self.slInput)[listNumber].send_keys(Keys.CONTROL, "a")
        self.find_elements(*self.slInput)[listNumber].send_keys(Keys.DELETE)
        self.find_elements(*self.slInput)[listNumber].clear()
        self.find_elements(*self.slInput)[listNumber].send_keys(shuliang)

    """单选"""
    dx = (By.CLASS_NAME, "danxuan")
    def click_dx(self, dxk):
        self.find_elements(*self.dx)[dxk].click()

    """全选"""
    qx = (By.CLASS_NAME, "quanxuan")
    def click_qx(self, qxk):
        self.find_elements(*self.qx)[qxk].click()

    """删除"""
    sc = (By.CLASS_NAME, "delete")
    def click_sc(self,sc):
        self.find_elements(*self.sc)[sc].click()

    """结算"""
    jiesuan = (By.ID, "jiesuan")
    def click_jiesuan(self):
        self.find_element(*self.jiesuan).click()

    """已签到/签到按钮"""
    qdButton = (By.ID, "qiandao")
    def click_qdButton(self):
        self.find_element(*self.qdButton).click()

    """积分订单"""
    jfdd = (By.LINK_TEXT, "[积分订单]")
    def click_jfdd(self):
        self.find_element(*self.jfdd).click()

    """去赚取积分"""
    qzqjf = (By.LINK_TEXT, "[去赚取积分]")
    def click_qzqjf(self):
        self.find_element(*self.qzqjf).click()

    """积分首页"""
    jfsy = (By.LINK_TEXT, "积分首页")
    def click_jfsy(self):
        self.find_element(*self.jfsy).click()

    """个人中心"""
    grzx = (By.LINK_TEXT, "个人中心")
    def click_grzx(self):
        self.find_element(*self.grzx).click()

    """返回药易购"""
    fhyyg = (By.LINK_TEXT, "返回药易购")
    def click_fhyyg(self):
        self.find_element(*self.fhyyg).click()


    """热门兑换商品加入购物车"""
    spjrgwc = (By.CLASS_NAME, "fr")
    def click_spjrgwc(self, splist):
        self.find_elements(*self.spjrgwc)[splist].click()

    """礼品车"""
    lpc = (By.CLASS_NAME, "lp_cart")
    def click_lpc(self):
        self.find_element(*self.lpc).click()

    """兑换成功提示"""
    dhcg = (By.CLASS_NAME, "success_title")
    def text_dhcg(self):
        return self.find_element(*self.dhcg).text

    """确认提交"""
    submit = (By.ID, "btn")
    def click_submit(self):
        self.find_element(*self.submit).click()

    """订单详情"""
    ddxq = (By.LINK_TEXT, "订单详情")
    def click_ddxq(self):
        self.find_element(*self.ddxq).click()

    """我的积分"""
    wdjf = (By.LINK_TEXT, "我的积分")
    def click_wdjf(self):
        self.find_element(*self.wdjf).click()

    """为你推荐"""
    wntj = (By.CLASS_NAME, "wntj-cp")
    def click_wntj(self,list):
        self.find_elements(*self.wntj)[list].click()

    """立即兑换"""
    dh = (By.CLASS_NAME, "dh")
    def click_dh(self):
        self.find_element(*self.dh).click()

    """加入礼品车"""
    jrlpc = (By.CLASS_NAME, "jr")
    def click_jr(self):
        self.find_element(*self.jrlpc).click()

