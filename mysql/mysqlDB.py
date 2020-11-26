import os
import pymysql

DB_CONF = {
    'host': '192.168.2.252',
    'port': 3306,
    'user': 'test_group',
    'password': 'test123_group',
    'db': 'yaofangwang_dev',
    'charset': 'utf8'
}


class DB(object):
    def __init__(self, db_conf=None):
        if db_conf is None:
            db_conf = DB_CONF
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def query(self, sql):
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
            print(f'查询sql: {sql} 查询结果: {data}')
            return data
        except:
            print("Error: unable to fecth data")


    def change_db(self, sql):
        try:
            result = self.cur.execute(sql)
            print(f'执行sql: {sql} 影响行数: {result}')
        except:
            print("Error: unable to fecth data")

    def close(self):
        print('关闭数据库连接')
        self.cur.close()
        self.conn.close()




# class DB1(object):
#     def __init__(self):
#         self.conn=pymysql.connect(
#             host ="192.168.2.252",
#             user ="test_group",
#             passwd ="test123_group",
#             database ="yaofangwang_dev",
#             autocommit=True
#         )
#         self.mycursor =self.conn.cursor(cursor=pymysql.cursors.DictCursor)
#     def select_db(self,sql):
#         self.mycursor.execute(sql)
#         data=self.mycursor.fetchall()
#         print(data)
#         self.conn.close()



