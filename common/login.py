from common.get_log import get_log
import requests
import logging
import pytest
from page_request.pagerequest import Apimethod
from data import canshu1
from common import pysplit
from common import gol
import re
from mysql import mysqlDB

# fruits='{"apple":1,"pear":2}'
# text=json.loads(fruits)
# print(text)
# get_log('test').info('测试一下')



logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

logging.basicConfig(level=logging.DEBUG)


casedate=canshu1.excelshuju1().openexl('E:\pythonbijia\data\case.xlsx','Sheet2')

print(casedate)


# @pytest.mark.parametrize("caseid,host,path,headers,params,method,rowid,exceptvalue",casedate)
# class logincla():
#     def login(caseid,host,path,headers,params,method,rowid,exceptvalue):
#
#         get_log('登录').info('当前是第{}条案例'.format(caseid))
#         get_log('登录').info('当前测试数据是{}'.format(params))
#
#
#
#         res=Apimethod(host,path,headers,eval(params),method)
#         print(res)
#         resstatuscode=res.getstatus()
#         rescode=res.getcode()
#         resuserid=res.jiekouqingqiu().json()["result"]["id"]
#         rescookid = res.jiekouqingqiu().cookies.get_dict()
#
#         array=pysplit.get_cookie.cookie(rescookid)
#         gol.set_value("ssid",rescookid)
#
#         print(array)

gol._init()
class login1():
    def get_ssid(self):
        response = requests.get(url=casedate[0][1] + casedate[0][2], headers=casedate[0][3], params=eval(casedate[0][4]))
        print(response.text)
        rescookid = response.headers['Set-Cookie']
        gol.set_value("ssid", rescookid)
        print(rescookid)
        return rescookid


    def get_accountid(self):
        response = requests.get(url=casedate[0][1] + casedate[0][2], headers=casedate[0][3], params=eval(casedate[0][4]))

        accountid=response.json()['result']['id']

        print(accountid)
        return accountid




if __name__=='__main__':

    aa=login1()
    aa.get_ssid()
    aa.get_accountid()
    print(gol.get_value("ssid"))

