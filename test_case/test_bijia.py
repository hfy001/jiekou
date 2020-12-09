import pytest
import requests
import logging
import json
from mysql import mysqlDB
from data import canshu
from page_request.pagerequest import ApiMethod
import allure
from common import get_path


path=get_path.get_bijia()

casedate=canshu.ExcelData().openexl(path)

logging.basicConfig(level=logging.DEBUG)


@allure.epic("药房网APP")
@allure.feature("比价")
@allure.step("比价")
@allure.title("比价")
@pytest.mark.parametrize("caseID,host,path,headers,params,method,rowid",casedate)
def test_case01(caseID,host,path,headers,params,method,rowid):
    res=ApiMethod(host,path,eval(headers),eval(params),method)
    print(res)
    resstatuscode=res.getstatus()
    rescode=res.getcode()
    rerowcount=res.getrowcount()
    b=eval(params)['conditions']
    d=eval(b)['medicineid']
    print(d)

    sql = """select count(*) from
                           ( select sm.id  from stk_store_medicine sm
                             join stk_medicine m  on m.id=sm.medicineid
                             join sto_store st on st.id=sm.storeid
                             left join sys_region r on r.id=st.regionid
                             join sto_store_shop ss on st.id=ss.storeid
                             left join sto_store_fake sf on st.id=sf.storeid
                             join stk_special_category sc on sc.id=m.categoryid
                             join stk_store_medicine_price smp on smp.store_medicineid=sm.id and smp.dict_price_type=1
                             left JOIN  sto_app_keys sak on sak.storeid=st.id and sak.dict_bool_status=1
                             left join sto_store_config ssc on st.id=ssc.storeid
                             where st.dict_store_type=1
                             and st.dict_store_sub_type=0 and st.dict_business_status=1 and st.dict_business_status_store=1 and st.dict_store_status=4
                             and m.active=1 and sc.active=1 and sm.standard=m.standard   and sm.dict_store_medicine_status>0 and sm.reserve>0 and  sm.dict_scheduled_days < 2
                             and sc.dict_medicine_b2c_status>=0 and m.dict_medicine_b2c_status>=0 and (ss.dict_bool_fake=0 or( ss.dict_bool_fake=1 and ((sc.dict_medicine_type>0
                             and sf.dict_store_fake<>1) OR (sc.dict_medicine_type=0 and sf.dict_store_fake<>2) OR (sc.dict_medicine_type=-1  and sf.dict_store_fake<>3)) ))
                             and m.id={0} and (IFNULL(sak.dict_app_type,0)=3 or ss.dict_shop_type!=3)
                             and ( r.name_path not like concat('%','全国','%' ) or st.dict_bool_citytrading=1 )  ) tb1 limit 1 ;""".format(d)

    db = mysqlDB.DB()

    chaxun=db.query(sql)[0]['count(*)']
    db.close()

    assert resstatuscode==200,"判断响应code为 %s" % resstatuscode
    assert rescode == 1, "判断code是不是=1,code的值为 %s" % rescode
    assert rerowcount==chaxun