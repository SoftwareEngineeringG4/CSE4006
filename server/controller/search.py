from db.dbconn import curs
from controller.board import Board


class Search:

    '''
    Search Part
    init with begin, keyword must have
    must search all board db data
    '''

    def __init__(self, keyword):
        self.search_word = keyword
        self.board_num = 0
        self.post_name = ""

    def FindPost(self, bid):
        boardList = Board(bid).GetPostList()
        findList = []
        for board in boardList:
            searchQuery = "SELECT `title`, `contents`, `write_time`, `writer` \
                    FROM " + board + " WHERE `title` = " + self.search_word + " OR \
                    `contents` = " + self.search_word + ";"
            curs.execute(searchQuery)
            findList += curs.fetchall()
        return findList

