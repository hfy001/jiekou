import pytest
from src.shop  import shop
from data import  get_data
import allure

casedate1 = get_data.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet2')
case=eval(casedate1[0][2])
print(case)


@allure.epic("药房网APP")
@allure.feature('店铺模块')
class Testshop:

    def setup_class(self):
        self.shop = shop()

    @allure.title("店铺包邮活动")
    @allure.step("店铺包邮活动")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[24]])
    def test_FreePost(self,id,api_id,params,rowid,loginssid):
        re = self.shop.get_FreePost(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1