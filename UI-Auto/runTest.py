#coding:utf-8
import time, os, sys
# from common.HTMLTestRunner import HTMLTestRunner
from common.HTMLTestRunner_cn import HTMLTestRunner
from common.email import send_mail, report
import unittest
# from testcase_web import TestLogin


if __name__ == "__main__":

    """用例构造及选择"""
    # 指定测试用例为当前文件夹下的test_case目录
    test_dir = './testcase_web'
    # discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='Test*.py')  # 执行所有Test的测试用例
    discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='TestOrderProcess.py')  # 执行指定的测试用例

    # 使用testsuit进行用例选择
    # suite = unittest.TestSuite()
    # TestCases = [TestLogin("test_1_login_noUserAndPwd")]  # 选择测试用例
    # suite.addTests(TestCases)

    """测试报告生成"""
    # now = time.strftime("%Y%m%d%H%M%S")
    now = time.strftime("%Y-%m-%d")
    filename = './report/'+'合纵药易购web端执行下单模块（线上环境）_' + now+'.html'
    fp = open(filename, "wb")
    '''一般HTML报告格式'''
    # runner = HTMLTestRunner(stream=fp,
    #                         title="合纵药易购回归测试",
    #                         description="合纵药易购自动化回归测试")
    '''改版后HTML报告格式'''
    runner = HTMLTestRunner(title="回归测试报告",
                            description="test",
                            stream=fp, verbosity=2, retry=0, save_last_try=True)

    """测试用例执行"""
    # runner.run(suite)  # 按照testsuite执行
    runner.run(discover)  # 按照discover批量执行
    fp.close()

    """发送测试报告"""
    # test_report = './report'  # 定义报告文件目录
    # rep = report(test_report)
    # send_mail(rep)

