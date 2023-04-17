from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello World !!! My name is Anshul<h1>"

@app.route("/hello_world_galaxy")
def hello_world_galaxy():
    return "<h1>Hello Galaxy<h1>"    

@app.route("/hello_world_universe")
def hello_world_universe():
    return "<h1>Hello Universe<h1>"    

@app.route('/test')
def test():
    return ('The value of 5+6 is {}'.format(5+6))

@app.route('/test2')
def test2():
    data = request.args.get('x')
    return ('The value input from url is {}'.format(data))    

@app.route('/add')
def add():
    a = request.args.get('¸q')
    b = request.args.get('x')
    c = a+b
    return ('Sum is {}'.format(c))    

if __name__=='__main__':
    app.run(host = "0.0.0.0")