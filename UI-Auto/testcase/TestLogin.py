# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.LoginPage import LoginPage
from selenium import webdriver
from time import sleep
from common.public import host

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(30)
        cls.url = host + "/auth/login"
        cls.username = "测试24"
        cls.password = "123456"

        # 声明LoginPage类对象
        cls.login_page = LoginPage(cls.driver, cls.url, u"合纵易购登录界面")
        cls.login_page.open()

    #不输入用户名和密码
    def test_1_login_noUserAndPwd(self):
        # 调用点击登录按钮组件
        self.login_page.click_submit()
        sleep(0.5)
        self.assertEqual(self.login_page.show_errorMsg1(), "请输入用户名或手机号")

    #只输入用户名
    def test_2_login_noPwd(self):
        self.login_page.input_username(self.username)
        self.login_page.click_submit()
        sleep(0.5)
        self.assertEqual(self.login_page.show_errorMsg1(), "请输入用户名或手机号")

    #只输入密码
    def test_3_login_noUser(self):
        sleep(3)
        self.login_page.clear_text(self.login_page.usernameloc)
        self.login_page.input_password(self.password)
        self.login_page.click_submit()
        sleep(0.5)
        self.assertEqual(self.login_page.show_errorMsg1(), "请输入用户名或手机号")

    #输入错误密码
    def test_4_login_errorPwd(self):
        self.login_page.input_username(self.username)
        self.login_page.clear_text(self.login_page.passwordloc)
        self.login_page.input_password("xxxx")
        self.login_page.click_submit()
        sleep(0.5)
        self.assertEqual((self.login_page.show_errorMsg2()), "用户名或密码错误。")

     #输入不存在的用户
    def test_5_login_errorPwd(self):
        self.login_page.clear_text(self.login_page.usernameloc)
        self.login_page.clear_text(self.login_page.passwordloc)
        self.login_page.input_username("xxxx")
        self.login_page.input_password(self.password)
        self.login_page.click_submit()
        sleep(0.5)
        self.assertEqual(self.login_page.show_errorMsg2(), "用户名或密码错误。")

    # 输入正确的用户名密码
    def test_6_login_success(self):
        self.login_page.clear_text(self.login_page.usernameloc)
        self.login_page.clear_text(self.login_page.passwordloc)
        self.login_page.input_username(self.username)
        # 调用密码输入组件
        self.login_page.input_password(self.password)
        # 调用点击登录按钮组件
        self.login_page.click_submit()
        self.assertEqual(self.login_page.is_login_success(), "[退出]")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
