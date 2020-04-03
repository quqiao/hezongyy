# coding:utf-8
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib
from urllib import request
import re
import time
import xlwt

requests.adapters.DEFAULT_RETRIES = 50
s = requests.session()  # 新建session
s.keep_alive =False
url = "https://www.scjuchuang.com/"
driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
"""登录后进入院线专区"""
def get_cookie(url):
    try:
        driver.get(url)  #
        driver.maximize_window()
        driver.find_element_by_class_name("logColor.loginStatus").click()
        driver.find_element_by_class_name("loginName").send_keys("yczs123")  #
        driver.find_element_by_class_name("loginPassword").send_keys("123456")
        driver.find_element_by_class_name("homeLoginBtn.clear").click()
        time.sleep(5)
        cookies = driver.get_cookies()
        print(cookies)
        driver.quit()
        return cookies
    except Exception as msg:
        print(u"启动浏览器报错了：%s" % str(msg))
    # driver.find_element_by_class_name("popup-close").click()
    # time.sleep(3)
    # driver.find_element_by_link_text("院线专区").click()
    # time.sleep(2)

def add_cookies(cookies):
    '''往session添加cookies'''
    try:
        # 添加cookies到CookieJar
        c = requests.cookies.RequestsCookieJar()
        for i in cookies:
            c.set(i["name"], i['value'])
        s.cookies.update(c)  # 更新session里cookies
    except Exception as msg:
        print(u"添加cookies的时候报错了：%s" % str(msg))

def get_information(nub):
    try:
        # 抓取第一页的数据
        if nub <= 1:
            url_page = url + "goods?attr=1&page=1"
        else:
            url_page = url + "goods?attr=1&page=%s" % str(nub)
        print(u"正在抓取的页面：%s" % url_page)
        requests.packages.urllib3.disable_warnings()
        r2 = s.get(url_page, verify=False)
        soup = BeautifulSoup(r2.content, "html.parser")
        time.sleep(2)
        price = soup.find_all(class_="goods-price")
        price1 = price.string
        print(price1)
        name = soup.find_all(class_="goods-name")
        name1 = name.string
        # guige = soup.find_all(text="规格：")
        # print(guige)
        # xiaoqi = soup.find_all(text="效期：")
        workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个workbook 设置编码
        worksheet = workbook.add_sheet('My Worksheet')  # 创建一个worksheet
        for p in price1:
            worksheet.write(price1.index(int(p)+1), 1, label=p)  # 写入excel,参数对应 行, 列, 值
        for n in name1:
            worksheet.write(name1.index(int(n)+1), 2, label=n)  # 写入excel,参数对应 行, 列, 值
        # for g in guige:
        #     worksheet.write(guige.index(g+1), 3, label=g)  # 写入excel,参数对应 行, 列, 值
        # for x in xiaoqi:
        #     worksheet.write(xiaoqi.index(x+1), 4, label=x)  # 写入excel,参数对应 行, 列, 值
        workbook.save('Excel_test.xls')  # 保存

    except Exception as msg:
        print(u"抓取信息过程中报错了 ：%s" % str(msg))


if __name__ == "__main__":
    cookies = get_cookie(url)
    add_cookies(cookies)
    # n = get_ye_nub(url)
    # for i in list(range(1, n + 1)):
    #     save_name(i)
    # for i in range(1, 34):
    get_information(1)
