#!/bin/env python
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask import abort
from flask import redirect
from flask import url_for
from DbUtils import MySqlUtils
import time
import json
import uuid
app = Flask(__name__)

#dbUtils = MySqlUtils("ip", 3306, 'admin', 'admin@123', 'demo')
@app.route('/api/v1/data/', methods=['GET'])
def query_all():
    datas = []
    sql = "SELECT * FROM DATA"
    result = dbUtils.select(sql)
    for row in result:
        datas.append(row)
    return jsonify({'datas': datas})


@app.route('/api/v1/data/<int:id>/', methods=['GET'])
def query_from_id(id):
    data=[]
    sql = "SELECT * FROM DATA WHERE ID = %s"
    result = dbUtils.select(sql,(id,))
    for row in result:
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
    return data,201
    
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}),404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
