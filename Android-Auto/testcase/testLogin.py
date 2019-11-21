# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.LoginPage import LoginPage
import uiautomator2 as u2
from time import sleep
# from common.public import host

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb()
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        # cls.u.disable_popups(True)  # 允许自动处理弹出框
        cls.u.make_toast("测试开始", 3)

    @classmethod
    def tearDownClass(cls):
        cls.u.make_toast("测试结束", 3)
        cls.u.app_stop_all()
        cls.u.service("uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行

    def setUp(self):
        self.d = self.u.session("com.hz.purchase")  # 启动药易购APP
        sleep(5)  # 等待首页广告结束

    def tearDown(self):
        pass

    def test_1_login(self):
        """登录用例"""
        self.d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        sleep(1)
        self.d(resourceId="com.hz.purchase:id/in_account").click()
        self.d(resourceId="com.hz.purchase:id/in_account").send_keys("屈桥123")  # 登录界面 --- 账号输入
        sleep(2)
        self.d(resourceId="com.hz.purchase:id/in_psd").click()
        self.d(resourceId="com.hz.purchase:id/in_psd").send_keys("123456")  # 登录界面 --- 密码输入
        sleep(2)
        self.d.set_fastinput_ime(False)  # 关闭FastInputIME输入法
        sleep(2)
        self.d(resourceId="com.hz.purchase:id/btn_login").click()  # 点击登录按钮
        sleep(2)
        self.d(text="我的").exists(timeout=5)

if __name__ == "__main__":
    unittest.main()
