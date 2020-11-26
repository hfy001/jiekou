import json
from data import  get_api
from page_request.pagerequest import Apimethod




def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))

#  购物车
class cart:

    casedate1 = get_api.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet1')

    # 购物车数量
    def get_cartcount(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[10][1], self.casedate1[10][2], headers, params,
                        self.casedate1[10][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 加入购物车
    def addCart(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[19][1], self.casedate1[19][2], headers, params,
                        self.casedate1[19][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 购物车信息
    def get_Cart(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[22][1], self.casedate1[22][2], headers, params,
                        self.casedate1[22][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 购物车页面精选商品
    def get_TopVisitMedicine(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[23][1], self.casedate1[23][2], headers, params,
                        self.casedate1[23][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 修改购物车数量
    def editCart(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[25][1], self.casedate1[25][2], headers, params,
                        self.casedate1[25][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 移入收藏夹
    def moveToFavorite(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[26][1], self.casedate1[26][2], headers, params,
                        self.casedate1[26][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 删除购物车商品
    def deleteCartGoods(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[27][1], self.casedate1[27][2], headers, params,
                        self.casedate1[27][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress