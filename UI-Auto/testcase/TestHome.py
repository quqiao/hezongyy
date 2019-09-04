# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.HomePage import HomePage
from selenium import webdriver
from time import sleep
from common.public import host

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(30)
        cls.url = host
        cls.phone = "18056558899"
        cls.password = "123456"
        # 声明LoginPage类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购反馈界面")
        cls.home_page.open()

    # 全部商品分类检查
    def test_1_home_sort(self):
        # 关掉广告
        # self.home_page.click_ad()
        # 点击呼吸系统用药列表
        self.home_page.click_list1()
        # 检查呼吸系统用药列表
        self.assertEqual(self.home_page.check_list1(), "呼吸系统用药")
        # 点击清热消炎列表
        self.home_page.click_list2()
        # 检查清热消炎列表
        self.assertEqual(self.home_page.check_list2(), "清热、消炎类")

    # 进入本周精选检查
    def test_2_home_week(self):
        # 下滑到本周精选页面显示
        target = self.driver.find_element_by_xpath("//*[@id='mzjx']/div/div[1]/span[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        sleep(0.5)
        # 点击精选内容
        self.home_page.click_week()
        # 跳转到新页面后需重新定位
        sleep(1)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        # 检查每周精选页面
        self.assertEqual(self.home_page.check_week(), "加入购物车")
        # 关闭当前页面
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
