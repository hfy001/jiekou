import pytest
from src.address  import Address
from data import  get_data



casedate1 = get_data.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet2')
case=casedate1[0]
print(case)

# class TestAddress:
#     # casedate1 = get_data.excelshuju().openexl('E:\pythonbijia\data\getapi.xlsx', 'Sheet2')
#     def step_up(self):
#         self.add = address.Address()


@pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[0]])
def test_getaddress(id,api_id,params,rowid,loginssid):
    add = Address()
    re = add.get_address(params,loginssid)
    print(re.text)


params={'pageIndex':'undefined',
'pageSize':'10',
'__client':'app_wx',
'app_version':'4.5.00',
'osVersion':'miniapp',
'deviceName':'iPhone%206s%20Plus%3CiPhone8%2C2%3E',
'os':'ios',
'version':'7.0.17',
'market':'iPhone',
'networkType':'true',
'lat':'31.236276',
'lng':'121.480248',
'user_city_name':'上海',
'user_region_id':'95'}

test_getaddress(1,1,params,1,loginssid)


