from db.dbconn import curs


class Board:

    def __init__(self, board_name, write_auth):
        self.bid = 0
        self.board_name = board_name
        self.write_auth = write_auth

    def GetBlackList(self):
        sql = "SELECT * FROM `BlackList`;"
        list = []
        curs.execute(sql)
        list = curs.fetchall()
        return list

    def GetPostList(self):
        sql1 = "SELECT * FROM `Board`;"
        list = []
        curs.execute(sql1)
        list = curs.fetchall()
        return list

    def AddPost(self, title, contents, writer):
        InsertPost = "INSERT INTO " + self.board_name + " (`title`, `contents`, `writer`)\
                      VALUES (" + title + contents + writer + ");"

        InsertBoard = "INSERT INTO `Board` (`bid`, `board_name`, `write_name`) VALUES \
                       (" + self.bid + self.board_name + self.write_auth + ");"

        curs.execute(InsertPost)
        curs.execute(InsertBoard)
        curs.commit()

