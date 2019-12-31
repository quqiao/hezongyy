# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.HomePage import HomePage
from pages.GoodsDetailPage import GoodsDetailPage
from selenium import webdriver
from time import sleep
from common.public import home_url, PublicMethod,xianshang_url

class TestHome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chromedriver)
        cls.driver.implicitly_wait(5)  # 隐式等待
        cls.url = home_url
        cls.username = "测试05"
        cls.password = "123456"
        cls.ssnr = "感冒灵"
        cls.xiangsu1 = "window.scrollBy(0, 800)"
        cls.xiangsu2 = "window.scrollBy(0, 200)"
        cls.public_page = PublicMethod(cls.driver, cls.url, u"合纵易购首页界面")  # 声明publicMethod类对象
        cls.home_page = HomePage(cls.driver, cls.url, u"合纵易购首页界面")  # 声明LoginPage类对象
        cls.goodsDetail_page = GoodsDetailPage(cls.driver, cls.url, "合纵易购首页界面")  # 声明GoodsDetailPage类对象
        cls.public_page.get_url(cls.url)
        cls.public_page.login(cls.username, cls.password)
        cls.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_home_01(self):
        """进入中药专区"""
        sleep(2)
        self.home_page.script_zyzq()  # 进入中药专区
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"中药专区" in title)  # 判断标题中包含有普药
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
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"院线专区" in title)  # 判断标题中包含有普药
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
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"vip专区" in title)  # 判断标题中包含有普药

    def test_home_04(self):
        """进入促销专区"""
        sleep(0.5)
        self.driver.close()
        sleep(1)
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.click_cxzq()  # 点击促销专区
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"促销专区" in title)  # 判断标题中包含有普药
        sleep(0.5)
        self.driver.close()

    def test_home_05(self):
        """进入保健品专区"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.home_page.click_bjpzq()
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"保健专区" in title)  # 判断标题中包含有普药
        sleep(0.5)
        self.driver.close()

    def test_home_06(self):
        """进入每周精选页面检查"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.public_page.scroll_down(self.xiangsu1)
        sleep(2)
        self.home_page.click_week()  # 点击精选内容
        sleep(1)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"促销专区" in title)  # 判断标题中包含促销专区
        sleep(1)
        self.driver.close()  # 关闭当前页面

    def test_home_07(self):
        """进入品牌专区"""
        self.public_page.switch_home()   # 定位到首页
        sleep(0.5)
        self.public_page.scroll_down(self.xiangsu2)  # 滚动到品牌专区栏
        sleep(0.5)
        self.home_page.click_ppzqhyh()  # 点击换一换，切换品牌
        sleep(0.5)
        self.home_page.click_ppzqckqb()  # 点击进入查看
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(1)
        title = self.driver.title
        sleep(1)
        self.assertTrue(u"品牌专区" in title)  # 判断标题中包含有普药
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
        sleep(3)
        self.home_page.click_wntjdt1()  # 点击为你推荐大图
        sleep(0.5)
        self.public_page.switch_secendPage()  # 定位到当前页面
        sleep(0.5)
        self.assertEqual(self.goodsDetail_page.text_bt(), "为您推荐", msg="没有进入商品详情页面")  # 判断是否进入商品详情页

    def test_home_15(self):
        """搜索框输入搜索没有的内容查询"""
        sleep(1)
        self.driver.close()
        sleep(1)
        self.public_page.switch_home()
        sleep(1)
        self.home_page.input_ssk("@#$%^")  # 搜索框中输入内容
        sleep(0.5)
        self.home_page.click_ssButton()  # 点击搜索按钮
        sleep(1)
        self.assertEqual(self.home_page.text_sswk(), "发布求购", msg="搜索没有的内容错误")  # 判断没有的内容搜索查询时
        sleep(1)
        self.driver.back()
        sleep(0.5)

    def test_home_16(self):
        """搜索框输入搜索正确的内容查询"""
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(1)
        self.home_page.input_ssk(self.ssnr)  # 搜索框中输入内容
        sleep(0.5)
        self.home_page.click_ssButton()  # 点击搜索按钮
        sleep(0.5)
        mingzi = self.home_page.text_spmz()
        sleep(1)
        self.assertTrue(u"感冒灵" in mingzi)
        sleep(1)
        self.driver.back()
        sleep(0.5)

    # def test_home_17(self):
    #     """搜索框联想的内容查询"""
    #     self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
    #     sleep(2)
    #     self.home_page.input_ssk(self.ssnr)  # 搜索框中输入内容
    #     sleep(2)
    #     self.home_page.click_ssList1(1)  # 点击搜索列表第一个
    #     sleep(2)
    #     mingzi = self.home_page.text_spmz()
    #     sleep(1)
    #     self.assertTrue(u"感冒灵" in mingzi)
    #     sleep(1)
    #     self.driver.back()
    #     sleep(0.5)
