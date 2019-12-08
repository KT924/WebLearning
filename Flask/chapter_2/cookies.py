from flask import Flask
from flask import make_response,redirect
from flask import request,url_for

app=Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello():
    name=request.args.get('name')
    if name is None:
        name=request.cookies.get('name','Human')
    return '<H1> Hello {0} </h1>'.format(name)

@app.route('/set/<name>')
def set_cookies(name):
    response=make_response(redirect(url_for('hello')))
    response.set_cookie('name',name)
    return response

if __name__=='__main__':
    app.run(host='0.0.0.0')
