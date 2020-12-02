# from common.get_log import get_log
# import json
# import logging
# import pytest
# from page_request.pagerequest import Apimethod
# from data import canshu1
# from write_excel.wrexcel import writeex
# from urllib import  parse
# import allure
#
#
#
#
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')
#
# logging.basicConfig(level=logging.DEBUG)
#
#
# casedate=canshu1.excelshuju1().openexl('E:\pythonbijia\data\case.xlsx','Sheet1')
#
# print(casedate)
#
# @allure.feature('查询药品')
# @pytest.mark.parametrize("caseid,host,path,headers,params,method,rowid,exceptvalue",casedate)
# def test_case02(caseid,host,path,headers,params,method,rowid,exceptvalue):
#
#     get_log('查询药品').info('当前是第{}条案例'.format(caseid))
#     get_log('查询药品').info('当前测试数据是{}'.format(params))
#
#
#     res=Apimethod(host,path,eval(headers),eval(params),method)
#     print(res)
#     resstatuscode=res.getstatus()
#     rescode=res.getcode()
#
#     assert resstatuscode==200,"判断响应code为 %s" % resstatuscode
#     assert rescode == 1, "判断code是不是=1,code的值为 %d" % rescode
#     assert rescode==eval(exceptvalue)['code']
#
#
#
#
#
