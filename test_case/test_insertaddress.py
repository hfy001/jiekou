
import logging
import pytest
from page_request.pagerequest import ApiMethod
from data import canshu2
import allure
from common import get_path


path=get_path.get_login()
logging.basicConfig(level=logging.DEBUG)


casedate1=canshu2.ExcelData2().openexl(path,'Sheet4')

# casedate1[0][3]=array[0]      #pysplit.get_cookie.cookie(login)
print(casedate1)


@allure.epic("药房网APP")
@allure.feature("添加地址模块")
@allure.step("添加地址模块")
@allure.title("添加地址模块")


@pytest.mark.parametrize("caseid1,host,path,params,method,rowid,exceptvalue", casedate1)
def test_insertaddress(caseid1,host,path,params,method,rowid,exceptvalue,loginssid):
        headers={}
        headers["Cookie"]=loginssid.get_ssid()
        res1 = ApiMethod(host, path, headers, eval(params), method)
        resaddresscode = res1.jiekouqingqiu().json()["code"]
        assert resaddresscode == 1

# @pytest.mark.parametrize("caseid1,host,path,params,method,rowid,exceptvalue", casedate1)
# def test_insertaddress(self,caseid1,host,path,params,method,rowid,exceptvalue,loginssid):
#         headers={}
#         headers["Cookie"]=loginssid.get_ssid()
#         res1 = Apimethod(host, path, headers, eval(params), method)
#         self.resaddresscode = res1.jiekouqingqiu().json()["code"]
#         assert self.resaddresscode == 1