# from common.get_log import get_log
import json
import logging
import pytest
from page_request.pagerequest import Apimethod
from data import canshu1
from write_excel.wrexcel import writeex
from urllib import  parse
import allure
from mysql import mysqlDB
from common import get_path


path=get_path.get_login()



logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

logging.basicConfig(level=logging.DEBUG)


casedate=canshu1.excelshuju1().openexl(path,'Sheet2')

print(casedate)



@allure.epic("药房网APP")
@allure.feature('登录模块')
@allure.title('登录模块')
@allure.step('登录模块')
@pytest.mark.parametrize("caseid,host,path,headers,params,method,rowid,exceptvalue",casedate)
def test_case02(caseid,host,path,headers,params,method,rowid,exceptvalue):

    # get_log('登录').info('当前是第{}条案例'.format(caseid))
    # get_log('登录').info('当前测试数据是{}'.format(params))



    res=Apimethod(host,path,headers,eval(params),method)
    print(res)
    resstatuscode=res.getstatus()
    rescode=res.getcode()
    resuserid=res.jiekouqingqiu().json()["result"]["id"]
    rescookid = res.jiekouqingqiu().cookies.get_dict()["ssid"]





    b=eval(params)['userName']

    sql = """SELECT id from user_account where account_name='{0}';""".format(b)

    db = mysqlDB.DB()
    userid=db.query(sql)[0]['id']
    db.close()
    assert resstatuscode==200,"判断响应code为 %s" % resstatuscode
    assert rescode==eval(exceptvalue)['code'], "判断code是不是=1,code的值为 %d" % rescode
    assert resuserid==userid
