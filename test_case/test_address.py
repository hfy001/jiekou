import pytest
from src.address  import Address
from data import  get_data
import allure
from common import get_path


path=get_path.get_api()
casedate1 = get_data.ExcelData().openexl(path, 'Sheet2')
case=eval(casedate1[0][2])
print(case)


@allure.epic("药房网APP")
@allure.feature("收货地址模块")
class TestAddress:

    def setup_class(self):
        self.add = Address()

    @allure.step("添加地址")
    @allure.title("添加地址")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[1]])
    def test_addaddress(self,id,api_id,params,rowid,loginssid):
        re = self.add.add_address(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    @allure.step("获取地址")
    @allure.title("获取地址")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[0]])
    def test_getaddress(self,id,api_id,params,rowid,loginssid):
        re = self.add.get_address(eval(params),loginssid)
        resaddress = re.json()["result"][0]["address_name"]
        assert resaddress == '海大富别人高回报看缴费如果您把日军'



    @allure.step("删除地址")
    @allure.title("删除地址")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[2]])
    def test_deleteaddress(self,id,api_id,params,rowid,loginssid):
        addressid=self.add.search_address(eval(params),loginssid)
        parameter=eval(params)
        parameter['id']=addressid
        re = self.add.delete_address(parameter,loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1