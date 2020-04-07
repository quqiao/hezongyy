# coding:utf-8
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib
from urllib import request
import re
import time
import xlwt
import xlrd

url = "http://www.longyiyy.com/"
driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
"""登录后进入特价专区"""
def login():
    driver.get(url)  #
    driver.maximize_window()
    driver.find_element_by_class_name("login").click()  # 点击首页上方登录
    driver.find_element_by_name("username").send_keys("18030535053")  # 输入账号
    driver.find_element_by_name("userpass").send_keys("123456")  # 输入密码
    driver.find_element_by_class_name("is").click()  # 点击登录按钮
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[5]/div/ul[2]/li[1]/a/img").click()  # 点击特价专区
    time.sleep(5)
    windows = driver.window_handles
    driver.switch_to.window(windows[1])  # 切换到第二页
    time.sleep(2)

workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个workbook 设置编码
worksheet = workbook.add_sheet('My Worksheet')  # 创建一个worksheet

def get_information(nub, xunhuan2):
    try:
        # 抓取第一页的数据
        if nub <= 1:
            url_page = url + "events-filter-527-2-1.html"
        else:
            url_page = url + "events-filter-527-%s-1.html" % str(nub)
        print(u"正在抓取的页面：%s" % url_page)
        driver.get(url_page)

        try:
            """获取药品名称"""
            list_name = []
            for n1 in range(40):
                name = driver.find_elements_by_class_name("blue")[n1].text
                list_name.append(name)
            print(list_name)
            n2_1 = 0
            for n2 in list_name:
                worksheet.write(n2_1 + xunhuan2, 0, label=n2)  # 写入excel,参数对应 行, 列, 值
                n2_1 = n2_1 + 1

            """获取厂家名称"""
            list_cj = []
            for c1 in range(1, 41):
                cj = driver.find_elements_by_css_selector("body > div:nth-child(8) > div > div.list_containers.list-1 > ul > li:nth-child(%d) > p:nth-child(3)"%c1)[0].text
                list_cj.append(cj)
            print(list_cj)
            c2_1 = 0
            for c2 in list_cj:
                worksheet.write(c2_1 + xunhuan2, 1, label=c2)  # 写入excel,参数对应 行, 列, 值
                c2_1 = c2_1 + 1

            """获取规格"""
            list_guige = []
            for g1 in range(1, 41):
                guige = driver.find_elements_by_css_selector("body > div:nth-child(8) > div > div.list_containers.list-1 > ul > li:nth-child(%d) > p:nth-child(4)"%g1)[0].text
                list_guige.append(guige)
            print(list_guige)
            g2_1 = 0
            for g2 in list_guige:
                worksheet.write(g2_1 + xunhuan2, 2, label=g2)  # 写入excel,参数对应 行, 列, 值
                g2_1 = g2_1 + 1

            """获得效期"""
            list_xiaoqi = []
            for x1 in range(1, 41):
                xiaoqi = driver.find_elements_by_css_selector("body > div:nth-child(8) > div > div.list_containers.list-1 > ul > li:nth-child(%d) > p:nth-child(7)"%x1)[0].text
                list_xiaoqi.append(xiaoqi)
            print(list_xiaoqi)
            x2_1 = 0
            for x2 in list_xiaoqi:
                worksheet.write(x2_1 + xunhuan2, 3, label=x2)  # 写入excel,参数对应 行, 列, 值
                x2_1 = x2_1 + 1

            """获取价格"""
            list_price1 = []
            for p1 in range(40):
                price1 = driver.find_elements_by_class_name("red")[p1].text
                list_price1.append(price1)
            print(list_price1)
            p2_1 = 0
            for p2 in list_price1:
                worksheet.write(p2_1 + xunhuan2, 4, label=p2)  # 写入excel,参数对应 行, 列, 值
                p2_1 = p2_1 + 1

            list_price2 = []
            for p3 in range(1, 41):
                price2 = driver.find_elements_by_css_selector("body > div:nth-child(8) > div > div.list_containers.list-1 > ul > li:nth-child(%d) > p:nth-child(8) > span:nth-child(2)"%p3)[0].text
                list_price2.append(price2)
            p4_1 = 0
            for p4 in list_price2:
                worksheet.write(p4_1 + xunhuan2, 5, label=p4)  # 写入excel,参数对应 行, 列, 值
                p4_1 = p4_1 + 1
            now = time.strftime("%Y-%m-%d")
            workbook.save('longyi_tjzq_%s.xls' % now)
        except OSError:
            pass
    except Exception as msg:
        print(u"抓取信息过程中报错了 ：%s" % str(msg))


if __name__ == "__main__":
    login()
    xh = 0
    for i in list(range(1, 10)):
        get_information(i, xh)
        xh = xh + 40
    # save1()
