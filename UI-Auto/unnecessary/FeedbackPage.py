# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage


# 继承BasePage类
class FeedbackPage(BasePage):

    # 定位器，通过元素属性定位元素对象
    ad = (By.XPATH, "//*[@id='app']/div/div[1]/div/span/img")  # 点击关掉广告
    feedback = (By.XPATH, "//*[@id='fixed-right']/div[1]/div[7]/a/img")    # 进入反馈界面
    radio1 = (By.XPATH, "//*[@id='radio']/label[1]/input")  # 反馈类型：药品咨询
    radio2 = (By.XPATH, "//*[@id='radio']/label[2]/input")  # 反馈类型：首页意见建议
    radio3 = (By.XPATH, "//*[@id='radio']/label[3]/input")  # 反馈类型：服务投诉
    radio4 = (By.XPATH, "//*[@id='radio']/label[4]/input")  # 反馈类型：服务表扬
    radio5 = (By.XPATH, "//*[@id='radio']/label[5]/input")  # 反馈类型：问题报告
    phone = (By.ID, "celORmail")  # 手机/邮箱输入框
    content = (By.ID, "content")  # 内容输入框
    submit = (By.XPATH, "//*[@id='body']/div[2]/div[2]/div[2]/div/form/div[3]/div/input")  # 提交按钮
    errorMsg1 = (By.XPATH, "//*[@id='body']/div[2]/div[2]/div[2]/div/form/div[2]/p")  # 手机/邮箱填写错误提示
    errorMsg2 = (By.XPATH, "//*[@id='body']/div[2]/div[2]/div[2]/div/form/div[3]/div/p")  # 内容填写错误提示
    submitSuccess = (By.CLASS_NAME, "tip_text")  # 提交成功后的提示
    confirm = (By.XPATH, "//*[@id='shopping_box']/div/p[2]/a")  # 提交成功后的确认


    # Action
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 调用send_keys对象，输入手机/邮箱名
    def input_phone(self, phone):
        self.find_element(*self.phone).send_keys(phone)

    # 调用send_keys对象，输入内容
    def input_content(self, content):
        self.find_element(*self.content).send_keys(content)

    # 调用click对象，点击进入反馈界面
    def click_feedback(self):
        self.find_element(*self.feedback).click()

    # 调用click对象，点击phone输入框
    def click_phone(self):
        self.find_element(*self.phone).click()

    # 调用click对象，点击content输入框
    def click_content(self):
        self.find_element(*self.content).click()

    # 调用click对象，点击提交
    def click_submit(self):
        self.find_element(*self.submit).click()

    # 调用click，关掉广告
    def click_ad(self):
        self.find_element(*self.ad).click()


    # 调用click对象，选择反馈类型
    def click_radio1(self):
        self.find_element(*self.radio1).click()
    def click_radio2(self):
        self.find_element(*self.radio2).click()
    def click_radio3(self):
        self.find_element(*self.radio3).click()
    def click_radio4(self):
        self.find_element(*self.radio4).click()
    def click_radio5(self):
        self.find_element(*self.radio5).click()

    # 调用click对象，提交成功后确认
    def click_confirm(self):
        self.find_element(*self.confirm).click()

    # 用户名不合理是Tip框内容展示
    def show_errorMsg1(self):
        return self.find_element(*self.errorMsg1).text

    def show_errorMsg2(self):
        return self.find_element(*self.errorMsg2).text

    # 提交成功检查
    def is_submit_success(self):
        return self.find_element(*self.submitSuccess).text






