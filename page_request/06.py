import logging
import pytest
from page_request.pagerequest import Apimethod
from data import canshu1
from requests.cookies import RequestsCookieJar
import requests
import re

from write_excel.wrexcel import writeex
from urllib import  parse
import allure
from mysql import mysqlDB

host='http://192.168.2.252:18080/4000/4000/0/'
path='guest.account.login'
headers={}
params={'userName':'啦啦哈哈',
'password':'abc123',
'login_type':'2'}
method='get'

res=Apimethod(host,path,headers,params,method)
# print(res.jiekouqingqiu().text)
resstatuscode=res.getstatus()
rescode=res.getcode()
resuserid=res.jiekouqingqiu().json()["result"]["id"]
rescookid1=res.jiekouqingqiu().headers['Set-Cookie']

array = re.split('[;]',rescookid1)


rescookid2=res.jiekouqingqiu().cookies.get_dict()
rescookid=res.jiekouqingqiu().cookies.get_dict()["ssid"]
# print(resuserid)
print(type(rescookid1))
print(rescookid1)
print(rescookid2)
print(rescookid)
print(array[0])




# casedate1=canshu1.excelshuju1().openexl('E:\pythonbijia\data\case.xlsx','Sheet3')
# print(type(casedate1))
# print(casedate1)
# cookie={}
# cookie['Cookie']=array[0]
# casedate1[0][3]= cookie
#
# print(casedate1[0][3])


