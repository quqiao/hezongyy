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

url = "https://www.scjuchuang.com/"
driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
"""进入"""
list_name = []
list_price = []
list_guige = []
list_cj = []
# list_xiaoqi = []
def goodsDetail():
    driver.get(url)  # 获取访问url
    driver.maximize_window()  # 最大化窗口
    driver.find_element_by_class_name("logColor.loginStatus").click()  # 点击登录
    driver.find_element_by_class_name("loginName").send_keys("yczs123")  # 输入账号
    driver.find_element_by_class_name("loginPassword").send_keys("123456")  # 输入密码
    driver.find_element_by_class_name("homeLoginBtn.clear").click()  # 登录
    # time.sleep(3)
    # driver.find_element_by_class_name("popup-close").click()
    time.sleep(3)
    target = driver.find_element_by_class_name("brankHead")
    driver.execute_script("arguments[0].scrollIntoView();", target)
    time.sleep(2)
    title_box = ["281", "299", "300", "301", "302"]
    for i in title_box:
        driver.find_element_by_id(i).click()
        for j in range(11):
            s = driver.find_element_by_class_name("recomUl.recomUl281")
            s.find_elements_by_tag_name("li")[j].click()
            time.sleep(3)
            windows = driver.window_handles
            driver.switch_to.window(windows[1])
            time.sleep(3)
            name = driver.find_element_by_class_name("detail-name").text
            list_name.append(name)

            price = driver.find_element_by_class_name("detail-old-price.showPrice").text
            list_price.append(price)

            guige1 = driver.find_elements_by_class_name("detail-desc-item")[0]
            guige2 = guige1.find_elements_by_tag_name("p")[0]
            guige3 = guige2.find_elements_by_tag_name("span")[1].text
            list_guige.append(guige3)

            cj = driver.find_element_by_class_name("detail-enterprise").text
            list_cj.append(cj)

            # xiaoqi1 = driver.find_element_by_class_name("detail-late-time")
            # xiaoqi2 = xiaoqi1.find_elements_by_tag_name("span")[1].text
            # list_xiaoqi.append(xiaoqi2)
            driver.close()  # 关闭商品详情页
            time.sleep(3)
            driver.switch_to.window(windows[0])
            print(list_cj)

workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个workbook 设置编码
worksheet = workbook.add_sheet('My Worksheet')  # 创建一个worksheet
def save_excel():
    n1 = 0
    for n in list_name:
        worksheet.write(n1, 0, label=n)  # 写入excel,参数对应 行, 列, 值
        n1 = n1 + 1
    p1 = 0
    for p in list_price:
        worksheet.write(p1, 1, label=p)  # 写入excel,参数对应 行, 列, 值
        p1 = p1 + 1
    g1 = 0
    for g in list_guige:
        worksheet.write(g1, 2, label=g)  # 写入excel,参数对应 行, 列, 值
        g1 = g1 + 1
    # x1 = 0
    # for x in list_xiaoqi:
    #     worksheet.write(x1, 3, label=x)  # 写入excel,参数对应 行, 列, 值
    #     x1 = x1 + 1
    c1 = 0
    for c in list_cj:
        worksheet.write(c1, 4, label=c)
        c1 = c1 + 1

    workbook.save('scjuchuang_wntj.xls')

if __name__ == "__main__":
    goodsDetail()
    save_excel()