import json
from data import  get_api
from page_request.pagerequest import Apimethod


def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))

# 收货地址 添加、查看列表、删除

class person:

    casedate1 = get_api.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet1')

    # 我的页面
    def get_AccountCenter(self,params,loginssid):
        headers={}
        headers["Cookie"]=loginssid.get_ssid()
        res = Apimethod(self.casedate1[33][1], self.casedate1[33][2], headers, params,
                        self.casedate1[33][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    #获取积分
    def get_ValidPoint(self,params,loginssid):
        headers={}
        headers["Cookie"]=loginssid.get_ssid()
        res = Apimethod(self.casedate1[34][1], self.casedate1[34][2], headers, params,
                        self.casedate1[34][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress


    #获取用户实名信息
    def get_CertInfoForDrug(self,params,loginssid):
        headers={}
        headers["Cookie"]=loginssid.get_ssid()
        res = Apimethod(self.casedate1[36][1], self.casedate1[36][2], headers, params,
                        self.casedate1[36][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 新增用药人
    def insert_userdrug(self,params,loginssid):
        headers={}
        headers["Cookie"]=loginssid.get_ssid()
        res = Apimethod(self.casedate1[37][1], self.casedate1[37][2], headers, params,
                        self.casedate1[37][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 获取未读数量
    def get_NotReadCount(self,params,loginssid):
        headers={}
        headers["Cookie"]=loginssid.get_ssid()
        res = Apimethod(self.casedate1[39][1], self.casedate1[39][2], headers, params,
                        self.casedate1[39][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress