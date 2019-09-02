# -*- coding: utf-8 -*-
__author__ = 'liuquan'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage


# 继承BasePage类
class LoginPage(BasePage):

    # 定位器，通过元素属性定位元素对象
    usernameloc = (By.XPATH, "//input[@placeholder='请输入用户名']")
    passwordloc = (By.XPATH, "//input[@placeholder='请输入密码']")
    submit = (By.XPATH, "//button/span")
    errorMsg = (By.CLASS_NAME,"login-error")
    loginuser = (By.CLASS_NAME,"el-dropdown-link")


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

    # 用户名或密码不合理是Tip框内容展示
    def show_errorMsg(self):
        return self.find_element(*self.errorMsg).text

    # 登录成功检查
    def is_login_success(self):
        return self.find_element(*self.loginuser).text






