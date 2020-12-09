import json
from data import  get_api
from page_request.pagerequest import ApiMethod
from common import get_path


path=get_path.get_api()


# 搜索页面
def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))


#  商家药品详情页，可以不要cookie
class storemedicine:
    casedate1 = get_api.ExcelData().openexl(path, 'Sheet1')

    def storemedicine(self,params):
        headers={}
        res = ApiMethod(self.casedate1[11][1], self.casedate1[11][2], headers, params,
                        self.casedate1[11][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 商家详情页
    def shopinfo(self,params):
        headers={}
        res = ApiMethod(self.casedate1[12][1], self.casedate1[12][2], headers, params,
                        self.casedate1[12][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 商家优选商品
    def StoreMedicineTop(self,params):
        headers={}
        res = ApiMethod(self.casedate1[13][1], self.casedate1[13][2], headers, params,
                        self.casedate1[13][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 商家资质和外景
    def ShopQualification(self,params):
        headers = {}
        res = ApiMethod(self.casedate1[14][1], self.casedate1[14][2], headers, params,
                        self.casedate1[14][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # APP首页底部资质图片
    def BannerBottom(self,params):
        headers = {}
        res = ApiMethod(self.casedate1[15][1], self.casedate1[15][2], headers, params,
                        self.casedate1[15][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress

    # 商家药品分类
    def MedicineCategory(self,params):
        headers = {}
        res = ApiMethod(self.casedate1[16][1], self.casedate1[16][2], headers, params,
                        self.casedate1[16][3])
        resaddress = res.jiekouqingqiu()
        pretty(resaddress)
        return resaddress