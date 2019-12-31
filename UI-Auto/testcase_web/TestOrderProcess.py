# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import unittest
from pages.CategoriesPage import CategoriesPage
from pages.HomePage import HomePage
from pages.PuYaoPage import PuYaoPage
from pages.JingPinZhuanQuPage import JingPinZhuanQuPage
from pages.SettlePage import SettlePage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage
from pages.ZhongYaoPage import ZhongYaoPage
from pages.GoodsDetailPage import GoodsDetailPage
from common.public import PublicMethod
from selenium import webdriver
from time import sleep
from common.public import xianshang_url, home_url

class TestOrderProcess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
            pass


    def setUp(self):
        chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromedriver)
        self.url = home_url
        self.public_page = PublicMethod(self.driver, self.url, u"合纵药易购订单界面")  # 声明publicMethod类对象
        self.categories_page = CategoriesPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明categoriesPage类对象
        self.home_page = HomePage(self.driver, self.url, u"合纵药易购订单界面")  # 声明homepage类对象
        self.puyao_page = PuYaoPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明puyaopage类对象
        self.jpzq_page = JingPinZhuanQuPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明jingpinzhuanqu类对象
        self.settle_page = SettlePage(self.driver, self.url, u"合纵药易购订单界面")  # 声明settlepage类对象
        self.cart_page = CartPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明cartpage类对象
        self.order_page = OrderPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明orderpage类对象
        self.zhongyao_page = ZhongYaoPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明zhongyaoPage类对象
        self.goodsDetail_Page = GoodsDetailPage(self.driver, self.url, u"合纵药易购订单界面")  # 声明GoodsDetailPage类对象
        self.driver.implicitly_wait(5)
        self.ssnr = "阿胶"
        self.username = "测试05"
        self.password = "123456"
        self.ddbz = "订单备注"
        self.shuliang = 20
        self.public_page.get_url(self.url)
        self.public_page.login(self.username, self.password)
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭

    def tearDown(self):
        self.driver.quit()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        # chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
        # cls.driver = webdriver.Chrome(executable_path=chromedriver)
        # cls.driver.quit()
        pass

    def test_OrderProcess_01(self):
        """在普药中选择商品进行下单"""
        sleep(2)
        self.categories_page.click_py()  # 点击普药进入普药列表
        sleep(0.5)
        self.puyao_page.click_addcart1()  # 点击第一个商品加入购物车
        sleep(2)
        self.puyao_page.click_addcart2()  # 点击第二个商品加入购物车
        sleep(2)
        self.puyao_page.click_addcart3()  # 点击第三个商品加入购物车
        sleep(2)
        self.home_page.click_gwc()  # 进入购物车界面
        sleep(0.5)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_02(self):
        """在精品专区中选择商品进行下单"""
        sleep(2)
        self.categories_page.click_jpzq()  # 点击精品专区进入精品列表
        sleep(2)
        self.jpzq_page.click_addcart1()  # 输入第一个商品加入购物车
        sleep(2)
        self.jpzq_page.click_addcart2()  # 输入第二个商品加入购物车
        sleep(2)
        self.jpzq_page.click_addcart3()  # 输入第三个商品加入购物车
        sleep(1)
        self.home_page.click_gwc()  # 进入购物车界面
        sleep(2)
        self.cart_page.input_number1(self.shuliang, 0)
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 1)
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 2)
        sleep(0.5)
        self.cart_page.click_jiage()
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_03(self):
        """在中药专区选择商品进行下单"""
        sleep(1)
        self.categories_page.click_zyzq()  # 点击进入中药专区
        sleep(1)
        self.zhongyao_page.click_ljqg1()  # 点击第一个商品立即抢购
        sleep(1)
        self.public_page.switch_secendPage()  # 句柄切换到第二页中
        sleep(1)
        self.goodsDetail_Page.click_jrgwc()  # 点击加入购物车
        sleep(1)
        self.driver.close()  # 退出商品详情页面
        sleep(1)
        self.public_page.switch_home()  # 句柄切换到首页
        sleep(1)
        self.zhongyao_page.click_ljqg2()  # 点击第二个商品立即抢购
        sleep(1)
        self.public_page.switch_secendPage()  # 句柄切换到第二页
        sleep(1)
        self.goodsDetail_Page.click_jrgwc()  # 点击加入购物车
        sleep(1)
        self.goodsDetail_Page.click_gwc()  # 点击购物车按钮
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 0)  # 输入第一个商品的数量
        sleep(2)
        self.cart_page.input_number1(self.shuliang, 1)  # 输入第二个商品的数量
        sleep(1)
        self.cart_page.click_jiage()
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_04(self):
        """呼吸系统用药商品下单"""
        sleep(2)
        self.categories_page.click_list1()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list1_1()  # 点击进入抗感冒类界面
        sleep(1)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(0.5)
        self.puyao_page.click_addcart1()  # 商品1加入购物车
        sleep(2)
        self.puyao_page.click_addcart2()  # 商品2加入购物车
        sleep(2)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(0.5)
        self.cart_page.input_number1(self.shuliang, 0)  # 输入第一个商品的数量
        sleep(2)
        self.cart_page.input_number1(self.shuliang, 1)  # 输入第二个商品的数量
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_05(self):
        """清热消炎商品下单"""
        sleep(0.5)
        self.categories_page.click_list2()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list2_1()  # 点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        self.puyao_page.click_addcart1()  # 商品1加入购物车
        sleep(1)
        self.puyao_page.click_addcart2()  # 商品2加入购物车
        sleep(1)
        self.puyao_page.click_addcart3()  # 商品3加入购物车
        sleep(5)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 0)  # 输入第一个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 1)  # 输入第二个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 2)  # 输入第三个商品的数量
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_06(self):
        """五官皮肤及外用商品下单"""
        sleep(0.5)
        self.categories_page.click_list3()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list3_1()  # 点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        self.puyao_page.click_addcart1()  # 商品1加入购物车
        sleep(1)
        self.puyao_page.click_addcart2()  # 商品2加入购物车
        sleep(1)
        self.puyao_page.click_addcart3()  # 商品3加入购物车
        sleep(5)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(0.5)
        self.cart_page.input_number1(self.shuliang, 0)  # 调用给第一个商品输入数量
        sleep(2)
        self.cart_page.input_number1(self.shuliang, 1)  # 调用给第二个商品输入数量
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        # sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_07(self):
        """补益安神及维矿类商品下单"""
        sleep(0.5)
        self.categories_page.click_list5()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list5_1()  # 点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        self.puyao_page.click_addcart1()  # 商品1加入购物车
        sleep(1)
        self.puyao_page.click_addcart2()  # 商品2加入购物车
        sleep(1)
        self.puyao_page.click_addcart3()  # 商品3加入购物车
        sleep(5)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(0.5)
        self.cart_page.input_number1(self.shuliang, 0)  # 输入第一个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 1)  # 输入第二个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 2)  # 输入第三个商品的数量
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        # sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_08(self):
        """商品分类——妇、儿科列表"""
        sleep(0.5)
        self.categories_page.click_list6()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list6_1()  # 点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        self.puyao_page.click_addcart1()  # 商品1加入购物车
        sleep(1)
        self.puyao_page.click_addcart2()  # 商品2加入购物车
        sleep(1)
        self.puyao_page.click_addcart3()  # 商品3加入购物车
        sleep(5)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(0.5)
        self.cart_page.input_number1(self.shuliang, 0)  # 输入第一个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 1)  # 输入第二个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 2)  # 输入第三个商品的数量
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        # sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_09(self):
        """商品分类——心脑血管及神经类用药列表"""
        sleep(0.5)
        self.categories_page.click_list7()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list7_1()  # 点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        self.puyao_page.click_addcart2()  # 商品2加入购物车
        sleep(1)
        self.puyao_page.click_addcart3()  # 商品3加入购物车
        sleep(5)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(0.5)
        self.cart_page.input_number1(self.shuliang, 0)  # 输入第一个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 1)  # 输入第二个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 2)  # 输入第三个商品的数量
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        # sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_10(self):
        """商品分类——风湿骨伤及其他药品列表"""
        sleep(0.5)
        self.categories_page.click_list9()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list9_1()  # 点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        self.puyao_page.click_addcart2()  # 商品2加入购物车
        sleep(1)
        self.puyao_page.click_addcart3()  # 商品3加入购物车
        sleep(5)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(0.5)
        self.cart_page.input_number1(self.shuliang, 0)  # 输入第一个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 1)  # 输入第二个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 2)  # 输入第三个商品的数量
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        # sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_11(self):
        """商品分类——非药品列表"""
        sleep(0.5)
        self.categories_page.click_list12()  # 点击进入呼吸系统分类选择
        sleep(0.5)
        self.categories_page.click_list12_1()  # 点击进入抗感冒类界面
        sleep(0.5)
        self.public_page.switch_secendPage()  # 句柄切换到第二页上
        sleep(1)
        self.puyao_page.click_addcart2()  # 商品2加入购物车
        sleep(1)
        self.puyao_page.click_addcart3()  # 商品3加入购物车
        sleep(5)
        self.home_page.click_gwc()  # 调用进入购物车界面按钮
        sleep(0.5)
        self.cart_page.input_number1(self.shuliang, 0)  # 输入第一个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 1)  # 输入第二个商品的数量
        sleep(1)
        self.cart_page.input_number1(self.shuliang, 2)  # 输入第三个商品的数量
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        # sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_12(self):
        """搜索内容进行下单"""
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(1)
        self.home_page.input_ssk(self.ssnr)  # 搜索框中输入内容
        sleep(1)
        self.home_page.click_ssButton()  # 点击搜索按钮
        sleep(1)
        self.home_page.click_jrgwc_ej()  # 点击商品加入购物车
        sleep(1)
        self.home_page.click_gwc()  # 购物车按钮
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")

    def test_OrderProcess_13(self):
        """搜索框联想的内容进行下单"""
        self.public_page.is_element_exist()  # 判断广告页是否弹出，弹出自动关闭
        sleep(2)
        self.home_page.input_ssk(self.ssnr)  # 搜索框中输入内容
        sleep(2)
        self.home_page.click_ssList1(0)  # 点击搜索列表第一个
        sleep(2)
        self.home_page.click_jrgwc_hqej()  # 点击商品加入购物车
        sleep(1)
        self.home_page.click_gwc()  # 购物车按钮
        sleep(1)
        self.cart_page.click_jiesuan()  # 点击结算按钮
        sleep(0.5)
        # self.settle_page.click_tjdd()  # 点击提交订单
        # sleep(0.5)
        # self.assertEqual(self.order_page.text_cgts(), "感谢您在本网站购买商品，您的订单已成功提交！")


