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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
