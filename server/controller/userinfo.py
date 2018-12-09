from flask import flash, session
from db.dbconn import curs, conn


class UserInfo:

    '''
    Represent a user.
    init whit login, have session
    '''

    req_email = ""

    userIdCheck = u"SELECT `person_id` FROM `User` WHERE `person_id` = %s"
    PwssCheck = u"SELECT `password` FROM `User` WHERE `person_id` = %s"
    checkEmail = u"SELECT `person_id` FROM `User` WHERE `email` = %s"
    checkName = u"SELECT `name` FROM `User` WHERE `person_id` = %s"
    InsertQuery = u"INSERT INTO `User` \
    (person_id, password, name, email, idNumber)\
    VALUES (%s, %s, %s, %s, %s)"

    def __init__(self, user_id):
        self.signed_in = False
        self.name = "default"
        self.user_id = user_id
        self.selectquery = ""
        self.query = ""

def Login(self, pwss):
        error = None
        loginQuery = ("SELECT `name` FROM `User` WHERE `person_id`=\'"
                      + self.user_id + "\'")
        print(loginQuery)
        self.selectquery = UserInfo.userIdCheck
        curs.execute(self.selectquery, (self.user_id, ))
        userid_ = curs.fetchone()

        if userid_ == None:
            error = "Invalid"
            flash("There is no such ID")
        else:
            self.selectquery = UserInfo.PwssCheck
            curs.execute(self.selectquery, (userid_, ))
            pwss_ = curs.fetchone()
            if pwss_[0] != pwss:
                error = "Invalid"
                flash('Invalid')
            else:
                session['logged_in'] = True
                session['person_id'] = self.user_id
                self.signed_in = True
                curs.execute(loginQuery.encode("utf-8"))
                self.name = curs.fetchone()
                flash('Welcome ' + self.name[0])
                error = None

        return error

    def Register(self, user_id, pwss, user_name, email, identifyNum):
        error = None

        if "" in [user_id, pwss, user_name, email, identifyNum]:
            error = "Filed is Empty!"
        else:
            self.selectquery = u"SELECT EXISTS (" + UserInfo.checkEmail + u")"
            print(email)
            curs.execute(self.selectquery, (email, ))
            email_ = curs.fetchone()
            self.selectquery = u"SELECT EXISTS (" + UserInfo.checkName + u")"
            curs.execute(self.selectquery, (user_id, ))
            name_ = curs.fetchone()

            if email_[0] == 0 and name_[0] == 0:
                flash('Account Created!')
                curs.execute(UserInfo.InsertQuery,
                             (user_id, pwss, user_name, email, identifyNum, ))
                conn.commit()
            else:
                error = "Already Exist"
        return error

    def idValidCheck(self, candidate_user_id):
        error = None
        message = 0

        if candidate_user_id == "":
            error = "No Input"
        else:
            self.selectquery = u"SELECT EXISTS (" + UserInfo.userIdCheck + u")"
            curs.execute(self.selectquery, (candidate_user_id, ))
            userid_ = curs.fetchone()

            if userid_[0] == 0:
                message = 1
            else:
                message = 0

        return message, error

    def ChangeUserInfo(self):
        error = None
        return redirect(url_for('mypage'))


    def Logout(self):
        error = None
        print("Check Logout...")
        if self.user_id:
            session.clear()
            self.sign_in = False
            flash('logged out')
            error = "logout!!"
        return error

    def GetMyInfo(self):
        myinfoQuery = "SELECT password, name, email, idNumber\
                    FROM User WHERE person_id = %s"

        curs.execute(myinfoQuery, (self.user_id, ))
        values = curs.fetchall()[0]
        return values

    def GetMyPost(self):
        myinfoQuery = "SELECT title, contents, write_time, writer \
                    FROM Post WHERE writer = %s"

        curs.execute(myinfoQuery, (self.user_id, ))
        values = curs.fetchall()
        return values
