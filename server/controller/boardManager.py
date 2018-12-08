from db.dbconn import curs


class BoardManager:

    def AddPost(board_name, title, contents, writer):
        InsertPost = "INSERT INTO " + board_name + " (`title`, `contents`, `writer`)\
                      VALUES (" + title + contents + writer + ");"
        curs.execute(InsertPost)
        curs.commit()

    def ModifyPost():

        return 0

    def RemovePost():

        return 0
