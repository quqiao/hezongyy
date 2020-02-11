# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys


# 继承BasePage类
class JiFenShangCheng_ddxqPage(BasePage):
    """订单详情"""
    ddxq1 = (By.CLASS_NAME, "vip_right_title")
    ddxq2 = (By.TAG_NAME, "span")
    def text_ddxq(self):
        return self.find_element(*self.ddxq1).find_element(*self.ddxq2).text