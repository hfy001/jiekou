import pytest
from src.favorite  import favorite
from data import  get_data
import allure
from mysql import mysqlDB
from common import get_path


path=get_path.get_api()
casedate1 = get_data.excelshuju().openexl(path, 'Sheet2')
case=eval(casedate1[0][2])
print(case)


@allure.epic("药房网APP")
@allure.feature("查看地址模块")
class TestFavorite:

    def setup_class(self):
        self.favo = favorite()

    # 收藏药品
    @allure.step("收藏药品")
    @allure.title("收藏药品")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[17]])
    def test_collect(self,id,api_id,params,rowid,loginssid):
        re = self.favo.CollectMedicine(eval(params),loginssid)
        self.recode = re.json()["code"]
        assert self.recode == 1


    # 取消收藏药品
    @allure.step("取消收藏药品")
    @allure.title("取消收藏药品")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[18]])
    def test_CancelCollect(self,id,api_id,params,rowid,loginssid):
        re = self.favo.CancelCollectMedicine(eval(params),loginssid)
        self.recode = re.json()["code"]
        assert self.recode == 1


    # 收藏商家
    @allure.step("收藏商家")
    @allure.title("收藏商家")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[20]])
    def test_CollectStore(self,id,api_id,params,rowid,loginssid):
        re = self.favo.CollectStore(eval(params),loginssid)
        self.recode = re.json()["code"]
        assert self.recode == 1


    # 取消收藏商家
    @allure.step("取消收藏商家")
    @allure.title("取消收藏商家")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[21]])
    def test_CancelCollectStore(self,id,api_id,params,rowid,loginssid):
        re = self.favo.CancelCollectStore(eval(params),loginssid)
        self.recode = re.json()["code"]
        assert self.recode == 1