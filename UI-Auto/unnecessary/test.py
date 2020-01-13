#coding:utf-8

class A(object):
    def foo1(self):
        print(self)

    @classmethod
    def foo2(cls):
        print(cls)

a = A()
a.foo1()
a.foo2()