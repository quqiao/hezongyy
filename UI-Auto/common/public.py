from selenium.webdriver.common.by import By
from pages.basePage import BasePage

host = "http://47.97.73.102:9521"


class PublicMethod(BasePage):
    ad = (By.XPATH, "//*[@id='app']/div/div[1]/div/span/img")  # 点击关掉广告

    # 调用windows_handles,句柄切换到首页
    def switch_home(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    # 调用windows_handles,句柄切换到第二页
    def switch_secendPage(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    # Action
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 调用click，关掉广告
    def click_ad(self):
        self.find_element(*self.ad).click()



