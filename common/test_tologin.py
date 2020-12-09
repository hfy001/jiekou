
#
# from common.get_log import get_log
import json
import logging
import pytest
from page_request.pagerequest import ApiMethod
from data import canshu2
import allure
from common import pysplit
import  re
from mysql import mysqlDB
from common import login
from common import gol
import requests
from common import get_path


path = get_path.get_login()
logging.basicConfig(level=logging.DEBUG)


casedate1 = canshu2.ExcelData2().openexl(path,'Sheet3')

# casedate1[0][3]=array[0]      #pysplit.get_cookie.cookie(login)
print(casedate1[0])


def test_view_address(loginssid):

    headers={}
    headers["Cookie"] = loginssid.get_ssid()
    res1 = requests.get(url=casedate1[0][1] + casedate1[0][2], headers=headers, params=eval(casedate1[0][3]))
    resaddress = res1.json()["result"][0]["address_name"]
    assert resaddress == '上海市浦东新区浦东新区管委会'
    resaddresscode = res1.json()["code"]
    assert resaddresscode == 1

