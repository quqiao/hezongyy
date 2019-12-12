# -*- coding: utf-8 -*-
__author__ = 'quqiao'
import unittest
import uiautomator2 as u2
from time import sleep


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb()
        # cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
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

    def test_login_01(self):
        """账号和密码为空时登录"""
        sleep(2)
        self.d(resourceId="com.hz.purchase:id/btn_login").click()  # 点击登录按钮
        assert "请输入登录名" in self.d.toast.get_message(5.0, default="")

    def test_login_02(self):
        """账号为空时登录"""
        self.d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        sleep(1)
        self.d(resourceId="com.hz.purchase:id/in_psd").send_keys("123456")  # 登录界面 --- 密码输入
        sleep(1)
        self.d.set_fastinput_ime(False)  # 关闭FastInputIME输入法
        sleep(1)
        self.d(resourceId="com.hz.purchase:id/btn_login").click()  # 点击登录按钮
        assert "请输入登录名" in self.d.toast.get_message(5.0, default="")

    def test_login_03(self):
        """密码为空时登录"""
        self.d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        sleep(1)
        # self.d(resourceId="com.hz.purchase:id/in_account").click()
        self.d(resourceId="com.hz.purchase:id/in_account").send_keys("屈桥123")  # 登录界面 --- 账号输入
        self.d.set_fastinput_ime(False)  # 关闭FastInputIME输入法
        sleep(1)
        self.d(resourceId="com.hz.purchase:id/btn_login").click()  # 点击登录按钮
        sleep(1)
        assert "请输入密码" in self.d.toast.get_message(5.0, default="")

    def test_login_04(self):
        """账号输入错误时登录"""
        self.d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        sleep(1)
        # self.d(resourceId="com.hz.purchase:id/in_account").click()
        self.d(resourceId="com.hz.purchase:id/in_account").send_keys("屈桥123111")  # 登录界面 --- 账号输入
        sleep(2)
        # self.d(resourceId="com.hz.purchase:id/in_psd").click()
        self.d(resourceId="com.hz.purchase:id/in_psd").send_keys("123456")  # 登录界面 --- 密码输入
        sleep(2)
        self.d.set_fastinput_ime(False)  # 关闭FastInputIME输入法
        sleep(2)
        self.d(resourceId="com.hz.purchase:id/btn_login").click()  # 点击登录按钮
        sleep(1)
        assert "用户名或密码错误" in self.d.toast.get_message(5.0, default="")

    def test_login_05(self):
        """密码输入错误时登录"""
        self.d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        sleep(1)
        # self.d(resourceId="com.hz.purchase:id/in_account").click()
        self.d(resourceId="com.hz.purchase:id/in_account").send_keys("屈桥123")  # 登录界面 --- 账号输入
        sleep(1)
        self.d(resourceId="com.hz.purchase:id/in_psd").send_keys("888888")  # 登录界面 --- 密码输入
        sleep(1)
        self.d.set_fastinput_ime(False)  # 关闭FastInputIME输入法
        sleep(1)
        self.d(resourceId="com.hz.purchase:id/btn_login").click()  # 点击登录按钮
        sleep(1)
        assert "用户名或密码错误" in self.d.toast.get_message(5.0, default="")

    def test_login_06(self):
        """正确用户名登录"""
        self.d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        sleep(1)
        self.d(resourceId="com.hz.purchase:id/in_account").send_keys("屈桥123")  # 登录界面 --- 账号输入
        sleep(1)
        self.d(resourceId="com.hz.purchase:id/in_psd").send_keys("123456")  # 登录界面 --- 密码输入
        sleep(1)
        self.d.set_fastinput_ime(False)  # 关闭FastInputIME输入法
        sleep(1)
        self.d(resourceId="com.hz.purchase:id/btn_login").click()  # 点击登录按钮
        sleep(3)
        self.d(text="我的").exists(timeout=5)

if __name__ == "__main__":
    unittest.main()
