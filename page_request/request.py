import requests,json
#from common.log import logger,LOG
import logging

#@logger('requests请求')
class requestlei():
    def __init__(self):
        pass

    def get(self,url,headers):
        try:
            r = requests.get(url,headers)
            r.encoding = 'UTF-8'
            json_response = r.text
            return json_response
        except Exception as e:
            print('get请求出错，出错原因：%s'%e)
            return {}

    def post(self,url,params,headers):
        try:
            r = requests.post(url,data = params,headers = headers)
            json_response = r.text
            return json_response
        except Exception as e:
            print('post请求出错，出错原因：%s'%e)

    def delfile(self,url,hearders):
        try:
            del_word = requests.delete(url,headers = hearders)
            json_response = json.loads(del_word.text)
            return json_response
        except Exception as e:
            print('del请求出错，出错原因：%s'%e)
            return {}

    def putfile(self,url,params):
        try:
            data = json.dumps(params)
            me = requests.put(url,data)
            json_response = json.loads(me.text)
            return json_response
        except Exception as e:
            print('put请求出错，出错原因：%s'%e)
            return json_response