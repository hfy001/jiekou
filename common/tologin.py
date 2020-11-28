# from common import login
# from common import gol
#
#
#
# def diaoy():
#     aa = login.login()
#     aa.login()
#     print(gol.get_value("ssid"))
#     print(type(gol.get_value("ssid")))
#
#
# if __name__=='__main__':
#     diaoy()



from common.get_log import get_log
import json
import logging
import pytest
from page_request.pagerequest import Apimethod
from data import canshu2
import allure
from common import pysplit
import  re
from mysql import mysqlDB
from common import login
from common import gol
import requests
from common import get_path


path=get_path.get_login()
logging.basicConfig(level=logging.DEBUG)





# @pytest.fixture()
# def loginssid():
#     aa=login.login
#     return aa.login()

class dizhi:
    casedate1 = canshu2.excelshuju2().openexl(path, 'Sheet3')

    # casedate1[0][3]=array[0]      #pysplit.get_cookie.cookie(login)
    print(casedate1[0])

    def chakandizhi(self):


        aa = login.login1()
        aa.get_ssid()
        headers={}
        # headers["Cookie"]=gol.get_value("ssid")
        headers["Cookie"]=aa.get_ssid()
        # res1 = requests.get(url=casedate1[0][1] + casedate1[0][2], headers=headers, params=eval(casedate1[0][3]))
        res = Apimethod(self.casedate1[0][1], self.casedate1[0][2],headers, eval(self.casedate1[0][3]),self.casedate1[0][4])

        resaddress = res.jiekouqingqiu()

        resaddress1 = resaddress.json()["result"][0]["address_name"]

        # sql='SELECT id  FROM user_account_address WHERE accountid={0} LIMIT 1'.format(aa.get_accountid())
        # db = mysqlDB.DB()
        # chaxun=db.query(sql)[0]['id']
        # db.close()
        print(type(self.casedate1[0][3]))

        print(headers)
        print(resaddress.text)
        print(resaddress1)
        # print(type(chaxun))





# gol._init()
# class login():
#     def login(self):
#         response = requests.get(url=casedate[0][1] + casedate[0][2], headers=casedate[0][3], params=casedate[0][4])
#         rescookid = response.cookies.get_dict()
#         gol.set_value("ssid", rescookid)
#         # print(rescookid)

if __name__=='__main__':
    aa=dizhi()
    aa.chakandizhi()