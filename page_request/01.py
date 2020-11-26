import logging
import json
import pytest
import requests
# from page_request.pagerequest import ApiTest
from page_request.pagerequest import Apimethod
from mysql import mysqlDB

# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')

from data import canshu
from data import canshu



logging.basicConfig(level=logging.DEBUG)

# @pytest.mark.parametrize("host,path,headers,params,method",casedate)
# def test_case02(host,path,headers,params,method):
#     log = logging.getLogger('test_case02')
#
#     # response=requests.get(url=host+path,headers=eval(headers),params=eval(params))
#
#     res=Apimethod(host,path,headers,params,method)
#     print(res)
#     resstatuscode=res.getstatus()
#     rescode=res.getcode()
#
#     assert resstatuscode==200,"判断响应code为 %s" % resstatuscode
#     assert rescode == 1, "判断code是不是=1,code的值为 %d" % rescode


casedate=canshu.excelshuju().openexl('E:\pythonbijia\data\case.xlsx')

print(casedate)

host1 = 'http://192.168.2.252:18080'
path1 ='/4000/4000/0/guest.medicine.getSearchPageData'

headers1 = {
  'Content-Type': 'application/x-www-form-urlencoded'
}


params1={'keywords':'感冒灵'}
method1='get'

abv=Apimethod(host1,path1,headers1,params1,method1)
print(abv.jiekouqingqiu().text)
print(abv.jiekouqingqiu().url)
print(abv.getstatus())
print(abv.getcode())


# sql ="select * from sto_store limit 1"
# db=mysqlDB.DB()
# db.query(sql)
# db.close()

a=casedate[1][3]
print(type(a))
b= eval(a)
print(type(b))
print(b['keywords'])

for  i in range(0,len(casedate)):
  aa=casedate[i][3]
  bb=eval(aa)
  print(bb['keywords'])


# for i  in range()