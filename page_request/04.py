#coding:utf-8
import  json
from common.get_log import logs,get_log
from data import canshu2
fruits='{"apple":1,"pear":2}'
text=json.loads(fruits)
print(text)
get_log('test').info('测试一下')


casedate1=canshu2.excelshuju2().openexl('E:\pythonbijia\data\case.xlsx','Sheet4')

# casedate1[0][3]=array[0]      #pysplit.get_cookie.cookie(login)
print(casedate1)