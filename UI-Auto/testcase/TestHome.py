# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage
from selenium import webdriver
from time import sleep
from common.public import host

class TestLogin(unittest.TestCase):
    "safsafd"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.url = host+"/home/home"


        # 声明LoginPage类对象
        cls.homePage = HomePage(cls.driver, cls.url, u"情况分析")
        cls.homePage.open()

    #通过导航页进入首页
    def test_1_enter_home_by_topNav(self):
        self.homePage.click_homePage()
        self.assertEqual(self.homePage.Menuselected(),"首页")

    #通过导航页进入工作台
    def test_2_enter_workspace_by_topNav(self):
        self.homePage.click_workspace()
        sleep(2)
        self.assertEqual(self.homePage.Menuselected(), "分析中心工作台")
        self.driver.find_element(By.XPATH,"//span[@class='entitySearchPopover_title']").is_displayed()

    #通过导航页进入主题管理
    def test_3_enter_subjectAdmin_by_topNav(self):
        self.homePage.click_subjectAdmin()
        sleep(2)
        self.assertEqual(self.homePage.Menuselected(), "分析方案管理")
        self.driver.find_element(By.XPATH, "//div[@class='managementScenario-leftSide-title']").is_displayed()

    # 通过导航页进入结果列表
    def test_4_enter_resultAdmin_by_topNav(self):
        self.homePage.click_resultAdmin()
        sleep(2)
        self.assertEqual(self.homePage.Menuselected(), "分析结论管理")
        self.driver.find_element(By.XPATH, "//form[@class='el-form el-form--label-right']").is_displayed()

    def test_5_enter_mainMenuResultAdmin(self):
        self.homePage.click_mainMenuResultAdmin()
        sleep(4)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
