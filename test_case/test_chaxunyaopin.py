import logging
import pytest
from page_request.pagerequest import ApiMethod
from data import canshu
import allure

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

logging.basicConfig(level=logging.DEBUG)
from common import get_path


path=get_path.get_login()


casedate=canshu.ExcelData().openexl(path)

print(casedate)

@allure.epic("药房网APP")
@allure.feature("查询药品模块")
@allure.step("查询药品模块")
@allure.title("查询药品模块")
@pytest.mark.parametrize("caseID,host,path,headers,params,method,rowid",casedate)
def test_case02(caseID,host,path,headers,params,method,rowid):
    log = logging.getLogger('test_case03')

    # response=requests.get(url=host+path,headers=eval(headers),params=eval(params))

    res=ApiMethod(host,path,eval(headers),eval(params),method)
    print(res)
    resstatuscode=res.getstatus()
    rescode=res.getcode()

    assert resstatuscode==200,"判断响应code为 %s" % resstatuscode
    assert rescode == 1, "判断code是不是=1,code的值为 %d" % rescode