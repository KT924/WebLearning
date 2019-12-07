from flask import Flask
from flask import redirect
from flask import session
from flask import request
from flask import url_for
from flask import make_response


USER_DATA = {'username': 'test', 'password': 'test123'}
app = Flask(__name__)
app.secret_key = "DevKey"

@app.route('/hello/',methods=['GET'])
def hello():
    username=session['username']
    return '<h1> hello {0} </h1>'.format(username)

@app.route('/login/', methods=['POST'])
def login():
    auth_data = request.get_json()
    print(auth_data)
    if (auth_data['username'] == USER_DATA['username']
        and auth_data['password'] == USER_DATA['password']):
        session['logged_in']=True
        session['username']=USER_DATA['username']
        session['password']=USER_DATA['password']
        return redirect(url_for('hello'))
    else:
        return '<h1> 用户名密码不正确 </h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
