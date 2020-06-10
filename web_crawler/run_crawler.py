#coding:utf-8
import time, os, sys
import unittest
# from testcase_web import TestLogin
import xlwt


if __name__ == "__main__":

    """定义爬取网站页面的目录"""
    test_dir = 'crawler_page_selenium'  # 指定测试用例为当前文件夹下的test_case目录
    discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='crawler*.py')  # 执行所有Test的测试用例
    # discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='TestJiFenShangChengShangPin.py')  # 执行指定的测试用例

    """测试用例执行"""
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建一个workbook 设置编码
    # runner.run(suite)  # 按照testsuite执行
    # test.run(discover)  # 按照discover批量执行
    now = time.strftime("%Y-%m-%d")
    workbook.save('./report/longyi_tjzq_%s.xls' % now)

    """发送测试报告"""
    # test_report = './report'  # 定义报告文件目录
    # rep = report(test_report)
    # send_mail(rep)