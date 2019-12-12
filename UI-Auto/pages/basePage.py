# -*- coding: utf-8 -*-
__author__ = 'quqiao'
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver



class BasePage(object):
    """
     BasePage封装所有页面都公用的方法，例如driver, url ，FindElement等
    """

    # 初始化driver、url、等
    def __init__(self, selenium_driver, base_url, pagetitle):
        self.base_url = base_url
        self.pagetitle = pagetitle
        self.driver = selenium_driver

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url, self.pagetitle)


    # 打开页面，校验页面链接是否加载正确
    def _open(self, url, pagetitle):
        self.login("测试05", "123456")
        # 使用get打开访问链接地址
        if (url == "http://47.97.73.102:9521/auth/login"):
            self.driver.get(url)
            self.driver.maximize_window()
            sleep(2)
        else:
            self.login("测试06", "123456")
            self.driver.maximize_window()
            self.driver.get(url)

        self.driver.delete_all_cookies()
        self.driver.add_cookie({'name': 'token', 'value': '13A7E9249EA392A52EC2871FBCBD881A'})
        self.driver.add_cookie({'name': 'userInfo', 'value': '%7B%22id%22%3A%2220190528000001GA%22%2C%22yhdlm%22%3A%22liuquan%22%2C%22mm%22%3A%226a95bae7c150c829cf8c17e95e3b73a2%22%2C%22yhzwm%22%3A%22%u5218%u6743%22%2C%22xb%22%3A%22%u7537%22%7D'})
        sleep(1)
        self.driver.refresh()
        sleep(1)

        # 使用assert进行校验，打开的链接地址是否与配置的地址一致。调用on_page()方法
        assert self.on_page(pagetitle), u"打开开页面失败 %s" % url

    # 重写元素定位方法
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    # 定义script方法，用于执行js脚本，范围执行结果,第一种方式
    def script1(self, src):
        self.driver.execute_script(src)

    def script2(self, src1, src2):
        self.driver.execute_script(src1, src2)

    # 重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def clear_text(self, loc):
        self.find_element(*loc).click()
        self.find_element(*loc).send_keys(Keys.CONTROL, "a")
        self.find_element(*loc).send_keys(Keys.DELETE)
        self.find_element(*loc).clear()

    def move_to_element(self, loc):
        ActionChains(self.driver).move_to_element(loc).perform()

    def get_url(self, base_url):
        self.driver.get(base_url)
        self.driver.maximize_window()

    # def login(self, uname, pwd):
    #     self.find_element(By.XPATH, "//*[@id='username']").send_keys(uname)
    #     self.find_element(By.XPATH, "//*[@id='password']").send_keys(pwd)
    #     self.find_element(By.XPATH, "//*[@id='right_1']/a").click()
    #     sleep(2)


