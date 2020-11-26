import xlrd
from xlutils.copy import copy


# file= 'E:\pythonbijia\data\canshu1.xlsx'
# data= xlrd.open_workbook(file)
# print(type(data))
#
# data_copy= copy(data)
# print(type(data_copy))
#
# sheet_copy=data_copy.get_sheet(0)
# print(type(sheet_copy))
#
# sheet_copy.write(1,11,'测试内容')
# data_copy.save(file)


class writeex:
    def write_value(self,file,row,col,value):
        data = xlrd.open_workbook(file)
        data_copy = copy(data)
        sheet_copy = data_copy.get_sheet(0)
        sheet_copy.write(row,col,value)
        data_copy.save(file)