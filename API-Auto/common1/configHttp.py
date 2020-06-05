import requests
import json
from common1.Log import logger

logger = logger
class RunMain():

    def send_post(self, url, data, header):  # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, data=data, headers=header).json()  # 因为这里要封装post方法，所以这里的url和data值不能写死
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_put(self, url, data):
        result = requests.put(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_delete(self, url, data):
        result = requests.delete(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None, headers=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data, headers)
            logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, data)
            logger.info(str(result))
        elif method == 'put':
            result = self.send_put(url, data)
            logger.info(str(result))
        elif method == 'delete':
            result = self.send_delete(url, data)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result
if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    result = RunMain().run_main('delete', 'http://192.168.31.93:38080/SingleSignOn/find/', '{"1234567"}'.encode('utf-8'))
    print(result)