#!/bin/env python
from flask import Flask,request,make_response,jsonify
from DbPoolUtils import MysqlClient
import time
import json
import uuid
app=Flask(__name__)

dbUtils = MysqlClient(user='admin', host="192.168.10.11",
                     passwd='111111', db='demo', port=3306)
@app.route('/card/',methods=['POST'])
def card():
    sessionID=str(uuid.uuid1())
    body=request.json
    user=body['user']
    updateTime=time.strftime(r"%Y-%m-%d %H:%M:%S",time.localtime())
    sql="INSERT INTO CARD VALUES(id,%s,%s)"
    flag=dbUtils.insert(sql,(user,updateTime))
    response=jsonify({"uuid":sessionID,"update_time":updateTime,"user":user,"success":flag})
    return response

@app.route('/query/',methods=['GET'])
def query():
    sessionId=str(uuid.uuid1())
    id=request.args['id']
    sql="SELECT * FROM CARD WHERE ID = %s"
    result=dbUtils.select(sql,(id,))
    for each in result:
        print(each)
    return 'hello'


if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)