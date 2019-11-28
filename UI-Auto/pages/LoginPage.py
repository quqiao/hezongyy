# -*- coding: utf-8 -*-
__author__ = 'quqiao'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage


# 继承BasePage类
class LoginPage(BasePage):

    # 定位器，通过元素属性定位元素对象
    usernameloc = (By.XPATH, "//*[@id='username']")  # 登录界面用户名输入框
    passwordloc = (By.XPATH, "//*[@id='password']")  # 登录界面密码输入框
    submit = (By.XPATH, "//*[@id='right_1']/a")  # 登录界面提交按钮
    errorMsg1 = (By.CLASS_NAME, "prompt2")  # 用户名错误出现的提示
    errorMsg2 = (By.XPATH, "//*[@id='right_1']/p[2]/span[2]")  # 密码错误出现的提示
    loginuser = (By.XPATH, "//*[@id='app']/div/div[1]/div[1]/div/ul[1]/li[4]/a")  # 登录成功提示


    # Action
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 调用send_keys对象，输入用户名
    def input_username(self, username):
        self.find_element(*self.usernameloc).send_keys(username)

    # 调用send_keys对象，输入密码
    def input_password(self, password):
        self.find_element(*self.passwordloc).send_keys(password)

    # 调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element(*self.submit).click()

    # 用户名不合理是Tip框内容展示
    def show_errorMsg1(self):
        return self.find_element(*self.errorMsg1).text

    def show_errorMsg2(self):
        return self.find_element(*self.errorMsg2).text

    # 登录成功检查
    def is_login_success(self):
        return self.find_element(*self.loginuser).text






