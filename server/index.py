from header import app
from flask import render_template, url_for, redirect, request, session
from users import UserInfo
from dbconn import curs


def render_redirect(template, url, error):
    if error is None:
        return redirect(url_for(url))
    print(error)
    return render_template(template, error=error)


@app.route("/")
@app.route("/main")
def main_page():
    curs.execute("desc User;")
    for i in range(6):
        print(curs.fetchone()[0])
    curs.execute("SELECT * FROM User;")
    print(curs.fetchall())
    return render_template('main.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        user_id = request.form['person_id']  # login id
        pwss = request.form['password']  # password
        user_name = request.form['name']  # your personal name
        email = request.form['email']  # your eamil
        identifyNum = request.form['idNumber']  # local number

        if "" in [user_id, pwss, user_name, email, identifyNum]:
            error = 'Empty Filed'
        else:
            user = UserInfo(email)
            error = user.Register(user_id, pwss, user_name, email, identifyNum)
        return render_redirect('main.html', 'main_page', error)
    else:
        return render_template('registration.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_id = request.form['person_id']
        pwss = request.form['password']
        print(user_id, pwss)
        if "" in [user_id, pwss]:
            error = 'Empty Filed'
        else:
            user = UserInfo(user_id)
            error = user.Login(pwss)
        return render_redirect('login.html', 'main_page', error)
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    error = UserInfo(session.get).Logout()
    if error is False:
        return redirect(url_for('main_page'))
    else:
        return render_redirect('main.html', 'main_page', error)


@app.route("/MyInfo", methods=['GET', 'POST'])
def check_myinfo():
    return render_template("myinfo.html")


@app.route("/MyPosts", methods=['GET', 'POST'])
def check_mypost():
    return render_template("index.html")


@app.route("/board/<board_name>", methods=['GET'])
def board_open(board_name):
    return render_template(board_name+".html")


@app.route("/admin_page", methods=['POST'])
def admin():
    return render_template("admin.html")


@app.route("/write_post/<board_name>", methods=['GET', 'POST'])
def write_post(board_name):
    error = None
    if request.method == 'POST':
        return render_template(board_name+".html")
    else:
        error = "not logged in"
        return render_template("main.html", "main_page", error)


@app.route("/modify_post/<board_name>", methods=['POST'])
def modify_post(board_name):
    return render_template(board_name+".html")
