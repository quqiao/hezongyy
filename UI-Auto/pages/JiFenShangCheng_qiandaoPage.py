# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys


# 继承BasePage类

class JiFenShangCheng_qiandaoPage(BasePage):
    """已签到/签到按钮"""
    qdButton = (By.ID, "qiandao")
    def click_qdButton(self):
        self.find_element(*self.qdButton).click()

    def getValue_qdButton(self):
        return self.find_element(*self.qdButton).get_attribute("value")

    """"签到成功/失败提示文本"""
    qdcgts = (By.CLASS_NAME, "layui-layer-content.layui-layer-padding")
    def text_qdcgts(self):
        return self.find_element(*self.qdcgts).text
