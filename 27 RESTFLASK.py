from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/0")
def helloworld():
    return "<h1>Hello World</h1>"

@app.route("/1")
def helloworld1():
    return "<h1>Hello World1</h1>"

@app.route("/2")
def helloworld2():
    return "<h1>Hello World2</h1>"

@app.route("/test")
def test():
    a = 5+6
    return "This is my function to run hte prigrsmms {}".format(a)
@app.route("/test2")
def test2():
    data = request.args.get("x")
    return "This a data input from my url{}".format(data)
    #http://192.168.29.178:5000/test2?x=sudh
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")