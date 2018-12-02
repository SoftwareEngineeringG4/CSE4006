from flask import redirect, url_for, flash, session
from dbconn import curs


class UserInfo:

    '''
    Represent a user.
    init whit login, have session
    '''

    req_email = ""

    userIdCheck = u"SELECT person_id FROM User where person_id = {0}"
    PwssCheck = u"SELECT password FROM User where person_id = {0}"
    query3 = u"SELECT person_id FROM User where email = ?"
    query4 = u"SELECT person_id FROM User WHERE person_id = ?"
    findquery = u"SELECT person_id FROM User WHERE person_id = ?"

    def __init__(self, user_id):
        self.signed_in = False
        self.name = "default"
        self.user_id = user_id
        self.selectquery = ""
        self.query = ""

    def Login(self, pwss):
        error = None
        signinquery = ("select name from User where person_id=\'"
                       + self.user_id + "\'")
        print(signinquery)
        self.selectquery = u"SELECT EXISTS (" + UserInfo.userIdCheck + u")"
        tmp = self.selectquery.format(self.user_id)
        userid_ = curs.execute(tmp).fetchone()
        if userid_[0] == 0:
            error = "Invalid"
        else:
            self.selectquery = u"SELECT EXISTS (" + UserInfo.PwssCheck + u")"
            tmp = self.selectquery.format(self.user_id)
            pwss_ = curs.execute(tmp).fetchone()
            if pwss_[0] == pwss:
                error = "Invalid"
            else:
                session['logged_in'] = True
                session['person_id'] = self.user_id
                self.signed_in = True
                temp = curs.execute(signinquery.encode("utf-8"))
                self.name = temp.fetchone()
                flash('Welcom ' + self.name[0])
        return error

    def Register(self, user_id, pwss, user_name, email, identifyNum):
        error = None

        if "" in [user_id, pwss, user_name, email, identifyNum]:
            error = "Filed is Empty!"
        else:
            self.selectquery = u"SELECT EXISTS (" + UserInfo.query3 + u")"
            email_ = curs.execute(self.selectquery, (email, )).fetchone()
            self.selectquery = u"SELECT EXISTS (" + UserInfo.query4 + u")"
            name_ = curs.execute(self.selectquery, (user_id, )).fetchone()

            if email_[0] == 0 and name_[0] == 0:
                flash('Account Created!')
                curs.execute(UserInfo.findquery, [email, user_id, pwss])
                curs.commit()
            else:
                error = "Already Exist"
        return error

    def ChangeUserInfo(self):
        error = None
        return redirect(url_for('mypage'))

    def Logout(self):
        error = None
        return redirect(url_for('signin'))
