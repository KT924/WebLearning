#!/bin/env python


import pymysql


class MySqlUtils:
    def __init__(self, host, port, user, password, dbName):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.dbName = dbName
        self.dbConn = self.connect_db()


    def __connect_db(self):
        dbConn = pymysql.connect(
            host=self.host, port=self.port, user=self.user, password=self.password, database=self.dbName)
        dbConn.autocommit(False)
        return dbConn

    def disconnect_db(self):
        self.dbConn.close()
    def insert_sql(self,sql):
        try:
            cursor = self.dbConn.cursor()
            cursor.execute(sql)
            self.dbConn.close()
            return True
        except:
            return False
    def update_sql(self):
        pass

    def delete_sql(self):
        pass

    def select_sql(self):
        pass

if __name__ == '__main__':
    dbUtils = MySqlUtils("192.168.10.11", 3306, 'admin', '111111', 'demo')
    sql="INSERT INTO card VALUES(id,'wkt','2019-12-08 19:21:22')"
    dbUtils.insert_sql(sql)
