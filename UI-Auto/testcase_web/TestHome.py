# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.HomePage import HomePage
from selenium import webdriver
from time import sleep
from common.public import home_url, PublicMethod

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(30)
        cls.url = home_url
        cls.username = "测试05"
        cls.password = "123456"
        cls.ssnr = "感冒灵"
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵易购首页界面")  # 声明publicMethod类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购首页界面")  # 声明LoginPage类对象
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.click_ad()  # 关闭广告

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_home_01(self):
        """进入中药专区"""
        sleep(2)
        self.home_page.script_zyzq()  # 进入中药专区
        sleep(0.5)
        # self.assertEqual(self.home_page.check_zyzq(), "配方中药饮片")  # 检查中药专区
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_02(self):
        """进入院线专区"""
        sleep(0.5)
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.script_yxzq()  # 点击院线专区
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_03(self):
        """进入VIP专区"""
        sleep(0.5)
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.click_vip()  # 点击VIP专区
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_04(self):
        """进入促销专区"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.click_cxzq()  # 点击促销专区
        # sleep(0.5)
        # self.assertEqual(self.home_page.check_week(), "加入购物车")  # 检查促销专区
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_05(self):
        """进入保健品专区"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.click_bjpzq()
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_06(self):
        """进入每周精选页面检查"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.scroll_mzjx()  # 下滑到本周精选页面显示
        sleep(0.5)
        # 点击精选内容
        self.home_page.click_week()
        # 跳转到新页面后需重新定位
        sleep(1)
        self.public_page.switch_secendPage()  # 定位到当前页面
        # 关闭当前页面
        self.driver.close()

    def test_home_07(self):
        """进入品牌专区"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.scroll_mzjx()  # 滚动到品牌专区栏
        sleep(0.5)
        self.home_page.click_ppzqhyh()  # 点击换一换，切换品牌
        sleep(0.5)
        self.home_page.click_ppzqckqb()  # 点击进入查看
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_08(self):
        """进入新品上架列表"""
        sleep(0.5)
        self.public_page.switch_home()   # 定位到首页
        sleep(5)
        self.home_page.scroll_xpsj()  # 滚动到新品上架
        sleep(5)
        self.home_page.click_xpsjdt()  # 点击新品上架大图
        sleep(5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_09(self):
        """进入产品推荐列表"""
        sleep(0.5)
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.click_cptjdt()  # 点击产品推荐大图
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_10(self):
        """进入当季热销"""
        sleep(0.5)
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.scroll_djrx()  # 滚动到当季热销
        sleep(0.5)
        self.home_page.click_djrxdt()  # 点击当季热销大图
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_11(self):
        """进入家庭保健"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.click_jtbjdt()  # 点击家庭保健大图
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_12(self):
        """进入中药饮片"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.scroll_zyyp()  # 滚动到中药饮片
        sleep(0.5)
        self.home_page.click_zyypdt()  # 点击中药饮片大图
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_13(self):
        """进入诊所特供"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.click_zstgdt()  # 点击诊所特供大图
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_14(self):
        """为你推荐操作"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.scroll_wntjtitle()  # 滚动到为你推荐的位置
        sleep(0.5)
        self.home_page.click_wntjzh()  # 向左滑动
        sleep(0.5)
        self.home_page.click_wntjyh()  # 向右滑动
        sleep(0.5)
        self.home_page.click_wntjdt1()  # 点击为你推荐大图
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.driver.close()

    def test_home_15(self):
        """搜索框输入搜索没有的内容查询"""
        self.home_page.input_ssk("ssss")  # 搜索框中输入内容
        sleep(0.5)
        self.home_page.click_ssButton()  # 点击搜索按钮
        sleep(1)
        self.driver.back()
        sleep(0.5)

    def test_home_16(self):
        """搜索框输入搜索正确的内容查询"""
        self.public_page.click_ad()
        sleep(1)
        self.home_page.input_ssk(self.ssnr)  # 搜索框中输入内容
        sleep(0.5)
        self.home_page.click_ssButton()  # 点击搜索按钮
        sleep(0.5)
        self.driver.back()
        sleep(0.5)

    def test_home_17(self):
        """搜索框联想的内容查询"""
        self.public_page.click_ad()
        sleep(2)
        self.home_page.input_ssk(self.ssnr)  # 搜索框中输入内容
        sleep(2)
        self.home_page.click_ssList1()  # 点击搜索列表第一个
        sleep(2)
        self.driver.back()
        sleep(0.5)




