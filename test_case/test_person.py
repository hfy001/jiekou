import pytest
from src.person  import person
from data import  get_data
import allure

casedate1 = get_data.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet2')
case=eval(casedate1[0][2])
print(case)

@allure.epic("药房网APP")
@allure.feature("我的模块")
class Testperson:

    def setup_class(self):
        self.person = person()



    # 我的页面
    @allure.step("我的页面")
    @allure.title("我的页面")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[33]])
    def test_getAccountCenter(self,id,api_id,params,rowid,loginssid):
        re = self.person.get_AccountCenter(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    # 获取我的积分
    @allure.step("获取我的积分")
    @allure.title("获取我的积分")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[34]])
    def test_getValidPoint(self,id,api_id,params,rowid,loginssid):
        re = self.person.get_ValidPoint(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1


    # 获取用户实名信息
    @allure.step("获取用户实名信息")
    @allure.title("获取用户实名信息")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[36]])
    def test_getCertInfoForDrug(self,id,api_id,params,rowid,loginssid):
        re = self.person.get_CertInfoForDrug(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    # 新增用药人
    @allure.step("新增用药人")
    @allure.title("新增用药人")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[37]])
    def test_insertuserdrug(self,id,api_id,params,rowid,loginssid):
        re = self.person.insert_userdrug(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    # 获取未读数量
    @allure.step("新增用药人")
    @allure.title("新增用药人")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[39]])
    def test_getNotReadCount(self,id,api_id,params,rowid,loginssid):
        re = self.person.get_NotReadCount(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1