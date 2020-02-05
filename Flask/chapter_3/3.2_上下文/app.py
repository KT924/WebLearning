from flask import Flask
from flask import render_template
from flask import url_for
from flask import session
from flask import Markup

app=Flask(__name__)
app.secret_key = "DevKey"


@app.route('/')
def index():
    people="John"
    return render_template('index.html',people=people)

"""
上下文变量
当调用render_template函数渲染模板时，带有该装饰器的函数都会被执行
需要返回一个dict对象
app.context_processor(inject_foo) 直接传入函数名
app.context_processor(lambda : dict(foo="I am foo."))  或使用lambda表达式
"""
@app.context_processor
def inject_foo():
    # foo="I am foo."
    foo = 'I am foo'
    lst=[1,2,3,4,5,6]
    n='taotao'
    return dict(foo=foo,lst=lst,n=n)

"""
全局函数
app.add_template_global(function,name)
"""
@app.template_global()
def bar():
    return 'I am bar'

"""
过滤器
"""
@app.template_filter()
def musical(s):
    return s+Markup(' &#9835;')

"""
测试器
{% if age is number %}
    {{ age }}
{% else %}
    表达式
{% endif %}
"""
@app.template_test()
def name(n):
    if n == 'taotao':
        return True
    return False

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)