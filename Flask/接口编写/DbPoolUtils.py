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
        print(self.__pool,self._conn,self._cursor)

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
        count=""
        try:
            count = self._cursor.execute(sql, param)
            return count
        except Exception as e:
            print("__execute方法执行错误", e)


    
    def __executemany(self,sql,param=()):
        count=""
        try:
            count=self._cursor.executemany(sql,param)
            return count
        except Exception as e:
            print("__executemany方法执行错误",e)
        finally:
            self.close()


    def select(self, sql, param=()):
        count = self.__execute(sql, param)
        while count != 0:
            result=self._cursor.fetchone()
            result=self.__dict_datetime_to_str(result)
            count-=1
            yield (count,result)
        self.close()



    def insert(self, sql, param=()):
        self.__get_conn()
        self.begin()
        count = self.__execute(sql, param)
        if count != 1:
            self.end('rollback')
        else:
            self.end('commit')
        return count




    def begin(self):
        self._conn.begin()
        #self.__execute('begin;')

    def end(self, option='commit'):
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()


if __name__ == '__main__':
    mc = MysqlClient(user='admin', host="192.168.10.11",
                     passwd='111111', db='demo', port=3306)
    #sql = 'INSERT INTO CARD values (id,\'wkt\',\'2019-12-14 19:00:00\')'
    for each in range(5):
        sql = 'SELECT * FROM CARD;'
        result = mc.select(sql)
        time.sleep(5)
        for each in result:
            print(each)