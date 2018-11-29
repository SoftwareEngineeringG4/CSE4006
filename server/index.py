import os
from flask import Flask, render_template, url_for, redirect, request
from dbconn import curs

#  SETTING DEFAULT TEMPLATES PATH
DEFAULT_TMP = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../src/templates/"))

app = Flask(__name__, template_folder=DEFAULT_TMP)


def render_redirect(template, url, error):
    if error == None:
        return redirect(url_for(url))
    return render_template(template, error=error)


@app.route("/")
@app.route("/main", methods=['GET', 'POST'])
def main_page():
    sql = "desc Post;"
    curs.execute(sql)
    version = curs.fetchall()
    return render_template('index.html', tb_desc=version)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form['personid']
        email = request.form['email']
        name = request.form['username']
        pwss = request.form['password']
        pwsc = request.form['passconf']

        if "" in [email, name, pwss, pwsc]:
            error = 'Empty Filed'
        else:
            #  user = User(email)
            #  error = user.signup(email, name, pwss, pwsc)
        return render_template('signup.html')
    else:
        return render_template('main.html')


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    return redirect(url_for('main_page'))


@app.route("/MyInfo", methods='POST')
def change_myinfo():
    return redirect(url_for('main_page'))


@app.route("/board/<board_name>", methods='GET')
def board_open(board_name):
    return render_template(board_name+".html")


@app.route("/admin_page", methods='POST')
def admin():
    return render_template("admin.html")


@app.route("/write_post/<board_name>", methods='POST')
def write_post(board_name):
    return render_template("admin.html")


@app.route("/modify_post/<board_name>", methods='POST')
def modify_post(board_name):
    return render_template("admin.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
