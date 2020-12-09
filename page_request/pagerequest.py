# from page_request.request import requestlei
import requests


class ApiMethod():

    def __init__(self, host,path,headers,params,method):
        self.host = host
        self.path = path
        self.params=params
        self.method = method
        self.headers = headers

    def jiekouqingqiu(self):
        if self.method=='get':
            try:

                response=requests.get(url=self.host+self.path,headers=self.headers,params=self.params)
                return response
            except Exception as e:
                print('get请求出错，出错原因：%s' % e)
                return {}

        elif self.method=='post':
            try:
                response=requests.get(url=self.host+self.path,headers=self.headers,params=self.params)
                return response
            except Exception as e:
                print('get请求出错，出错原因：%s' % e)
                return {}

    def getstatus(self):
        statuscode = self.jiekouqingqiu().status_code
        return statuscode

    def getcode(self):
        rescode=self.jiekouqingqiu().json()["code"]
        return rescode

    def getrowcount(self):
        resrowcount=self.jiekouqingqiu().json()["result"]["rowCount"]
        return resrowcount

