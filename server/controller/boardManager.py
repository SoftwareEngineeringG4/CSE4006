from db.dbconn import curs, conn


class BoardManager:

    def __init__(self):
        self.selectquery = ""

    def AddPost(board_name, title, contents, writer):
        error = None
        InsertPost = "INSERT INTO %s (`title`, `contents`, `writer`)\
                      VALUES (%s, %s, %s, );"
        curs.execute(InsertPost, (board_name, title, contents, writer, ))
        if conn.commit() is False:
            error = False
        else:
            error = "Success Insert!!"
        return error

    def ModifyPost(self, title, contents, target_user_id):
        error = None
        ModifyQuery = "UPDATE `Post` SET `title` = %s,\
                    contents = %s WHERE person_id = %s"
        curs.execute(ModifyQuery, (title, contents, target_user_id, ))
        if conn.commit() is False:
            error = "error"
        else:
            error = "update your this post"
        return error

    def RemovePost(title):
        error = None
        deleteQuery = "DELETE FROM `Post` WHERE title = %s"
        print(curs.execute(deleteQuery, (title, )))
        error = "Delete Success!!"
        return error
