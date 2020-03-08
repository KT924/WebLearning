from flask import Flask
from flask import render_template
from forms import LoginForm
from forms import LoginFlaskForm
from flask import request
from flask import redirect
from flask import url_for
import uuid,os

app = Flask(__name__)
app.secret_key="DEVkey"
app.config['MAX_CONTENT_LENGTH']=3*1024*1024
app.config['UPLOAD_PATH']=os.path.join(app.root_path,'uploads')

def random_filename(filename):
    ext=os.path.splitext(filename)[1]
    new_filename=uuid.uuid4().hex +ext
    print(new_filename)
    return new_filename



@app.route('/',methods=['GET','POST'])
def index():
    form=LoginFlaskForm()
    # form=LoginForm()
    # if request.method == 'POST' and form.validate():
    print(form.validate())
    if form.validate_on_submit():
        print('haha',form.data,form.errors)
        f= form.object.data
        print(type(form.object))
        filename=random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        return redirect(url_for('index'))
    return render_template('index.html',form=form)

@app.route('/home')
def home():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
