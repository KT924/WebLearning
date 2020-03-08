from flask import Flask
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for

app=Flask(__name__)
app.secret_key="DEVkey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flash')
def just_flash():
    flash('I am flash,who is looking for me ?')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)