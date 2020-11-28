import json
from data import  get_api
from page_request.pagerequest import Apimethod
from common import get_path


path=get_path.get_api()



def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))

#  购物车
class favorite:

    casedate1 = get_api.excelshuju().openexl(path, 'Sheet1')

    # 收藏药品
    def CollectMedicine(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[17][1], self.casedate1[17][2], headers, params,
                        self.casedate1[17][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 取消收藏药品
    def CancelCollectMedicine(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[18][1], self.casedate1[18][2], headers, params,
                        self.casedate1[18][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 收藏商家
    def CollectStore(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[20][1], self.casedate1[20][2], headers, params,
                        self.casedate1[20][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 取消收藏商家
    def CancelCollectStore(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[21][1], self.casedate1[21][2], headers, params,
                        self.casedate1[21][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress