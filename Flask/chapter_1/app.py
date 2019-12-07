from flask import Flask
app=Flask(__name__)

@app.route('/')   #URL路由设置
def index():   #对应的view函数
    return '<h3>HELLO WORLD</h3>'
@app.route('/name/<name>')
def name(name):
    return "hello %s" % (name)
if __name__=='__main__':
    app.run(host='0.0.0.0')