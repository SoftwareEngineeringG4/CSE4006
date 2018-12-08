from flask import flash
from db.dbconn import curs


class userInfoManager:

    def __init__(self, user_id):
        self.updateQuery = ""
        self.user_id = user_id

    def ChangeUserInfo(self, pwss, user_name, email, identifyNum):
        error = None
        if "" in [pwss, user_name, email, identifyNum]:
            error = "Filed is Empty!"
        else:
            self.updateQuery = u"UPDATE User SET password = %s,\
                                name = %s, email = %s, idNumber = %s \
                                WHERE person_id like %s"
            curs.execute(self.updateQuery,
                         (pwss, user_name, email, identifyNum, self.user_id, ))
            flash("update Successed")
            error = "Update Successed"
        return error
