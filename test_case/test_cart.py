import pytest
from src.cart import cart
from data import get_data
from mysql import mysqlDB
import allure
from common import get_path


path=get_path.get_api()
casedate1 = get_data.ExcelData().openexl(path, 'Sheet2')
case = eval(casedate1[0][2])
print(case)



@allure.epic("药房网APP")
@allure.feature("购物车模块")
class TestCart:

    def setup_class(self):
        self.cart = cart()

    @allure.step("购物车数量")
    @allure.title("购物车数量")
    # 购物车数量
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[10]])
    def test_cartcount(self, id, api_id, params, rowid, loginssid):
        re = self.cart.get_cartcount(params,loginssid)
        cartacount = re.json()["result"]['cartCount']

        sql = '''SELECT SUM(b.amount) as sumcart from stk_store_medicine a
                 LEFT JOIN sell_customer_cart b on a.id=b.store_medicineid
                 WHERE b.accountid={0}
                 and a.dict_store_medicine_status>=1'''.format(loginssid.get_accountid())
        db = mysqlDB.DB()
        sumcart = db.query(sql)[0]['sumcart']
        db.close()

        assert cartacount == sumcart


    # 加入购物车
    @allure.step("加入购物车")
    @allure.title("加入购物车")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[19]])
    def test_addCart(self,id,api_id,params,rowid,loginssid):
        re = self.cart.addCart(eval(params),loginssid)
        cart = re.json()["result"]['msg']
        assert cart=='加入购物车成功'


    # 购物车信息
    @allure.step("购物车信息")
    @allure.title("购物车信息")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[22]])
    def test_getCart(self,id,api_id,params,rowid,loginssid):
        re = self.cart.get_Cart(eval(params),loginssid)
        cartcode = re.json()["code"]
        assert cartcode==1


    # 购物车页面精选商品
    @allure.step("购物车页面精选商品")
    @allure.title("购物车页面精选商品")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[23]])
    def test_getTopVisitMedicine(self,id,api_id,params,rowid,loginssid):
        re = self.cart.get_TopVisitMedicine(eval(params),loginssid)
        cartcode = re.json()["code"]
        assert cartcode==1


    # 修改购物车数量
    @allure.step("修改购物车数量")
    @allure.title("修改购物车数量")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[25]])
    def test_editCart(self,id,api_id,params,rowid,loginssid):
        cartid=self.cart.search_cartid(loginssid)
        paramter=eval(params)
        paramter['cartId']=cartid
        re = self.cart.editCart(paramter,loginssid)
        cartcode = re.json()["code"]
        assert cartcode==1

    # 移入收藏夹
    @allure.step("移入收藏夹")
    @allure.title("移入收藏夹")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[26]])
    def test_moveToFavorite(self,id,api_id,params,rowid,loginssid):
        cartid=self.cart.search_cartList(loginssid)
        paramter=eval(params)
        print(cartid)
        paramter['cartidList']=cartid
        re = self.cart.moveToFavorite(paramter,loginssid)
        cartcode = re.json()["code"]
        assert cartcode==1


    # 删除购物车商品
    @allure.step("删除购物车商品")
    @allure.title("删除购物车商品")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[27]])
    def test_deleteCartGoods(self,id,api_id,params,rowid,loginssid):
        cartid=self.cart.search_cartid(loginssid)
        paramter=eval(params)
        paramter['cartId']=cartid
        re = self.cart.deleteCartGoods(paramter,loginssid)
        cartcode = re.json()["code"]
        assert cartcode==1

    @allure.step("获取购物车商品等具体信息")
    @allure.title("获取购物车商品等具体信息")
    @pytest.mark.parametrize("id,api_id,params,rowid",[casedate1[22]])
    def test_getCart(self,id,api_id,params,rowid,loginssid):
        re = self.cart.get_Cart(eval(params),loginssid)
        cartcode = re.json()["code"]
        # cartid = re.json()['result']['dataList'][0]['medicine_list'][0]['id']

        # for datalist in re.json()['result']['dataList']:
        #     for  medicine in datalist['medicine_list']:
        #         print(medicine['id'])
        #

        assert cartcode==1
