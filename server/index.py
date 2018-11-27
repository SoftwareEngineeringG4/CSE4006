import os
from flask import Flask, render_template
from dbconn import curs

#  SETTING DEFAULT TEMPLATES PATH
DEFAULT_TMP = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../src/templates/"))

app = Flask(__name__, template_folder=DEFAULT_TMP)


@app.route("/")
def hello():
    sql = "desc BlackList;"
    curs.execute(sql)
    version = curs.fetchall()
    return render_template('index.html', tb_desc=version[0])


@app.route("/hello")
def hello_s():
    return "Hello World?"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
