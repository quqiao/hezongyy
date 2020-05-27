# coding:utf-8
__author__ = 'quqiao'
import time, os, sys
from common.HTMLTestRunner import HTMLTestRunner
# from common1.email import send_mail,report
import unittest
from testcase_android import testLogin

if __name__ == "__main__":
    """用例构造及选择"""
    # 指定测试用例为当前文件夹下的test_case目录
    test_dir = './testcase_android'
    discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')  # 执行批量的测试用例
    # discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='testLogin.py')  # 执行指定的测试用例

    # 使用testsuit进行用例选择
    # suite = unittest.TestSuite()
    # TestCases = [testLogin("test_1_login_noUserAndPwd")]  # 选择测试用例
    # suite.addTests(TestCases)

    """测试报告生成"""
    # now = time.strftime("%Y%m%d%H%M%S")
    now = time.strftime("%Y-%m-%d")
    filename = './report/'+'合纵药易购android端UI回归测试_' + now+'.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp,
                            title="合纵药易购回归测试",
                            description="合纵药易购自动化回归测试")

    """测试报告执行"""
    runner.run(discover)  # 测试用例批量执行
    # runner.run(suite)  # 测试用例选择执行
    fp.close()

    """发送测试报告"""
    # test_report = './report'  # 定义报告文件目录
    # rep = report(test_report)
    # send_mail(rep)
