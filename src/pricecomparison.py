import json
from data import  get_api
from page_request.pagerequest import Apimethod
from common import get_path


path=get_path.get_api()

# 比价页面

def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))

#  比价商品页 商家列表  可以不要cookie
class pricecomparison:
    casedate1 = get_api.excelshuju().openexl(path, 'Sheet1')


    # 比价页商家商品
    def pricecompare(self,params):
        headers={}
        res = Apimethod(self.casedate1[8][1], self.casedate1[8][2], headers,params,
                        self.casedate1[8][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress


    # 比价商品详细描述
    def medicinedetal(self,params):
        headers={}
        res = Apimethod(self.casedate1[9][1], self.casedate1[9][2], headers,params,
                        self.casedate1[9][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

