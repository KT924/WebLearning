#!/bin/env python

import time
import datetime
import pymysql


class MySqlUtils:
    def __init__(self, host, port, user, password, dbName):
        self._dbConn = self.__connect_db(host, port, user, password, dbName)
        self._cursor = self.__get_cursor()

    def __connect_db(self, host, port, user, password, dbName):
        try:
            dbConn = pymysql.connect(
                host=host, port=port, user=user, password=password, database=dbName)
            dbConn.autocommit(False)
            return dbConn
        except Exception as e:
            print('连接失败', e)

    def reconnect(self,host,port,user,password,dbName):
        self._dbConn = self.__connect_db(host,port,user,password,dbName)
        self._cursor = self.__get_cursor()
        
    def __get_cursor(self, cursorType=pymysql.cursors.DictCursor):
        #print(type(self._dbConn))
        if  self._dbConn:
            return self._dbConn.cursor(cursor=cursorType)
            

    def __close_conn(self):
        self._dbConn.close()

    def __close_cursor(self):
        self._cursor.close()

    def __execute(self, sql, param=()):
        try:
            count = self._cursor.execute(sql, param)
            return count
        except Exception as e:
            print("__execute方法执行错误", e)

    def __executemany(self, sql, param=()):
        try:
            count = self._cursor.executemany(sql, param)
            return count
        except Exception as e:
            print('__executemany方法执行错误', e)

    @staticmethod
    def __dict_datetime_to_str(resultDict):
        if resultDict:
            resultReplace = {k: v.__str__() for k, v in resultDict.items(
            ) if isinstance(v, datetime.datetime)}
            resultDict.update(resultReplace)
        return resultDict

    def begin(self):
        self._dbConn.begin()

    def commit(self, commit=True):
        if commit:
            self._dbConn.commit()
        else:
            self._dbConn.rollback()

        
    def select(self, sql, param=()):
        count = self.__execute(sql, param)
        while count != 0:
            row = self._cursor.fetchone()
            row = self.__dict_datetime_to_str(row)
            count -= 1
            yield row
            
    def insert(self, sql, param=(), many=False):
        if not many:
            count = self.__execute(sql, param)
        else:
            count = self.__executemany(sql, param)
        return count

    def update(self, sql, param=(), many=False):
        if not many:
            count = self.__execute(sql, param)
        else:
            count = self.__executemany(sql, param)
        return count

    def delete(self, sql, param=(), many=False):
        if not many:
            count = self.__execute(sql, param)
        else:
            count = self.__executemany(sql, param)
        return count


if __name__ == '__main__':
   
    #dbUtils = MySqlUtils("192.168.10.11", 3306, 'admin', '111111', 'demo')
    #sql = "INSERT INTO DATA values(id,'wkt','测试数 据插入','2019-12-19 00:00:00','2019-12-19 00:00:00','http://localhost/data/1')"
    sql = "SELECT * FROM data;"
    while True:
        #sql="INSERT INTO card VALUES(id,'wkt','2019-12-08 19:21:22')"   
        #dbUtils.begin()
        count=dbUtils.select(sql)
        #dbUtils.commit(False)
        print(next(count))
        time.sleep(2)
        break