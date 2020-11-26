
import logging
import pytest
from page_request.pagerequest import Apimethod
from data import canshu2
from mysql import mysqlDB
import allure

logging.basicConfig(level=logging.DEBUG)


casedate1=canshu2.excelshuju2().openexl('E:\pythonbijia\data\case.xlsx','Sheet5')

# casedate1[0][3]=array[0]      #pysplit.get_cookie.cookie(login)
print(casedate1)
#  根据登录接口返回的 accountid，在数据库user_account_address中查询，删除第一条记录


@allure.epic("药房网APP")
@allure.feature("删除地址模块")
@allure.step("删除地址模块")
@allure.title("删除地址模块")
@pytest.mark.parametrize("caseid1,host,path,params,method,rowid,exceptvalue", casedate1)
def test_tianjiadizhi(caseid1,host,path,params,method,rowid,exceptvalue,loginssid):
    headers={}
    headers["Cookie"]=loginssid.get_ssid()
    sql='SELECT id  FROM user_account_address WHERE accountid={0} LIMIT 1'.format(loginssid.get_accountid())
    db = mysqlDB.DB()
    addressid = db.query(sql)[0]['id']
    db.close()
    param=eval(params)
    param['id']=addressid
    res1 = Apimethod(host, path, headers, param, method)
    resaddress = res1.jiekouqingqiu().json()["code"]
    print('param:',param)
    assert resaddress==1