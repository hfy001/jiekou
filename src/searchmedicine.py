import json
from data import  get_api
from page_request.pagerequest import Apimethod
from common import get_path


path=get_path.get_api()

# 搜索页面

def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))

#  查询药品 ，关键字联想，搜索品牌，可以不要cookie
class searchmedicine:
    casedate1 = get_api.excelshuju().openexl(path, 'Sheet1')

    def searchmedicine(self,params):
        headers={}
        res = Apimethod(self.casedate1[3][1], self.casedate1[3][2], headers,params,
                        self.casedate1[3][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 关键字联想
    def getassociate(self,params):
        headers={}
        res = Apimethod(self.casedate1[4][1], self.casedate1[4][2], headers,params,
                        self.casedate1[4][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 品牌
    def searchaliascn(self,params):
        headers={}
        res = Apimethod(self.casedate1[5][1], self.casedate1[5][2], headers,params,
                        self.casedate1[5][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 规格
    def searchstandard(self,params):
        headers={}
        res = Apimethod(self.casedate1[6][1], self.casedate1[6][2], headers,params,
                        self.casedate1[6][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 厂家
    def searchtitleabb(self,params):
        headers={}
        res = Apimethod(self.casedate1[7][1], self.casedate1[7][2], headers,params,
                        self.casedate1[7][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress