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
login_xls = readExcel.readExcel().get_xls('商品信息.xlsx', '1商品列表条件查询')

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
        print(self.case_name+"测试开始前准备")
        url = 'http://' + self.url + ':' + self.port + self.path
        print(url)

    def test1_02case(self):
        """1商品列表条件查询接口"""
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
        if self.case_name == 'brandId正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'brandId错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'brandId为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'id正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'id错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'id为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'vip正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'vip错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'vip为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'limitSize正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'limitSize错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'limitSize为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'limitStart正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'limitStart错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'limitStart为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'goodsIdList正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'goodsIdList错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'goodsIdList为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'manufacturerName正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'manufacturerName错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'manufacturerName为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'keywords正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'keywords错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'keywords为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'specification正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'specification错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'specification为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'dosageForm正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'dosageForm错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'dosageForm为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'serialNumberList正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'serialNumberList错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'serialNumberList为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'orderColumn正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderColumn错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'orderColumn为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'orderRule正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'orderRule错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'orderRule为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'statisticStart正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'statisticStart错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'statisticStart为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'statisticEnd正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'statisticEnd错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'statisticEnd为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'preferentialAmount正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'preferentialAmount错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'preferentialAmount为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'gift正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'gift错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'gift为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'specialSale正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'specialSale错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'specialSale为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'checkExpirationDate正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'checkExpirationDate错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'checkExpirationDate为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'preferential正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'preferential错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'preferential为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'vip正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'vip错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'vip为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'menuId正确':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'menuId错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'menuId为空':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'category为普药':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'category为麻黄碱':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'category为血液制品':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'category错误':  # 同上
            self.assertEqual(ss['code'], "900000")
        if self.case_name == 'category为空':  # 同上
            self.assertEqual(ss['code'], "900000")



# if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
#     print(testUserLogin().checkResult())
