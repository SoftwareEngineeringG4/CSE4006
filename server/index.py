from header import app
from flask import render_template, url_for, redirect, request, session
from controller import userinfo, admin, adminManager, board, boardManager, search
#  from db.dbconn import curs


def render_redirect(template, url, error):
    if error is None:
        return redirect(url_for(url))
    print(error)
    return render_template(template, error=error, auth=3)


@app.route("/")
@app.route("/main", methods=['GET', 'POST'])
def main_page():
    auth = 3
    if request.method == 'POST':
        auth = admin.AdminInfo(session.get['person_id']).CheckAuth()
    return render_template('main.html', auth=auth)


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
            user = userinfo.UserInfo(email)
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
            user = userinfo.UserInfo(user_id)
            error = user.Login(pwss)
        return render_redirect('login.html', 'main_page', error)
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    error = userinfo.UserInfo(session.get).Logout()
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
def admin_page():
    auth = True
    if request.methods == 'POST':
        auth = admin.AdminInfo(session.get['person_id']).CheckAuth()
    return render_template("admin.html", auth=auth)


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


@app.route("/search", methods=['GET', 'POST'])
def search_all():
    search_value = request.form['aaaa']
    return render_template("search.html", search=search_value)
