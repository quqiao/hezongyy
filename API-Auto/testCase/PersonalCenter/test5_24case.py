import json
import unittest
from common1.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
from testCase.user import test1_02case
# pythoncom.CoInitialize()
import time

time.sleep(3)
url = geturlParams.geturlParams().get_Url2_1()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('个人中心.xlsx', '24用户金币')
with open('./SaveParam/login_token.txt', 'r', encoding='utf-8') as f:
    hesytoken = f.read()  # 获取cookies
    f.close()


@paramunittest.parametrized(*login_xls)
class testSettleAddGoodsCart(unittest.TestCase):
    def setParameters(self, case_name, url, port,  path, query, method, expected, result):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.url = str(url)
        self.port = str(int(port))
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.expected = str(expected)
        self.result = str(result)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")

    def test2_04case(self):
        """24用户金币接口"""
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        """
        check test result
        :return:
        """
        # url1 = "http://www.xxx.com/login?"
        # new_url = url1 + self.query
        # data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query)) # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        data1 = self.query.encode('utf-8')
        # hearder = {"hesytoken": "32fcb1ca-a6d7-11ea-858f-0a0027000008"}
        hearder = {"hesytoken": hesytoken}
        info = RunMain().run_main(self.method, url, data1, hearder)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        if self.case_name == 'pageNumber正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'pageNumber错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 'x')
        if self.case_name == 'pageNumber为空':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 'x')

# if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
#     testUserLogin().checkResult()

