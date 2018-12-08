from db.dbconn import curs


class AdminInfo:

    def __init__(self, person_id):
        self.id = person_id

    def CheckAuth(self):
        error = False
        AuthQuery = "SELECT `auth` FROM `User` WHERE \
                     `person_id` = " + self.id + ";"
        curs.execute(AuthQuery)
        auth_ = curs.fetchone()
        if auth_[0] > 2:
            error = True
        return error
