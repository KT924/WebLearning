"""
Flask基础，与配置文件使用
"""


from flask import Flask
import config
app=Flask(__name__)
app.config.from_object(config)
@app.route('/')   #URL路由设置
def index():   #对应的view函数
    return '<h3>HELLO WORLD</h3>'
@app.route('/name/<name>/')
def name(name):
    return "hello %s" % (name)
if __name__=='__main__':
    app.run(host=app.config['HOST'],port=app.config['PORT'])