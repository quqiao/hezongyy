import json
import unittest
from common1.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import time
import readExcel
# pythoncom.CoInitialize()

# url = geturlParams.geturlParams().get_Url1_3()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('业务员APP.xlsx', '21条件查询订单')

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
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
        print("执行用例：" + self.case_name)
        url = 'http://' + self.url + ':' + self.port + self.path
        print(url)

    def test1_02case(self):
        """21条件查询订单接口"""
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
        # data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        url = 'http://' + self.url + ':' + self.port + self.path
        data1 = self.query.encode('utf-8')
        info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        if self.case_name == 'orderStatus为待开票':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderStatus为已开票':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderStatus为已拣货':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderStatus为已出库':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderStatus为已发货':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderStatus为已完成':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderStatus为2个':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderStatus为多个':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderStatus为错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderStatus为空':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'payStatus为未支付':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'payStatus为已支付':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'payStatus为错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'payStatus为空':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'salesmanId为正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'salesmanId为错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'salesmanId为空':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'startTime为正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'startTime为错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'startTime为空':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'endTime为正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'endTime为错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'endTime为空':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'pageNumber为正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'pageNumber为错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'pageNumber为空':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'pageSize为正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'pageSize为错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'pageSize为空':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'goodsGroupId为正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'goodsGroupId为错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'goodsGroupId为空':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')

# if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
#     print(testUserLogin().checkResult())
