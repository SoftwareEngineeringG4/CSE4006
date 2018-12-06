from db.dbconn import curs


class Board:

    def __init__(self, board_name):
        self.bid = 0
        self.board_name = board_name
        self.write_auth = 0
        
    def GetBlackList(self):
        sql = ""
        
    def GetPostList(self):
        sql1 = ""
        list = []
        curs.execute()
        return list
    
    def AddPost(self):
        sql2 = ""
        curs.execute()