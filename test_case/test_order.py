import pytest
from src.order  import order
from data import  get_data
import allure
from data import get_params
from common import get_path


path=get_path.get_api()
casedate1 = get_data.excelshuju().openexl(path, 'Sheet2')

parameter=get_params.get_params()



@allure.epic("药房网APP")
@allure.feature('订单模块')
class TestOrder:

    def setup_class(self):
        self.order = order()
    # # 订单结算页
    @allure.step("订单结算页")
    @allure.title("订单结算页")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[28]])
    def test_getBuy(self,id,api_id,params,rowid,loginssid):
        re = self.order.getBuy(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    # 创建订单
    @allure.step("创建订单")
    @allure.title("创建订单")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[29]])
    def test_createOrder(self,id,api_id,params,rowid,loginssid):
        re = self.order.createOrder(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1


    # 获取未付款订单信息
    @allure.step("获取未付款订单信息")
    @allure.title("获取未付款订单信息")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[31]])
    def test_orderDetail(self,id,api_id,params,rowid,loginssid):
        re = self.order.orderDetail(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1


    # 获取订单列表
    @allure.step("获取订单列表")
    @allure.title("获取订单列表")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[32]])
    def test_getOrderList(self,id,api_id,params,rowid,loginssid):
        re = self.order.getOrderList(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1


    # 发起付款，获取需要支付的sdk
    @allure.step("发起付款，获取需要支付的sdk")
    @allure.title("发起付款，获取需要支付的sdk")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[35]])
    def test_getBatchOrderInfo(self,id,api_id,params,rowid,loginssid):
        re = self.order.getBatchOrderInfo(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    # # 查看物流
    # @allure.step("查看物流")
    # @allure.title("查看订单物流信息")
    # @pytest.mark.parametrize("id,api_id,params,rowid",parameter.get_params(41))
    # def test_getShippingTrace(self,id,api_id,params,rowid,loginssid):
    #     re = self.order.getBatchOrderInfo(eval(params),loginssid)
    #     self.resaddresscode = re.json()["code"]
    #     assert self.resaddresscode == 1

    # 查看物流
    @allure.step("查看物流")
    @allure.title("查看订单物流信息")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[42]])
    def test_getShippingTrace(self,id,api_id,params,rowid,loginssid):
        re = self.order.getBatchOrderInfo(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1