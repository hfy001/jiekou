import pytest
from src.searchmedicine  import searchmedicine
from data import  get_data
import allure
from common import get_path


path=get_path.get_api()
casedate1 = get_data.excelshuju().openexl(path, 'Sheet2')
case=eval(casedate1[0][2])
print(case)


@allure.epic("药房网APP")
@allure.feature('搜索模块')
class TestSearchMedicine:

    def setup_class(self):
        self.search = searchmedicine()

    # 查询药品
    @allure.title("查询药品")
    @allure.step("查询药品")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[3]],)
    def test_searchmedicine(self,id,api_id,params,rowid):
        re = self.search.searchmedicine(eval(params))
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    # 关键字联想
    @allure.title("关键字联想")
    @allure.step("关键字联想")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[4]],)
    def test_getassociate(self,id,api_id,params,rowid):
        re = self.search.getassociate(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1

    # 按照品牌搜索
    @allure.title("品牌搜索")
    @allure.step("品牌搜索")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[5]],)
    def test_searchaliascn(self,id,api_id,params,rowid):
        re = self.search.searchaliascn(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1

    # 规格
    @allure.title("规格搜索")
    @allure.step("规格搜索")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[6]],)
    def test_searchstandard(self,id,api_id,params,rowid):
        re = self.search.searchstandard(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1

    # 厂家
    @allure.title("厂家搜索")
    @allure.step("厂家搜索")
    @pytest.mark.parametrize("id,api_id,params,rowid", [casedate1[7]],)
    def test_searchtitleabb(self,id,api_id,params,rowid):
        re = self.search.searchtitleabb(eval(params))
        self.resaddresscode = re.json()['code']
        assert self.resaddresscode == 1