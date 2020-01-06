# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.LoginPage import LoginPage
from selenium import webdriver
from time import sleep
from common.public import login_url, PublicMethod, username

class TestLogin(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(5)  # 隐式等待
        cls.url = login_url
        cls.username = username
        cls.password = "123456"
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵易购登录界面")  # 声明publicMethod类对象
        cls.login_page = LoginPage(cls.driver, cls.url, u"合纵易购登录界面")  # 声明LoginPage类对象
        cls.public_page.get_url(cls.url)  # 调用打开url

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_login_01(self):
        """不输入用户名和密码"""
        # 调用点击登录按钮组件
        self.login_page.click_submit()
        sleep(0.5)
        self.assertEqual(self.login_page.show_errorMsg1(), "请输入用户名或手机号")

    def test_login_02(self):
        """只输入用户名"""
        self.login_page.input_username(self.username)
        self.login_page.click_submit()
        sleep(0.5)
        self.assertEqual(self.login_page.show_errorMsg1(), "请输入用户名或手机号")

    def test_login_03(self):
        """只输入密码"""
        sleep(3)
        self.login_page.clear_text(*self.login_page.usernameloc)
        self.login_page.input_password(self.password)
        self.login_page.click_submit()
        sleep(0.5)
        self.assertEqual(self.login_page.show_errorMsg1(), "请输入用户名或手机号")

    def test_login_04(self):
        """输入错误密码"""
        self.login_page.input_username(self.username)
        self.login_page.clear_text(*self.login_page.passwordloc)
        self.login_page.input_password("xxxx")
        self.login_page.click_submit()
        sleep(0.5)
        self.assertEqual((self.login_page.show_errorMsg2()), "用户名或密码错误。")

    def test_login_05(self):
        """输入不存在的用户"""
        self.login_page.clear_text(*self.login_page.usernameloc)
        self.login_page.clear_text(*self.login_page.passwordloc)
        self.login_page.input_username("xxxx")
        self.login_page.input_password(self.password)
        self.login_page.click_submit()
        sleep(0.5)
        self.assertEqual(self.login_page.show_errorMsg2(), "用户名或密码错误。")

    def test_login_06(self):
        """输入正确的用户名密码"""
        self.login_page.clear_text(*self.login_page.usernameloc)
        self.login_page.clear_text(*self.login_page.passwordloc)
        self.login_page.input_username(self.username)
        # 调用密码输入组件
        self.login_page.input_password(self.password)
        # 调用点击登录按钮组件
        self.login_page.click_submit()
        self.assertEqual(self.login_page.is_login_success(), "[退出]")
