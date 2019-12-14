import time
from DBUtils.PooledDB import PooledDB
import pymysql
import datetime


class MysqlClient:
    __pool = None

    def __init__(self, mincached=4, maxcached=8, maxconnections=20,
                 blocking=True, maxusage=100, setsession=None, **kwargs):
        if not self.__pool:
            host = kwargs.get('host')
            port = kwargs.get('port')
            user = kwargs.get('user')
            passwd = kwargs.get('passwd')
            db = kwargs.get('db')
            self.__class__.__pool = PooledDB(
                pymysql, mincached=mincached,
                maxcached=maxcached, maxconnections=maxconnections,
                setsession=setsession, host=host, user=user, db=db, port=port, passwd=passwd,
                cursorclass=pymysql.cursors.DictCursor
            )
            self._conn = None
            self._cursor = None
            self.__get_conn()

    def __get_conn(self):
        self._conn = self.__pool.connection()
        self._cursor = self._conn.cursor()

    def close(self):
        try:
            #self._cursor.close()
            self._conn.close()
        except Exception as e:
            print(e)

    @staticmethod
    def __dict_datetime_to_str(result_dict):
        if result_dict:
            result_replace = {k: v.__str__() for k, v in result_dict.items(
            ) if isinstance(v, datetime.datetime)}
            result_dict.update(result_replace)
        return result_dict

    def __execute(self, sql, param=()):
        try:
            count = self._cursor.execute(sql, param)
        except Exception as e:
            print("__execute方法执行错误", e)
        finally:
            self.close()
        return count
    
    def __executemany(self,sql,param=()):
        try:
            count=self._cursor.executemany(sql,param)
        except Exception as e:
            print("__executemany方法执行错误",e)
        finally:
            self.close()
        return count

    def execute_select(self, sql, param=()):
        count = self.__execute(sql, param)
        result = self._cursor.fetchone()
        result = self.__dict_datetime_to_str(result)
        return count, result

    def execute_select_many(self, sql, param=()):
        count = self.__execute(sql, param)
        result=self._cursor.fetchall()
        [self.__dict_datetime_to_str(row) for row in result]
        return count,result

    def execute_insert(self, sql, param=()):
        self.begin()
        count = self.__execute(sql, param)
        self.end('commit')
        return count
    
    def execute_insert_many(self,sql,param=()):
        pass



    def begin(self):
        self._conn.autocommit(0)

    def end(self, option='commit'):
        if option == 'commit':
            self._conn.autocommit()
        else:
            self._conn.rollback()



