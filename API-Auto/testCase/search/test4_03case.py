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

time.sleep(3)
url = geturlParams.geturlParams().get_Url2_1()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('商品.xlsx', '3生产厂家首字母键值对返回')

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
        """3生产厂家首字母键值对返回接口"""
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
        if self.case_name == 'channelType为PC':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'channelType为APP':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'channelType为错误':  # 同上
            self.assertEqual(ss['code'], "900007")
        if self.case_name == 'channelType为空':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'columnType为普药':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'columnType为精品':  # 同上
            self.assertEqual(ss['code'], "000000")
        if self.case_name == 'columnType为诊所':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'columnType为中药':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'columnType为加盟':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'columnType为错误':
            self.assertEqual(ss['code'], '900007')
        if self.case_name == 'columnType为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'searchType为商品名称':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'searchType为厂家名称':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'searchType为错误':
            self.assertEqual(ss['code'], '900007')
        if self.case_name == 'searchType为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'keyWords为正确':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'keyWords为错误':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'keyWords为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'brandId为正确':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'brandId为错误':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'brandId为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'manufacturer为正确':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'manufacturer为错误':
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'manufacturer为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'preferential为不要求':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'preferential为有要求':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'preferential为错误':
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'preferential为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'specification为正确':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'specification为错误':
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'specification为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'dosageForm为正确':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'dosageForm为错误':
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'dosageForm为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'containEphedra为不要求':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'containEphedra为有要求':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'containEphedra为错误':
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'containEphedra为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'pharmaCategoryId为正确':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'pharmaCategoryId为错误':
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'pharmaCategoryId为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'specialSale为不筛选特卖':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'specialSale为筛选特卖':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'specialSale为错误':
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'specialSale为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'label为买赠':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'label为促销':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'label为效期':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'label为错误':
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'label为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'chineseHerb为不限':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'chineseHerb为西药':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'chineseHerb为中药':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'chineseHerb为错误':
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'chineseHerb为空':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'categoryLabel为正确':
            self.assertEqual(ss['code'], '000000')
        if self.case_name == 'categoryLabel为错误':
            self.assertEqual(ss['code'], '900006')
        if self.case_name == 'categoryLabel为空':
            self.assertEqual(ss['code'], '000000')

# if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
#     testUserLogin().checkResult()

