# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage


# 继承BasePage类
class FeedbackPage(BasePage):
    """反馈类型选择按钮"""
    radio = (By.ID, "type")
    def click_radio(self, radioList):
        self.find_elements(*self.radio)[radioList].click()

    """手机/邮箱输入框"""
    phone = (By.ID, "celORmail")
    def clear_phone(self):
        self.clear_text(*self.phone)
    def input_phone(self, phone):
        self.find_element(*self.phone).send_keys(phone)
    def click_phone(self):
        self.find_element(*self.phone).click()


    """内容输入框"""
    content = (By.ID, "content")
    def clear_content(self):
        self.clear_text(*self.content)
    def input_content(self, content):
        self.find_element(*self.content).send_keys(content)
    def click_content(self):
        self.find_element(*self.content).click()

    """提交按钮"""
    submit = (By.CLASS_NAME, "sub")  # 提交按钮
    def click_submit(self):
        self.find_element(*self.submit).click()

    """提交成功后的提示"""
    submitSuccess = (By.CLASS_NAME, "tip_text")
    def text_submit_success(self):
        return self.find_element(*self.submitSuccess).text

    """提交成功后的确认"""
    confirm = (By.CLASS_NAME, "login_a.confirm.again")
    def click_confirm(self):
        self.find_element(*self.confirm).click()

    """用户名不合理是Tip框内容展示"""
    errorMsg = (By.CLASS_NAME, "err")
    def text_errorMsg(self, errlist):
        return self.find_elements(*self.errorMsg)[errlist].text

    """用户反馈"""
    yhfk = (By.LINK_TEXT, "用户反馈")
    def text_yhfk(self):
        return self.find_element(*self.yhfk).text





