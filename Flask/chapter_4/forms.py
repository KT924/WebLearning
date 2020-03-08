from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from flask_wtf.file import FileRequired,FileAllowed,FileField
from wtforms.validators import DataRequired,Length


# 分别使用了wtforms的Form和flask_wtf的FlaskForm作为基类

# 主要区别在于视图在处理表单数据时，Form需要通过request.form来获取表单数据，而FlaskForm则直接通过对象的data属性来获取

class LoginFlaskForm(FlaskForm):
    username=StringField('Username')#,validators=[DataRequired()])
    password=PasswordField('Password')#,validators=[DataRequired(),Length(8,16)])
    remember=BooleanField('Remember me')
    object=FileField('Upload',validators=[FileAllowed(['txt'])])#,validators=[FileRequired(),FileAllowed(['txt'])])
    submit=SubmitField('Login')

class LoginForm(Form):
    username=StringField('Username')#,validators=[DataRequired()])
    password=PasswordField('Password')#,validators=[DataRequired(),Length(8,16)])
    remember=BooleanField('Remember me')
    submit=SubmitField('Login')