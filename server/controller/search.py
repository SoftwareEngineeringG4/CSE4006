from db.dbconn import curs


class Search:

    '''
    Search Part
    init with begin, keyword must have
    must search all board db data
    '''

    def __init__(self, keyword):
        self.serach_word = keyword
        self.board_name = ""
        self.board_num = 0
        self.post_name = ""

    def FindPost(self):
        sql1 = "SELECT (board_name, ) FROM " + self.board_num + "WHERE 
        sql2 = ""

        curs.execute()

