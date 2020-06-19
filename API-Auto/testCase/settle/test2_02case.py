import json
import unittest
from common1.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
from SaveParam.GetParam import UserLoginToken
from testCase.user import test1_01case
# pythoncom.CoInitialize()
import time
from SaveParam.GetParam import UserLoginToken

time.sleep(3)
url = geturlParams.geturlParams().get_Url2_1()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('购物车与结算.xlsx', '2修改购物车商品数量')


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
        print("执行用例：" + self.case_name)

    def test2_02case(self):
        """修改购物车商品数量接口"""
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
        hearder = {"hesytoken": UserLoginToken()}
        info = RunMain().run_main(self.method, url, data1, hearder)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        if self.case_name == 'url和参数都正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'url填写错误':  # 同上
            self.assertEqual(ss['code'], "900004")
        if self.case_name == 'url为空':  # 同上
            self.assertEqual(ss['code'], "900004")
        if self.case_name == 'goodsId为空':  # 同上
            self.assertEqual(ss['code'], "900006")
        if self.case_name == 'goodsId填写错误':  # 同上
            self.assertEqual(ss['code'], "200316")
        if self.case_name == 'type为普通':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'type为特卖':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'type为秒杀':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'type为阶梯价':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'type填写错误':  # 同上
            self.assertEqual(ss['code'], "900007")
        if self.case_name == 'type填写为空':  # 同上
            self.assertEqual(ss['code'], "900007")
        if self.case_name == 'number为0':  # 同上
            self.assertEqual(ss['code'], "200702")
        if self.case_name == 'number为50000':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'number为50001':  # 同上
            self.assertEqual(ss['code'], "900007")
        if self.case_name == 'number为错误':  # 同上
            self.assertEqual(ss['code'], "900006")
        if self.case_name == 'number为空':  # 同上
            self.assertEqual(ss['code'], "200702")
        if self.case_name == 'oldBasketType为普通':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'oldBasketType为特卖':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'oldBasketType为秒杀':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'oldBasketType为阶梯价':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'oldBasketType填写错误':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'oldBasketType填写为空':  # 同上
            self.assertEqual(ss['code'], "000000")



# if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
#     testUserLogin().checkResult()

