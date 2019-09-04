#coding:utf-8
import time,os,sys
from common.HTMLTestRunner import HTMLTestRunner
from common.email import send_mail,report
import unittest


if __name__ == "__main__":
    # 指定测试用例为当前文件夹下的test_case目录
    test_dir = './testcase'
    discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='Test*.py')

    # now = time.strftime("%Y%m%d%H%M%S")
    now = time.strftime("%Y-%m-%d")
    filename = './report/'+'合纵药易购web端UI回归测试_' + now+'.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp,
                            title="合纵药易购回归测试",
                            description="合纵药易购自动化回归测试")
    runner.run(discover)
    fp.close()

    # 发送测试报告
    # test_report = './report'  # 定义报告文件目录
    # rep = report(test_report)
    # send_mail(rep)
