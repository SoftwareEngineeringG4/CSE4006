import os
from flask import Flask, render_template


template_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../src/templates/"))
print(template_dir)
app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def hello():
    print(template_dir)
    return render_template('index.html')


@app.route("/hello")
def hello_s():
    return "Hello World?"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
