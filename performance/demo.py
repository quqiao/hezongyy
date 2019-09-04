#   coding:utf-8

from locust import HttpLocust, TaskSet, task
import json
from random import randint



# 定义用户行为
class UserBehavior(TaskSet):
    # with open("C:/Users/Administrator/PycharmProjects/eshare/performance1/UserId.txt") as f:
    #     userId = f.readlines()
    # test1 = randint(0, 162)
    # userIds = []
    # for i in userId:
    #     userIds.append(i)
    # userId1 = userIds[test1]
    # print(userId1)
    head = {
                "Accept": "application/json",
                "Content-Type": "application/json"}
    data = {"productId": "5b95ceca00017201a8c0229f",
            "number": 1,
            "buyerId": "tttt",
            "returnUrl": "http://useraccount.api.guodong.com/callback",
            "attributelist": [
                              {"attributeId": "5b62791000028201a8c06ede",
                               "attributeValue": "111"},  # 收货角色
                              {"attributeId": "5b62791000038201a8c06ede",
                               "attributeValue": "111****1111"}  # 联系电话
                             ]
            }
    data1 = json.dumps(data)

    @task(1)
    def CreateOrder(self):

        with self.client.post("Orders/CreateOrder", headers=self.head, data=self.data1,catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')



class WebsiteUser(HttpLocust):
    host = "http://order.api.guodong.com/"
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    stop_timeout = 10
    weight = 1
