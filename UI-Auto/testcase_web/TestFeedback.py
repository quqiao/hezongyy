# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.FeedbackPage import FeedbackPage
from pages.HomePage import HomePage
from pages.MyPage import MyPage
from selenium import webdriver
from time import sleep
from common.public import home_url, PublicMethod, username

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(30)
        cls.url = home_url
        cls.username = username
        cls.password = "123456"
        # 声明LoginPage类对象
        cls.feedback_page = FeedbackPage(cls.driver, cls.url, u"合纵易购反馈界面")
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵易购反馈界面")
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购反馈界面")
        cls.my_page = MyPage(cls.driver, cls.url, u"合纵易购反馈界面")
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_feedback_01(self):
        """进入用户反馈界面"""
        self.home_page.click_my()  # 进入我的药易购
        sleep(1)
        self.my_page.click_wdfk()  # 进入我的反馈
        sleep(1)
        self.my_page.click_wyfk()  # 进入我要反馈
        sleep(1)
        self.assertEqual(self.feedback_page.text_yhfk(), "用户反馈", msg="没有进入用户反馈界面")

    def test_feedback_02(self):
        """只输入手机号"""
        sleep(1)
        self.feedback_page.input_phone("15888556699")  # 输入电话号码
        sleep(1)
        self.feedback_page.click_content()  # 点击输入内容
        sleep(1)
        self.feedback_page.click_submit()
        sleep(1)
        self.assertEqual(self.feedback_page.text_errorMsg(0), "请至少填写10字以上", msg="内容不为空")

    def test_feedback_03(self):
        """只输入内容"""
        sleep(1)
        self.feedback_page.clear_phone()  # 清除phone中的内容
        sleep(1)
        self.feedback_page.input_content("aaaaaaaaaaasssssssssssss")  # 输入内容
        sleep(1)
        self.feedback_page.click_submit()  # 点击提交
        sleep(1)
        self.assertEqual(self.feedback_page.text_errorMsg(0), "电话话/邮箱至少填写一项", msg="手机号不为空")

    def test_feedback_04(self):
        """手机号不满11位"""
        sleep(1)
        self.feedback_page.clear_content()  # 清除content中的内容
        sleep(1)


    # 只输入手机号
    def test_2_login_noPwd(self):
        self.feedback_page.input_phone(self.phone)
        self.feedback_page.click_content()
        self.feedback_page.click_submit()
        sleep(0.5)
        self.assertEqual(self.feedback_page.show_errorMsg2(), "请至少填写10字以上,,,,,电话话/邮箱至少填写一项")


