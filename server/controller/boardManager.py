from db.dbconn import curs, conn


class BoardManager:

    postCheck = u"SELECT `auth` FROM `User` WHERE `person_id` = %s"

    def __init__(self):
        self.selectquery = ""

    def AddPost(board_name, title, contents, writer):
        InsertPost = "INSERT INTO " + board_name + " (`title`, `contents`, `writer`)\
                      VALUES (" + title + contents + writer + ");"
        curs.execute(InsertPost)
        curs.commit()

    def ModifyPost(self, title, contents, target_user_id):
        error = None
        ModifyQuery = "UPDATE `Post` SET `title` = %s,\
                    contents = %s WHERE person_id = %s"
        if target_user_id == "":
            error = "Invalid!"
        else:
            self.selectquery = u"SELECT EXISTS (" + self.postCheck + u")"
            curs.execute(self.selectquery, (target_user_id, ))
            userid_ = curs.fetchone()

            if userid_[0] == 0:
                error = "No data"
            else:
                curs.execute(ModifyQuery, (title, contents, ))
                conn.commit()
        return error

    def RemovePost():

        return 0
