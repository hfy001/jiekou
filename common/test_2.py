# import pytest
# # test_fixture1.py
#
#
# @pytest.fixture(scope='module', autouse=True)
# def test1():
#     print('\n开始执行module')
#
#
# @pytest.fixture(scope='class', autouse=True)
# def test2():
#     print('\n开始执行class')
#
#
# @pytest.fixture(scope='function', autouse=True)
# def test3():
#     print('\n开始执行function')
#
#
# def test_a():
#     print('---用例a执行---')
#
#
# def test_d():
#     print('---用例d执行---')
#
#
# class TestCase:
#
#     def test_b(self):
#         print('---用例b执行---')
#
#     def test_c(self):
#         print('---用例c执行---')
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_fixture1.py'])


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
from common import get_path


path=get_path.get_login()
logging.basicConfig(level=logging.DEBUG)


casedate=canshu1.excelshuju1().openexl(path,'Sheet2')
print(casedate)

@allure.feature('登录')
@pytest.fixture()
@pytest.mark.parametrize("caseid,host,path,headers,params,method,rowid,exceptvalue",casedate)
def login(caseid,host,path,headers,params,method,rowid,exceptvalue):

    get_log('登录').info('当前是第{}条案例'.format(caseid))
    get_log('登录').info('当前测试数据是{}'.format(params))
    res=Apimethod(host,path,headers,eval(params),method)
    rescookid = res.jiekouqingqiu().cookies.get_dict()["ssid"]
    array=pysplit.get_cookie.cookie(rescookid)
    return array


@pytest.fixture()
def get_cookie(request):
    cookie=request.param
    return cookie

casedate1=canshu2.excelshuju2().openexl('E:\pythonbijia\data\case.xlsx','Sheet3')

# casedate1[0][3]=array[0]      #pysplit.get_cookie.cookie(login)
print(casedate1)



@pytest.mark.parametrize("get_cookie", casedate[0], indirect=True)
def test_chakandizhi(get_cookie):
    cookie=get_cookie
    assert  cookie==''