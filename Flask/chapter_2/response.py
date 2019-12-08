from flask import Flask,Response,abort
from flask import make_response

app=Flask(__name__)

@app.route('/hello/')
def hello():
    response=make_response('Hello World')
    response.minetype='text/html'
    response.status='418'
    response.headers={'Host':'172.0.0.1','name':'file'}
    return response
if __name__=='__main__':
    app.run(host='0.0.0.0')