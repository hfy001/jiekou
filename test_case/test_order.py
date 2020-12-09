import pytest
from src.order  import order
from src.address import Address
from src.cart import cart
from data import  get_data
import allure
from data import get_params
from common import get_path
import json


path=get_path.get_api()
casedate1 = get_data.ExcelData().openexl(path, 'Sheet2')

parameter=get_params.GetParams()



@allure.epic("药房网APP")
@allure.feature('订单模块')
class TestOrder:

    def setup_class(self):
        self.order = order()
        self.add=Address()
        self.cart = cart()


    # # 订单结算页
    @allure.step("订单结算页")
    @allure.title("订单结算页")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[28]])
    def test_getBuy(self,id,api_id,params,rowid,loginssid):
        addressid=self.add.search_address(eval(params),loginssid)
        cartid = self.cart.search_cartid(loginssid)
        parameter=eval(params)
        parameter['addressid']=addressid
        parameter['cartids'] = cartid
        re = self.order.getBuy(parameter,loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    # 创建订单
    @allure.step("创建订单")
    @allure.title("创建订单")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[29]])
    def test_createOrder(self,id,api_id,params,rowid,loginssid):
        addressid=self.add.search_address(eval(params),loginssid)
        cartid = self.cart.search_cartid(loginssid)
        parameter= {}
        parameter['addressid']=addressid
        parameter['cartids'] = cartid
        resp = self.order.getBuy(parameter,loginssid)
        cartids=resp.json()['result']['list'][0]['medicine_list'][0]['id']
        totalprice=resp.json()['result']['list'][0]['store_medicine_price_total']
        packageid=resp.json()['result']['list'][0]['package_list'][0]['id']
        shopid=resp.json()['result']['list'][0]['storeid']
        logisticsid=resp.json()['result']['list'][0]['logistcs_list'][0]['id']


        parms={}
        pa={}
        shop={}
        medicine={}
        medicine['packageid']=packageid
        medicine['logisticsid']=logisticsid
        medicine['couponsid']=''
        medicine['rx_image']=''
        medicine['rx_content']=''
        medicine['no_rx_reason']=''
        medicine['dict_bool_etax']=''
        medicine['invoice_idcard']=''
        medicine['invoice_name']=''
        medicine['invoice_type']=0
        shop[shopid] = medicine
        pa['cartids']=cartids
        pa['packageids']=''
        pa['request_os']='ios'
        pa['use_point']='0'
        pa['platform_coupon_id']=''
        pa['use_balance']='0.00'
        pa['addressid']=addressid
        pa['all_order_price_total']=totalprice
        pa['shop_list']=shop
        pa['medicate_name']=''
        pa['medicate_idcard']=''
        pa['medicate_sex']=''
        pa['rx_info']=None
        parms['data_info']=json.dumps (pa)

        re = self.order.createOrder(parms,loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    # 获取未付款订单信息
    @allure.step("获取未付款订单信息")
    @allure.title("获取未付款订单信息")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[30]])
    def test_NotPayOrders(self,id,api_id,params,rowid,loginssid):
        unpaid_param={'pageIndex':'1',
                      'pageSize':'10',
                      'order_status':'unpaid'}

        unpaid = self.order.getOrderList(unpaid_param, loginssid)
        orderno=unpaid.json()['result']['dataList'][0]['orderno']
        parameter=eval(params)
        parameter['ordernos']=orderno
        re = self.order.NotPayOrders(parameter,loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1



    # 获取订单信息
    @allure.step("获取订单信息")
    @allure.title("获取订单信息")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[31]])
    def test_orderDetail(self,id,api_id,params,rowid,loginssid):
        unpaid_param={'pageIndex':'1',
                      'pageSize':'10'}

        unpaid = self.order.getOrderList(unpaid_param, loginssid)
        orderno=unpaid.json()['result']['dataList'][0]['orderno']
        parameter=eval(params)
        parameter['orderno']=orderno

        re = self.order.orderDetail(parameter,loginssid)
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
        unpaid_param={'pageIndex':'1',
                      'pageSize':'10',
                      'order_status':'unpaid'}

        unpaid = self.order.getOrderList(unpaid_param, loginssid)
        orderno=unpaid.json()['result']['dataList'][0]['orderno']
        parameter=eval(params)
        parameter['ordernoList']=orderno
        re = self.order.getBatchOrderInfo(parameter,loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    # 查看物流
    @allure.step("查看物流")
    @allure.title("查看订单物流信息")
    @pytest.mark.parametrize("id,api_id,params,rowid",parameter.getparams(41))
    def test_getShippingTrace(self,id,api_id,params,rowid,loginssid):
        re = self.order.getShippingTrace(eval(params),loginssid)
        self.resaddresscode = re.json()["code"]
        assert self.resaddresscode == 1

    # # 查看物流
    # @allure.step("查看物流")
    # @allure.title("查看订单物流信息")
    # @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[40]])
    # def test_getShippingTrace(self,id,api_id,params,rowid,loginssid):
    #     re = self.order.getShippingTrace(eval(params),loginssid)
    #     self.resaddresscode = re.json()["code"]
    #     assert self.resaddresscode == 1