import json
from data import  get_api
from page_request.pagerequest import ApiMethod
from common import get_path


path=get_path.get_api()


def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))


#  购物车
class order:

    casedate1 = get_api.ExcelData().openexl(path, 'Sheet1')

    # 订单结算页
    def getBuy(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = ApiMethod(self.casedate1[28][1], self.casedate1[28][2], headers, params,
                        self.casedate1[28][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 创建订单
    def createOrder(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = ApiMethod(self.casedate1[29][1], self.casedate1[29][2], headers, params,
                        self.casedate1[29][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 获取未付款订单信息
    def NotPayOrders(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = ApiMethod(self.casedate1[30][1], self.casedate1[30][2], headers, params,
                        self.casedate1[30][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 获取订单信息
    def orderDetail(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = ApiMethod(self.casedate1[31][1], self.casedate1[31][2], headers, params,
                        self.casedate1[31][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 获取订单列表
    def getOrderList(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = ApiMethod(self.casedate1[32][1], self.casedate1[32][2], headers, params,
                        self.casedate1[32][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 去付款
    def getBatchOrderInfo(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = ApiMethod(self.casedate1[35][1], self.casedate1[35][2], headers, params,
                        self.casedate1[35][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 查看物流
    def getShippingTrace(self, params, loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = ApiMethod(self.casedate1[40][1], self.casedate1[40][2], headers, params,
                        self.casedate1[40][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress