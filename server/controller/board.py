from db.dbconn import curs


class Board:

    def __init__(self, board_name, write_auth):
        self.bid = 0
        self.board_name = board_name
        self.write_auth = write_auth

    def GetBlackList():
        sql = "SELECT * FROM `BlackList`;"
        list = []
        curs.execute(sql)
        list = curs.fetchall()
        return list

    def GetPostList(board):
        sql = "SELECT * FROM `Post` WHERE BID = \
        (SELECT BID FROM `Board` WHERE board_name = %s );"
        list = []
        curs.execute(sql, (board, ))
        list = curs.fetchall()
        return list

    def GetBoardList():  # Use At Search Part
        sql1 = "SELECT * FROM `Board`;"  # Attribute bid, board_name, auth
        list = []
        curs.execute(sql1)
        list = curs.fetchall()
        return list

    def GetPost(self, title):
        postQuery = "SELECT BID, title, contents, writer, write_time FROM Post WHERE BID = \
        (SELECT BID FROM Board WHERE board_name = %s) AND title = %s;"
        curs.execute(postQuery, (self.board_name, title, ))
        thisPost = curs.fetchone()
        return thisPost
