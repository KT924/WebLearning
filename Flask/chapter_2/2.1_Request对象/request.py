from flask import Flask,request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    name=request.args.get('name','Flask')
    print(request.full_path)
    print(request.data)
    return '<h1> hello {0} </h1>'.format(name)

def do_something():
    print("Hello World")
if __name__=='__main__':
    app.run(host='0.0.0.0')