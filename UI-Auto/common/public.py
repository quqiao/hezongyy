from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep

home_url = "http://47.97.73.102:9521"
login_url = "http://47.97.73.102:9521/auth/login"
xianshang_login_url = "https://www.hezongyy.com/auth/login"


class PublicMethod(BasePage):
    ad = (By.XPATH, "//*[@id='app']/div/div[1]/div/span/img")  # 点击关掉广告
    sydl = (By.XPATH, "//*[@id='app']/div/div[1]/div[1]/div/ul[1]/li[3]/a")  # 首页登录按钮
    username = (By.XPATH, "//*[@id='username']")  # 用户名
    password = (By.XPATH, "//*[@id='password']")  # 密码
    submit = (By.XPATH, "//*[@id='right_1']/a")  # 登录

    # Action
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    def login(self, uname, pwd):
        self.find_element(*self.sydl).click()
        self.find_element(*self.username).send_keys(uname)
        self.find_element(*self.password).send_keys(pwd)
        self.find_element(*self.submit).click()
        sleep(2)

    def get_url(self, base_url):
        self.driver.get(base_url)
        self.driver.maximize_window()
        sleep(1)

    # 调用windows_handles,句柄切换到首页
    def switch_home(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    # 调用windows_handles,句柄切换到第二页
    def switch_secendPage(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    # 调用click，关掉广告
    def click_ad(self):
        self.find_element(*self.ad).click()

    # 调用script，向下滚动对应像素
    def scroll_down(self, xiangsu):
        self.script1(xiangsu)




