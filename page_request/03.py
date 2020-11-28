import json
from data import canshu
from common import get_cwd
import os


path = get_cwd.get_cwd()
excel_path1 = os.path.join(path, 'data/case.xlsx')

print(excel_path1)

casedate=canshu.excelshuju().openexl(excel_path1)
print(casedate)

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







