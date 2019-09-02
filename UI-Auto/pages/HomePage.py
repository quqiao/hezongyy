# -*- coding: utf-8 -*-
__author__ = 'liuquan'

from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from time import sleep



# 继承BasePage类
class HomePage(BasePage):
    #顶部导航
    homePage = (By.XPATH,'//ul[@class="topNav"]/li[1]')
    workspace = (By.XPATH,'//ul[@class="topNav"]/li[2]')
    subjectAdmin = (By.XPATH, '//ul[@class="topNav"]/li[3]')
    resultAdmin = (By.XPATH, '//ul[@class="topNav"]/li[4]')
    #顶部导航选中的菜单
    selectedMenu = (By.XPATH,'//li[@class="activeLi"]')

    #个人中心
    loginuser = (By.CLASS_NAME,"el-dropdown-link")
    ucenter = (By.XPATH,"//span[@class='sanjiao']/li[1]")
    userAdmin = (By.XPATH, "//span[@class='sanjiao']/li[2]")
    userAttention  = (By.XPATH, "//span[@class='sanjiao']/li[3]")
    myCollection = (By.XPATH, "//span[@class='sanjiao']/li[4]")
    logOut = (By.XPATH, "//span[@class='sanjiao']/li[5]")

    #主菜单
    mainMenu = (By.XPATH,'//i[@class="iconfont icon_top-menu"]')
    mainMenuUserAdmin = (By.XPATH,"//a[@href='#/user/user']")
    mainMenuResultAdmin = (By.XPATH,"//a[@href='#/conclusion/conclusionList']")
    mainMenuAnalysisScenceAdmin = (By.XPATH,"//a[@href='#/methodManage/methodManage']")
    mainMenuTaskAnalysis = (By.XPATH, "//a[@href='#/analysis/analysisList/analysisList]")
    mainMenuHome = (By.XPATH, "//a[@href='#/home/home']")


    #导航验证
    def Menuselected(self):
        return self.find_element(*self.selectedMenu).text

    #点击首页
    def click_homePage(self):
        self.find_element(*self.homePage).click()

    #点击工作空间
    def click_workspace(self):
        self.find_element(*self.workspace).click()

    #点击分析方案管理
    def click_subjectAdmin(self):
        self.find_element(*self.subjectAdmin).click()

    #点击分析结论管理
    def click_resultAdmin(self):
        self.find_element(*self.resultAdmin).click()

    #点击个人中心
    def click_ucenter(self):
        self.find_element(*self.loginuser).click()
        self.find_element(*self.ucenter).click()

    #点击账号管理
    def click_userAdmin(self):
        self.find_element(*self.loginuser).click()
        self.find_element(*self.userAdmin).click()

    #点击个人关注
    def click_userAttention(self):
        self.find_element(*self.loginuser).click()
        self.find_element(*self.userAttention).click()

    #点击我的收藏
    def click_myCollection(self):
        self.find_element(*self.loginuser).click()
        self.find_element(*self.myCollection).click()

    #点击退出
    def click_logOut(self):
        self.find_element(*self.loginuser).click()
        self.find_element(*self.logOut).click()

    #悬停的主菜单按钮
    def move_to_mainMenu(self):
        self.move_to_element(self.driver.find_element(*self.mainMenu))

     #主菜单进入首页
    def click_mainMenuHome(self):
        self.move_to_mainMenu()
        self.find_element(*self.mainMenuHome).click()

    #主菜单进入任务分析
    def click_mainMenuTaskAnalysis(self):
        self.move_to_mainMenu()
        self.find_element(*self.mainMenuTaskAnalysis).click()

    #主菜单进入分析场景管理
    def click_mainMenuAnalysisScenceAdmin(self):
        self.move_to_mainMenu()
        self.find_element(*self.mainMenuAnalysisScenceAdmin).click()

    #主菜单进入结论管理
    def click_mainMenuResultAdmin(self):
        self.move_to_mainMenu()
        self.find_element(*self.mainMenuResultAdmin).click()

    #主菜单进入用户管理
    def click_mainMenuUserAdmin(self):
        self.move_to_mainMenu()
        self.find_element(*self.mainMenuUserAdmin).click()


