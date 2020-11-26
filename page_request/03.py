import json
from data import canshu

casedate=canshu.excelshuju().openexl('E:\pythonbijia\data\canshu1.xlsx')
# print(casedate)

def medicineid():
    for i in  range(0,len(casedate)):
        a=casedate[i][3]
        # print(type(a))
        b=eval(a)
        # print(type(b))
        # print(b['conditions'])
        c=b['conditions']
        # print(type(c))
        print(c['medicineid'])
    return  c['medicineid']
