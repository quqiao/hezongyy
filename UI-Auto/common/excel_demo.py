# -*- coding: utf-8 -*-
__author__ = 'quqiao'

import xlrd

"""excel基本操作方法"""
# data = xlrd.open_workbook('test.xlsx')  # 打开Excel表格，参数是文件路径
# table1 = data.sheets()[0]  # 通过索引顺序获取
# table2 = data.sheet_by_index(0)  # 通过索引顺序获取
# table3 = data.sheet_by_name('Sheet1')  # 通过名称获取
# nrows = table1.nrows  # 获取总行数
# ncols = table2.ncols  # 获取总列数
# print(table1.row_values(0))  # 获取第一行值，参数是第几行
# print(table1.col_values(0))  # 获取第一列值，参数是第几行

""" excel存放数据
    在excel中存放数据，第一行为标题，也就是对应字典里面的key值，如：username,password
    如果excel数据中有纯数字的一定要右键>设置单元格格式>文本格式，要不然读取的数据是浮点数
"""

"""封装读取方法
    最终读取的数据是多个字典的list类型数据，第一行数据就是字典里的key值，从第二行开始一一对应value值
"""
class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)  # 获取第一行作为key值
        self.rowNum = self.table.nrows  # 获取总行数
        self.colNum = self.table.ncols  # 获取总列数

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                values = self.table.row_values(j)  # 从第二行取对应values值
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
if __name__ == "__main__":
    filepath = "F:\\pyhcarm\\hezongyy\\UI-Auto\\common\\test_excel.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())
