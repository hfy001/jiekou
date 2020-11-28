from common.get_log import get_log
import json
import logging
import pytest
from page_request.pagerequest import Apimethod
from data import canshu1
import allure
from common import pysplit
import  re
from mysql import mysqlDB
from common import get_path


path=get_path.get_login()
logging.basicConfig(level=logging.DEBUG)


casedate=canshu1.excelshuju1().openexl(path,'Sheet2')
print(casedate)

@allure.feature('登录')
@pytest.fixture(scope="module")
@pytest.mark.parametrize("caseid,host,path,headers,params,method,rowid,exceptvalue",casedate)
def login(caseid,host,path,headers,params,method,rowid,exceptvalue):

    get_log('登录').info('当前是第{}条案例'.format(caseid))
    get_log('登录').info('当前测试数据是{}'.format(params))
    res=Apimethod(host,path,headers,eval(params),method)
    rescookid = res.jiekouqingqiu().cookies.get_dict()["ssid"]
    array=re.split('[;]',rescookid)
    return array

print(type(login))

casedate1=canshu1.excelshuju1().openexl('E:\pythonbijia\data\case.xlsx','Sheet3')


casedate1[0][3]=login()
print(casedate1[0][3])


