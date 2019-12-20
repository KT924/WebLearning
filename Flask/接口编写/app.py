#!/bin/env python
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask import abort
from flask import redirect
from flask import url_for
from DbUtils import MySqlUtils
from collections import OrderedDict
import time
import json
app = Flask(__name__)

dbUtils = MySqlUtils("ip", 3306, 'admin', 'admin@123', 'demo')
@app.route('/api/v1/data/', methods=['GET'])
def query_all():
    datas = []
    sql = "SELECT * FROM DATA"
    result = dbUtils.select(sql)
    for row in result:
        row=make_public_uri(row)
        datas.append(row)
    return jsonify({'datas': datas})


@app.route('/api/v1/data/<int:id>/', methods=['GET'])
def query_from_id(id):
    data=[]
    sql = "SELECT * FROM DATA WHERE ID = %s"
    result = dbUtils.select(sql,(id,))
    for row in result:
        row=make_public_uri(row)
        data.append(row)
    
    return jsonify({'data':data})

@app.route('/api/v1/data/',methods=['POST'])
def create_data():
    data=request.json
    if not data:
        abort(404)
    user=data['user']
    description=data['description']
    create_time=time.strftime("%Y-%m-%d %H:%M:%S")
    update_time=time.strftime("%Y-%m-%d %H:%M:%S")
    sql="INSERT INTO DATA VALUES(id,%s,%s,%s,%s)"

    try:
        dbUtils.begin()
        count=dbUtils.insert(sql,(user,description,create_time,update_time))
        if count == 1:
            dbUtils.commit()
        else:
            dbUtils.commit(False)
    except:
        dbUtils.commit(False)
    return make_response(jsonify({"status":"insert success"}),201)
    

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}),404)


def make_public_uri(data):
    new_data={k:v for k,v in data.items()}
    id = data.get('id')
    new_data['uri']=url_for("query_from_id",id=str(id))
    return new_data


@app.route('/api/v1/data/<int:id>/',methods=['PUT'])
def update_data(id):
    data = request.json
    keyWord=['id','user','description']
    if not data:
        abort(404)
    for key in keyWord:
        if key not in data.keys():
            abort(400)
    sql="update data set user=%s,description=%s,update_time=%s where id = %s;"
    update_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    try:
        dbUtils.begin()
        count=dbUtils.update(sql,param=(data['user'],data['description'],update_time,data['id']))
        if count == 1:
            dbUtils.commit()
        else:
            dbUtils.commit(False)
        return make_response(jsonify({'status':'update success'}))
    except:
        dbUtils.commit(False)
        abort(400)

@app.route('/api/v1/data/<int:id>/',methods=['DELETE'])
def delete_data(id):
    sql="delete from data where id = %s"
    try:
        dbUtils.begin()
        count = dbUtils.delete(sql,param=(id,))
        if count == 1:
            dbUtils.commit()
        else:
            dbUtils.commit(False)
        return make_response(jsonify({'status':'delete success'}))
    except Exception as e:
        dbUtils.commit(False)
        abort(400)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
