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

    def test_search_01(self):
        """首页输入框输入药名直接搜索"""
        sleep(2)
        self.d(resourceId="com.hz.purchase:id/ll_btn_search").click()  # 点击首页搜索框
        self.d(resourceId="com.hz.purchase:id/et_key").send_keys("阿莫西林")  # 输入药名
        self.d(resourceId="com.hz.purchase:id/tv_btn_search").click()  # 点击搜索按钮
        self.d(text="阿莫西林").exists(timeout=3)

    def test_search_02(self):
        """首页输入框选择模糊匹配出的内容"""
        sleep(2)
        self.d(resourceId="com.hz.purchase:id/ll_btn_search").click()  # 点击首页搜索框
        self.d(resourceId="com.hz.purchase:id/et_key").send_keys("阿莫西林")  # 输入药名
        self.d(index=0, className="android.widget.LinearLayout").click()  # 点击模糊搜索出的第一个商品
        self.d(text="阿莫西林").exists(timeout=5)



    def test_search_03(self):
        """首页输入框输入厂家"""
        sleep(2)
        self.d(resourceId="com.hz.purchase:id/ll_btn_search").click()  # 点击首页搜索框
        self.d(resourceId="com.hz.purchase:id/et_key").send_keys("科伦药业")  # 输入药名
        self.d(resourceId="com.hz.purchase:id/tv_btn_search").click()  # 点击搜索按钮
        self.d(text="科伦药业").exists(timeout=5)

    def test_search_04(self):
        """首页输入框输入厂家模糊匹配出的内容"""
        sleep(2)
        self.d(resourceId="com.hz.purchase:id/ll_btn_search").click()  # 点击首页搜索框
        self.d(resourceId="com.hz.purchase:id/et_key").send_keys("科伦药业")  # 输入药名
        self.d(index=0, className="android.widget.LinearLayout").click()  # 点击模糊搜索出的第一个商品
        self.d(text="乙酰螺旋霉素片").exists(timeout=5)

    def test_search_05(self):
        """首页输入框中选择历史记录"""
        sleep(2)
        self.d(resourceId="com.hz.purchase:id/ll_btn_search").click()  # 点击首页搜索框
        self.d(resourceId="com.hz.purchase:id/et_key").click()  # 点击输入框
        self.d(index=0, className="android.widget.LinearLayout").click()  # 选择第一个历史记录
        self.d(text="筛选").exists(timeout=5)
