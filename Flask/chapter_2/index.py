from flask import Flask,redirect
app=Flask(__name__)

#方法选择
@app.route('/hello',methods=['GET'])
def hello():
    return '<h2> Hello Flask</h1>',404
#变量转换
@app.route('/goback/<int:year>')
def go_back(year):
    return '<p> Welcome to %d </p>' %(2018-year)
#any选择器
@app.route('/colors/<any(blue,red,green):color>')
def three_colors(color):
    return '<p>Love is patient and kine.love is not jealous or boastful or proud or rude.</p>'

#请求钩子
@app.before_first_request
def do_something():
    print('hello world')

@app.route('/baidu')
def baidu():
    return redirect('https://www.baidu.com')
if __name__=='__main__':
    app.run()