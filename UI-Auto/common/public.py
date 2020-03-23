from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from pages.basePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

home_url = "http://47.97.73.102:9521"  # 测试环境首页url
login_url = "http://47.97.73.102:9521/auth/login"  # 测试环境登录url
xianshang_login_url = "https://www.hezongyy.com/auth/login"  # 线上环境登录url
xianshang_url = "https://www.hezongyy.com/"  # 线上环境首页url
tejia_url = "http://47.97.73.102:9521/hdcx/#/tj"  # 测试环境特价页面url

test_url = "https://www.hezongyy.com/"
test_login_url = "https://www.hezongyy.com/auth/login"
username ="测试05"

"""选择不同本地驱动"""
chromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
# chromedriver = "F:/selenium_webdriver/chromedriver_win32/chromedriver.exe"

class PublicMethod(BasePage):
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    """登录操作"""
    sydl = (By.LINK_TEXT, "请登录")  # 首页登录按钮
    username = (By.XPATH, "//*[@id='username']")  # 用户名
    password = (By.XPATH, "//*[@id='password']")  # 密码
    submit = (By.XPATH, "//*[@id='right_1']/a")  # 登录
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

    """切换句柄操作"""
    # 调用windows_handles,句柄切换到首页
    def switch_home(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    # 调用windows_handles,句柄切换到第二页
    def switch_secendPage(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    """alert弹窗的"""
    # 点击确定按钮
    def switch_alert_accpet(self):
        al = self.driver.switch_to.alert()
        al.accept()

    # 点击取消按钮(如有按钮)
    def switch_alert_dismiss(self):
        al = self.driver.switch_to.alert()
        al.dismiss()

    # 点击输入内容（如有输入框）
    def switch_alert_send_keys(self, content):
        al = self.driver.switch_to.alert()
        al.send_keys(content)

    # 自定义弹窗
    def swithc_alert_customize(self):
        js = 'document.getElementById("doyoo_monitor").style.display="none";'
        self.script1(js)

    """页面滚动"""
    # 调用script，向下滚动对应像素
    def scroll_down(self, xiangsu):
        self.script1(xiangsu)

    # 调用script,向上滚动到顶部
    def scroll_top(self):
        js_top = "var q=document.documentElement.scrollTop=0"
        self.script1(js_top)

    # 调用script,向下滚动到底部
    def scroll_bottom(self):
        js_bottom1 = "var q=document.documentElement.scrollTop=10000"
        js_bottom2 = "window.scrollTo(0,document.body.scrollHeight)"
        self.script1(js_bottom1)

    # 定义select 选择框中的内容
    xlsrk = (By.CLASS_NAME, "search-list")  # 下拉输入框列表
    def select_by_index(self):
        s1 = Select(self.driver.find_element(*self.xlsrk))
        s1.select_by_index("2")
    def select_by_value(self):
        s1 = Select(self.driver.find_element(*self.xlsrk))
        s1.select_by_value("1")
    def select_by_visible_text(self):
        s1 = Select(self.driver.find_element(*self.xlsrk))
        s1.select_by_visible_text("2")

    """检查是否存在广告弹出框"""
    ad = (By.CLASS_NAME, "close")  # 点击关掉广告
    adk = (By.CLASS_NAME, "content_tj")  # 广告框弹出
    def is_element_exist(self):
        list = self.driver.find_elements(*self.adk)
        if len(list) == 0:
            # print('没有该元素')
            return 0
        elif len(list) >= 0:
            # print('共找到' + str(len(list)) + '个元素')
            self.find_element(*self.ad).click()

    """加入收藏夹，普药列表界面心形图标处"""
    jrsc = (By.CLASS_NAME, "datu-shoucang")
    def click_jrsc(self, sclist):
        self.find_elements(*self.jrsc)[sclist].click()

    """弹出框的左边按钮（确定，删除，查看收藏夹等）"""
    tckLeft = (By.CLASS_NAME, "layui-layer-btn0")
    def click_tckLeft(self):
        list = self.find_elements(*self.tckLeft)
        if len(list) == 0:
            pass
        elif len(list) >= 0:
            self.find_element(*self.tckLeft).click()

    """弹出框的右边按钮(取消）"""
    tckRight = (By.CLASS_NAME, "layui-layer-btn1")
    def click_tckRight(self):
        list = self.find_elements(*self.tckRight)
        if len(list) == 0:
            pass
        elif len(list) >= 0:
            self.find_element(*self.tckRight).click()

    """弹出框的关闭按钮"""
    tckClose = (By.CLASS_NAME, "layui-layer-setwin")
    def click_tckClose(self):
        list = self.find_elements(*self.tckClose)
        if len(list) == 0:
            pass
        elif len(list) >= 0:
            self.find_element(*self.tckClose).click()

    """F5+ctrl组合键刷新"""
    def refresh(self):
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()