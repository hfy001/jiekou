from common.get_log import get_log
import json
import logging
import pytest
from page_request.pagerequest import Apimethod
from data import canshu1
from data import canshu2
import allure
from common import pysplit
import  re
from mysql import mysqlDB
from common import login
from common import gol

logging.basicConfig(level=logging.DEBUG)


casedate1=canshu2.excelshuju2().openexl('E:\pythonbijia\data\case.xlsx','Sheet3')

# casedate1[0][3]=array[0]      #pysplit.get_cookie.cookie(login)
print(casedate1)

@allure.epic("药房网APP")
@allure.feature("查看地址模块")
@allure.step("查看地址模块")
@allure.title("查看地址模块")
@pytest.mark.parametrize("caseid1,host,path,params,method,rowid,exceptvalue", casedate1)
def test_chakandizhi(caseid1,host,path,params,method,rowid,exceptvalue,loginssid):
    headers={}
    headers["Cookie"]=loginssid.get_ssid()
    res1 = Apimethod(host, path, headers, eval(params), method)
    resaddress = res1.jiekouqingqiu().json()["result"][0]["address_name"]
    assert resaddress=='海大富别人高回报看缴费如果您把日军'