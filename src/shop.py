import json
from data import  get_api
from page_request.pagerequest import Apimethod




def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))

#  商家
class shop:

    casedate1 = get_api.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet1')

    # 商家包邮活动
    def get_FreePost(self, params,loginssid):
        headers={}
        headers["Cookie"] = loginssid.get_ssid()
        res = Apimethod(self.casedate1[24][1], self.casedate1[24][2], headers, params,
                        self.casedate1[24][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress
