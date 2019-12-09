#!/bin/env python
from flask import Flask,request
from DbUtils import MySqlUtils
import time
import json
import uuid
app=Flask(__name__)


@app.route('/card/',methods=['POST'])
def card():
    dbUtils = MySqlUtils("192.168.10.11", 3306, 'admin', '111111', 'demo')
    sessionID=str(uuid.uuid1())
    body=request.json
    user=body['user']
    updateTime=time.strftime(r"%Y-%m-%d %H:%M:%S",time.localtime())
    sql="INSERT INTO CARD VALUES(id,'{0}','{1}')".format(user,updateTime)
    flag=dbUtils.insert_sql(sql)
    response=json.dumps({"uuid":sessionID,"update_time":updateTime,"user":user,"success":flag},indent=4)
    return response


if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)