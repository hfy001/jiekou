import pytest
from src.person  import person
from data import  get_data
import allure
from common import get_path
from common.id_number import IdNumber
from common.get_name import Full_Name
from common.phone_number import PhoneNumber
import json

path=get_path.get_api()
casedate1 = get_data.ExcelData().openexl(path, 'Sheet2')


@allure.epic("药房网APP")
@allure.feature("我的模块")
class Testperson:

    def setup_class(self):
        self.person = person()
        self.id_number = IdNumber.generate_myid()
        self.name = Full_Name()
        self.phonenum = PhoneNumber()



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
        param = {}
        pa = {}
        pa['real_name'] = self.name.random_name()
        pa['idcard_no'] = self.id_number
        pa['birthday'] ='1961-04-20'
        pa['dict_sex'] =0
        pa['weight'] = 50
        pa['mobile'] = self.phonenum.create_phone()
        pa['dict_bool_medical_history'] = 0
        pa['medical_history'] = ''
        pa['allergy_history'] = ''
        pa['family_history'] = ''
        pa['dict_bool_allergy_history'] = 0
        pa['dict_bool_family_history'] = 0
        pa['dict_bool_liver'] = 0
        pa['dict_bool_renal'] = 0
        pa['dict_bool_nurse'] = 0
        pa['relation_label'] = '家属'
        pa['dict_bool_default'] = 0
        param['data']=json.dumps(pa)

        re = self.person.insert_userdrug(param,loginssid)
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