import pytest
from src.pricecomparison  import pricecomparison
from data import  get_data
import allure
from common import get_path


path=get_path.get_api()
casedate1 = get_data.excelshuju().openexl(path, 'Sheet2')
case=eval(casedate1[0][2])
print(case)


@allure.epic("药房网APP")
@allure.feature('搜索比价模块')
class TestSearchMedicine:

    def setup_class(self):
        self.compare = pricecomparison()

    # 比价商品页 商家列表
    @allure.title("比价页商家商品")
    @allure.step("比价页商家商品")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[8]],)
    def test_pricecompare(self,id,api_id,params,rowid):
        re = self.compare.pricecompare(eval(params))
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    @allure.title("比价商品详细描述")
    @allure.step("比价商品详细描述")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[9]],)
    def test_medicinedetal(self,id,api_id,params,rowid):
        re = self.compare.medicinedetal(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1