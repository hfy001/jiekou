from mysql import mysqlDB


import json
from data import canshu

casedate=canshu.excelshuju().openexl('E:\pythonbijia\data\canshu1.xlsx')
print(casedate)

def medicineid():
    list=[]
    for i in  range(0,len(casedate)):
        a=casedate[i][3]
        print(type(a))
        b=eval(a)
        print(type(b))
        print(b['conditions'])
        cc=b['conditions']
        c=eval(cc)
        print(type(c))
        print(c['medicineid'])
        list.append(c['medicineid'])
    return  c['medicineid']
medicine=medicineid()
print(medicine)



# sql="""select count(*) from
#                    ( select sm.id  from stk_store_medicine sm
#                      join stk_medicine m  on m.id=sm.medicineid
#                      join sto_store st on st.id=sm.storeid
#                      left join sys_region r on r.id=st.regionid
#                      join sto_store_shop ss on st.id=ss.storeid
#                      left join sto_store_fake sf on st.id=sf.storeid
#                      join stk_special_category sc on sc.id=m.categoryid
#                      join stk_store_medicine_price smp on smp.store_medicineid=sm.id and smp.dict_price_type=1
#                      left JOIN  sto_app_keys sak on sak.storeid=st.id and sak.dict_bool_status=1
#                      left join sto_store_config ssc on st.id=ssc.storeid
#                      where st.dict_store_type=1
#                      and st.dict_store_sub_type=0 and st.dict_business_status=1 and st.dict_business_status_store=1 and st.dict_store_status=4
#                      and m.active=1 and sc.active=1 and sm.standard=m.standard   and sm.dict_store_medicine_status>0 and sm.reserve>0 and  sm.dict_scheduled_days < 2
#                      and sc.dict_medicine_b2c_status>=0 and m.dict_medicine_b2c_status>=0 and (ss.dict_bool_fake=0 or( ss.dict_bool_fake=1 and ((dict_medicine_type>0
#                      and sf.dict_store_fake<>1) OR (dict_medicine_type=0 and sf.dict_store_fake<>2) OR (dict_medicine_type=-1  and sf.dict_store_fake<>3)) ))
#                      and m.id={0} and (IFNULL(sak.dict_app_type,0)=3 or ss.dict_shop_type!=3)
#                      and ( r.name_path not like concat('%','全国','%' ) or st.dict_bool_citytrading=1 )  ) tb1 limit 1 ;""".format(medicine)

sql="""
select * from ( 
              select  ss.use_erp,sm.storeid,st.address,sm.reserve,sm.id,sm.medicineid,st.title as store_title,sm.dict_scheduled_days,smp.discount,smp.real_price,
              sm.dict_bool_purchase_certificate, ifnull(cast(cast(ses.evaluation_star_sum as decimal(18,1))/ses.evaluation_count/4.0 as decimal(18,1)),5) as shop_avg_level, 
             rpm.score_pr as score,r.id as region_id,r.name_path as region_name_path,rss.avg_send_time,rss.return_rate, 
            if(st.lat=0,10000,CAST(6378.137 * acos(cos(radians('31.249162')) * cos(radians(st.lat)) * cos(radians(st.lng) - radians('121.487899')) + sin(radians('31.249162')) * sin(radians(st.lat))) AS DECIMAL (18, 1))) AS distance,
           (case when if(st.lat=0,10000,CAST(6378.137 * acos(cos(radians('31.249162')) * cos(radians(st.lat)) * cos(radians(st.lng) - radians('121.487899')) + sin(radians('31.249162')) * sin(radians(st.lat))) AS DECIMAL (18, 1)))<=600 then 1 else 0 end )AS distance_orderby, (
           case when st.id=0 then 1 else 0 end ) sidOrderBy , m.intro_image_storeid,-1 manual_image_storeid,  
           IFNULL(rr.dict_store_order_rate_flag,2) dict_store_order_rate_flag ,0 activity_condition_price,0 activity_reduce_price ,ifnull(fp2.free_condition_price,1000000) free_condition_price,0 as is_freepostage,
           IFNULL(t4.name,'') medicine_package_desc ,IFNULL(t4.unit_price_temp,0) smp_unit_price,  sm.period_to,(case when IFNULL(sak.dict_app_type,0)=3 then IFNULL(sak.id,0) else 0 end) is_erp,m.period_month, 
           (case when ss.dict_shop_type in (1,2) and 0=1 then 1 else 0 end) shop_type 
               from stk_store_medicine sm    
               join stk_medicine m  on m.id=sm.medicineid    
               join sto_store st on st.id=sm.storeid  
               left join sys_region r on r.id=st.regionid  
               join sto_store_shop ss on st.id=ss.storeid   
               left join sto_store_fake sf on st.id=sf.storeid  
               join stk_special_category sc on sc.id=m.categoryid 
               join stk_store_medicine_price smp on smp.store_medicineid=sm.id and smp.dict_price_type=1    
               left join rep_store_order_rate rr on rr.storeid=st.id    
               left join sto_store_evaluation_star ses on ses.storeid=st.id    
               left join rep_pointrate_medicine_new rpm on sm.medicineid=rpm.medicineid and sm.storeid=rpm.storeid    
               left join rep_store_service rss on rss.storeid=sm.storeid     
               left JOIN  sto_app_keys sak on sak.storeid=st.id and sak.dict_bool_status=1 
               left join (select min(sf.condition_price) as free_condition_price,storeid 
                           from sto_store_freepostage sf         
                           where  sf.dict_store_freepostage_type=2 and sf.dict_enable=1 and sf.start_time<=now() and DATE_ADD(NOW(),INTERVAL -1 DAY)< sf.end_time
                          group by storeid )         fp2 on fp2.storeid=sm.storeid 
               left join  stk_store_medicine_package t4 on t4.store_medicineid_temp=sm.id and t4.qty_temp<=sm.reserve and t4.dict_enable=1 
             and dict_bool_show_bj=1 and unit_price_temp<smp.real_price  where st.dict_store_type=1 and st.dict_store_sub_type=0 and st.dict_business_status=1 
            and st.dict_business_status_store=1 and st.dict_store_status=4 and m.active=1 and sc.active=1 and sm.standard=m.standard   and sm.dict_store_medicine_status>0 
             and sm.reserve>0 and  sm.dict_scheduled_days < 2 and sc.dict_medicine_b2c_status>=0 and m.dict_medicine_b2c_status>=0 and (IFNULL(sak.dict_app_type,0)=3 
             or ss.dict_shop_type!=3)and (ss.dict_bool_fake=0 or( ss.dict_bool_fake=1 and ((dict_medicine_type>0 and sf.dict_store_fake<>1) OR (dict_medicine_type=0 
              and sf.dict_store_fake<>2) OR (dict_medicine_type=-1  and sf.dict_store_fake<>3)) ))   and 
              m.id = {0}  and (IFNULL(sak.dict_app_type,0)=3 or ss.dict_shop_type!=3)  
             and ( r.name_path not like concat('%','全国','%' ) or st.dict_bool_citytrading=1 ) ) _t 
             where 1=1 order by  dict_store_order_rate_flag desc,dict_bool_purchase_certificate desc,
              (case when (intro_image_storeid=storeid) then 1 else 0 end) desc,
              (case when (manual_image_storeid=storeid) then 1 else 0 end) desc,score desc,real_price asc ,id asc  limit 0,10;""".format(medicine)



db= mysqlDB.DB()
db.query(sql)
dd=db.query(sql)
print(dd)
db.close()

