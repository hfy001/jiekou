import logging
from page_request.pagerequest import Apimethod
from data import  get_api
from common import login
from data import  get_data
import  json


casedate1 = get_api.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet1')
casedate = get_data.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet2')
case=casedate1[0]

# casedate1[0][3]=array[0]      #pysplit.get_cookie.cookie(login)
print(casedate1)

def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))

def get_address():
    aa=login.login1()
    headers = {}
    headers["Cookie"] = aa.get_ssid()
    res = Apimethod(casedate1[0][1], casedate1[0][2], headers, casedate1[0][3],
                    casedate1[0][3])
    resaddress = res.jiekouqingqiu().json()['result'][0]['id']

    print(resaddress)

get_address()