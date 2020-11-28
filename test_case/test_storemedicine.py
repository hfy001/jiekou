import pytest
from src.storemedicine  import storemedicine
from data import  get_data
import  allure
from common import get_path


path=get_path.get_api()
casedate1 = get_data.excelshuju().openexl(path, 'Sheet2')
case=eval(casedate1[0][2])
print(case)



@allure.epic("药房网APP")
@allure.feature('店铺模块')
class TestSearchMedicine:

    def setup_class(self):
        self.shopmedicine = storemedicine()

    # 商家药品详情页
    @allure.step("商家药品详情页")
    @allure.title("商家药品详情页")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[11]],)
    def test_pricecompare(self,id,api_id,params,rowid):
        re = self.shopmedicine.storemedicine(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1

    # 商家详情页
    @allure.step("商家详情页")
    @allure.title("商家详情页")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[12]],)
    def test_shopinfo(self,id,api_id,params,rowid):
        re = self.shopmedicine.shopinfo(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1

    # 商家优选商品
    @allure.step("商家优选商品")
    @allure.title("商家优选商品")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[13]],)
    def test_StoreMedicineTop(self, id, api_id, params, rowid):
        re = self.shopmedicine.StoreMedicineTop(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1

    # 商家资质和外景
    @allure.step("商家资质和外景")
    @allure.title("商家资质和外景")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[14]],)
    def test_ShopQualification(self, id, api_id, params, rowid):
        re = self.shopmedicine.ShopQualification(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1

    # APP首页底部资质图片
    @allure.step("APP首页底部资质图片")
    @allure.title("APP首页底部资质图片")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[15]],)
    def test_BannerBottom(self, id, api_id, params, rowid):
        re = self.shopmedicine.BannerBottom(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1

    # 商家药品分类
    @allure.step("商家药品分类")
    @allure.title("商家药品分类")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[17]],)
    def test_MedicineCategory(self, id, api_id, params, rowid):
        re = self.shopmedicine.MedicineCategory(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1