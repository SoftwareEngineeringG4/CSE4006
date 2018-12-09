from db.dbconn import curs
#  from controller.board import Board


class Search:

    '''
    Search Part
    init with begin, keyword must have
    must search all board db data
    '''

    def __init__(self, keyword):
        self.search_word = ['%' + keyword + '%']
        self.board_num = 3
        self.post_name = ""

    def FindPost(self, board_name):
        searchQuery = u"SELECT * FROM\
        Post WHERE (BID = (SELECT BID FROM Board WHERE board_name = %s))\
        AND (contents LIKE %s OR title LIKE %s);"
        curs.execute(searchQuery,
                     (board_name, self.search_word, self.search_word, ))
        findList = curs.fetchall()
        return findList

