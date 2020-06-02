#coding:utf-8

# class A(object):
#     def foo1(self):
#         print(self)
#
#     @classmethod
#     def foo2(cls):
#         print(cls)
#
# a = A()
# a.foo1()
# a.foo2()

# list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list[1])
# print(list[-1])
# totle = "sss +/" \
#         "aaa +/" \
#         "ddd"
#
# tt1 = "ss\nddd\nsss"
# print(totle)
# print(tt1)
# list = ["a", "b", "c", "d", "e", "f"]
# for i in list:
#         print(i)
#         print(list.index(i))

# title_box = ["281", "299", "300", "301", "302"]
# for i in title_box:
#     print(i)
# for i in range(1, 10):
#     print(i)
# import time
#
# now = time.strftime("%Y-%m-%d")
# # 使用预处理语句创建表
# sql = """CREATE TABLE longyi_tjzq_%s (
#          name  CHAR(20) NOT NULL,
#          cj  CHAR(40) NOT NULL,
#          gg CHAR(20) NOT NULL,
#          xq CHAR(20) NOT NULL,
#          price CHAR(20) NOT NULL )""" % now
#
# print(sql)
# import re
# string = "asdfasf   dsfdsa    &1.23 ##$$"
# print(re.findall(r"\d+\.?\d*", string))
# res = [{"group": "2", "id":91149,"number":"KX00150324","name":"消炎镇痛膏","norms":"7*10cm*8片","production":"江西吉安三力制药有限公司"},
#        {"group": "2", "id":10041,"number":"KX00420158","name":"氧氟沙星滴眼液","norms":"8ml：24mg","production":"江苏汉晨药业有限公司"}]
# li = res['norms']
# print(li)
# # dict = li['name']
# # print(dict)
# for i in range(25):
#        print(i)
#
# list1 = ("login/case1", "user/case1")
# for case in list1:  # 从caselist元素组中循环取出case
#        case_name = case.split("/")[-1]
#        print(case_name)

s = "sssss"

s1 = """sdfsaf: %s""" %s
print(s1)

