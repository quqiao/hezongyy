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
"""四川聚创网——院线专区"""
url = "https://www.scjuchuang.com/"
driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
"""登录后进入院线专区"""
def login():
    driver.get(url)  #
    driver.maximize_window()
    driver.find_element_by_class_name("logColor.loginStatus").click()
    driver.find_element_by_class_name("loginName").send_keys("yczs123")  #
    driver.find_element_by_class_name("loginPassword").send_keys("123456")
    driver.find_element_by_class_name("homeLoginBtn.clear").click()
    # time.sleep(5)
    # driver.find_element_by_class_name("popup-close").click()
    time.sleep(3)
    driver.find_element_by_link_text("院线专区").click()
    time.sleep(5)

workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个workbook 设置编码
worksheet = workbook.add_sheet('My Worksheet')  # 创建一个worksheet


def get_information(nub, xunhuan2):
    try:
        # 抓取第一页的数据
        if nub <= 1:
            url_page = url + "goods?attr=1&page=1"
        else:
            url_page = url + "goods?attr=1&page=%s" % str(nub)
        print(u"正在抓取的页面：%s" % url_page)
        driver.get(url_page)
        list_price = []
        for i in range(20):
            price = driver.find_elements_by_class_name("goods-price")[i].text
            list_price.append(price)
        print(list_price)

        list_name = []
        for i in range(20):
            name = driver.find_elements_by_class_name("goods-name")[i].text
            list_name.append(name)
        print(list_name)

        list_guige = []
        for i in range(1, 21):
            guige = driver.find_elements_by_css_selector("body > div.goods-list > ul > li:nth-child(%d) > p:nth-child(6)"%i)[0].text
            list_guige.append(guige)
        print(list_guige)


        list_xiaoqi = []
        for i in range(1, 21):
            xiaoqi = driver.find_elements_by_css_selector("body > div.goods-list > ul > li:nth-child(%d) > p:nth-child(7) > span:nth-child(1)"%i)[0].text
            list_xiaoqi.append(xiaoqi)
        print(list_xiaoqi)

        list_cj = []
        for i in range(1, 21):
            cj = driver.find_elements_by_css_selector("body > div.goods-list > ul > li:nth-child(%d) > p:nth-child(5)"%i)[0].text
            list_cj.append(cj)
        print(list_cj)

        p1 = 0
        for p in list_price:
            worksheet.write(p1+xunhuan2, 1, label=p)  # 写入excel,参数对应 行, 列, 值
            p1 = p1 + 1
        n1 = 0
        for n in list_name:
            worksheet.write(n1+xunhuan2, 0, label=n)  # 写入excel,参数对应 行, 列, 值
            n1 = n1 + 1
        g1 = 0
        for g in list_guige:
            worksheet.write(g1+xunhuan2, 2, label=g)  # 写入excel,参数对应 行, 列, 值
            g1 = g1 + 1
        x1 = 0
        for x in list_xiaoqi:
            worksheet.write(x1+xunhuan2, 3, label=x)  # 写入excel,参数对应 行, 列, 值
            x1 = x1 + 1
        c1 = 0
        for c in list_cj:
            worksheet.write(c1+xunhuan2, 4, label=c)
            c1 = c1 + 1

        workbook.save('scjuchuang_yxzq.xls')

    except Exception as msg:
        print(u"抓取信息过程中报错了 ：%s" % str(msg))


if __name__ == "__main__":
    login()
    xh = 0
    for i in list(range(1, 25)):
        get_information(i, xh)
        xh = xh + 20
    # save1()
