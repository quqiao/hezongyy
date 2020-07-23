import json
import unittest
from common1.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
from testCase.user import test1_01case
# pythoncom.CoInitialize()
import time

time.sleep(3)
# url = geturlParams.geturlParams().get_Url2_1()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('业务员APP.xlsx', '6查询商品列表')

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

    def test2_04case(self):
        """6查询商品列表接口"""
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
        url = 'http://' + self.url + ':' + self.port + self.path
        info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        if self.case_name == 'goodsGroupIds为1个':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'goodsGroupIds为2个':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'goodsGroupIds为多个':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'goodsGroupIds为错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'goodsGroupIds为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'pageNumber正确':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'pageNumber错误':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'pageNumber为空':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'pageSize正确':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'pageSize正确':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'pageSize错误':  # 同上
            self.assertEqual(ss['code'], "900006")
        if self.case_name == 'pageSize为空':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'sortFieldCode为默认排序':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'sortFieldCode为销量':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'sortFieldCode为价格':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'sortFieldCode错误':  # 同上
            self.assertEqual(ss['code'], "900006")
        if self.case_name == 'sortFieldCode为空':  # 同上
            self.assertEqual(ss['code'], "900006")
        if self.case_name == 'sortOrderCode为倒序':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'sortOrderCode为升序':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'sortOrderCode错误':  # 同上
            self.assertEqual(ss['code'], "900006")
        if self.case_name == 'sortOrderCode为空':  # 同上
            self.assertEqual(ss['code'], "900006")
        print("返回信息：" + ss['message'])

# if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
#     testUserLogin().checkResult()
