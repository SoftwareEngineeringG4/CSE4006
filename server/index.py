from header import app
from flask import render_template, url_for, redirect, request, session
from controller import userinfo, admin, adminManager, board
from controller import boardManager, search, userinfoManager
#  from db.dbconn import curs


defaultList = board.Board.GetBoardList()


def render_redirect(template, url, error):
    if error is None:
        return redirect(url_for(url))
    print(error)
    return render_template(template, error=error, auth=0, list=defaultList)


@app.route("/")
@app.route("/main", methods=['GET', 'POST'])
def main_page():
    auth = 0
    if request.method == 'POST':
        auth = admin.AdminInfo(session.get['person_id']).CheckAuth()
    return render_template('main.html', auth=auth, list=defaultList)


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
        return render_template('registration.html', list=defaultList)

@app.route("/register/idValidCheck", methods=['POST'])
def useridValidCheck():
    error = None
    if request.method == 'POST':
        candidate_user_id = request.form['id']
        if candidate_user_id == "":
            error = 'No Data'
        else:
            userInfo = userinfo.UserInfo()
    return

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
        return render_template('login.html', list=defaultList)


@app.route("/logout")
def logout():
    error = userinfo.UserInfo(session.get).Logout()
    if error is False:
        return redirect(url_for('main_page'))
    else:
        return render_redirect('main.html', 'main_page', error)


@app.route("/MyInfo", methods=['POST'])
def check_myinfo():
    myinfo = userinfoManager(session['person_id']).userInfoManager()
    print(myinfo)
    return render_template("myinfo.html", myinfo=myinfo, list=defaultList)


@app.route("/MyPosts", methods=['GET', 'POST'])
def check_mypost():
    if request.method == 'POST':
        mypost = userinfo.getMyInfo()
        print(mypost)
        return render_template("index.html", mypost=mypost, list=defaultList)
    else:
        render_redirect("main.html", 'main_page', "Valid error")


@app.route("/board/<board_name>", methods=['GET'])
def board_open(board_name):
    list = board.Board.GetPostList(board_name)
    print(list)
    return render_template("noticeboard.html",
                           list=defaultList, board=list, board_name=board_name)


@app.route("/post/<board_name>/<title>")
def spec_post(board_name, title):
    postValue = board.Board(board_name, 1).GetPost(title)
    print(postValue)
    return render_template("post.html", list=defaultList,
                           board_name=board_name,
                           title=postValue[1],
                           contents=postValue[2],
                           writer=postValue[3],
                           time=postValue[4])


@app.route("/admin_page", methods=['POST'])
def admin_page():
    auth = True
    error = None

    if request.methods == 'POST':
        auth = admin.AdminInfo(session.get).CheckAuth()
        adminMng = adminManager.Admin()
        button_val = request.form['sub_button']
        if button_val == 'adminAdd':
            target_user_id = request.form['user_name']
            error = adminMng.AdminAppointment(target_user_id)

        elif button_val == 'adminRemove':
            target_user_id = request.form['user_name']
            error = adminMng.AdminRemove(target_user_id)

        elif button_val == 'boardCreate':
            target_board_name = request.form['board_name']
            error = adminMng.boardCreate(target_board_name)

        elif button_val == 'addToBlackList':
            target_user_id = request.form['user_name']
            target_board_name = request.form['board_name']
            error = adminMng.AddBlackList(target_board_name, target_user_id)

        elif button_val == 'removeFromBlackList':
            target_user_id = request.form['user_name']
            target_board_name = request.form['board_name']
            error = adminMng.removeFromBlackList(target_board_name,
                                                 target_user_id)

    return render_template("admin.html",
                           auth=auth, error=error, list=defaultList)


@app.route("/write_post/<board_name>", methods=['GET', 'POST'])
def write_post(board_name):
    error = None
    auth = False
    if request.method == 'POST':
        title = request.form['subject']
        contents = request.form['content']
        writer = session['person_id']
        error = board.AddPost(board_name, title, contents, writer)
        if error is not False:
            return render_template(board_name+".html",
                                   error=error, auth=auth, list=defaultList)
        else:
            return render_template(board_name + ".html",
                                   error=error, list=defaultList)


@app.route("/modify_post/<board_name>", methods=['POST'])
def modify_post(board_name):
    error = None
    auth = False
    if request.method == 'POST':
        title = request.form['subject']
        contents = request.form['content']
        writer = session['person_id']
        error = board.ModifyPost(board_name, title, contents, writer)
        if error is not False:
            return render_template("write.html",
                                   error=error, auth=auth, list=defaultList)
        else:
            return render_template("write.html",
                                   error=error, list=defaultList)


@app.route("/search", methods=['GET', 'POST'])
def search_all():
    search_value = request.form['search']
    sendData = []
    for name in defaultList:
        sendData += search.Search(search_value).FindPost(name[1])
    return render_template("search.html",
                           values=sendData, list=defaultList,
                           keyword=search_value.encode("utf-8"))
