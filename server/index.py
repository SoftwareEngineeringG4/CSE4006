from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/hello")
def hello_s():
    return "Hello World?"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
