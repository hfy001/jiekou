import json
from data import  get_api
from common import login
from data import canshu2
from page_request.pagerequest import Apimethod
from common import get_path


path=get_path.get_api()

def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))

# 收货地址 添加、查看列表、删除

class Address:

    casedate1 = get_api.excelshuju().openexl(path, 'Sheet1')

    def get_address(self,params,loginssid):
        headers={}
        headers["Cookie"]=loginssid.get_ssid()
        res = Apimethod(self.casedate1[0][1], self.casedate1[0][2], headers, params,
                        self.casedate1[0][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    def add_address(self,params,loginssid):
        headers = {}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[1][1], self.casedate1[1][2], headers, params, self.casedate1[1][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        self.addressid=resaddress.json()['result']
        return resaddress



    # 需要返回一个addressid 用于删除功能
    def search_address(self,params,loginssid):
        headers = {}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[0][1], self.casedate1[0][2], headers, params,
                        self.casedate1[0][3])
        resaddress = res.jiekouqingqiu()
        addressid=resaddress.json()['result'][0]['id']
        return addressid

    def delete_address(self,params,loginssid):
        headers = {}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[2][1], self.casedate1[2][2], headers, params, self.casedate1[2][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

