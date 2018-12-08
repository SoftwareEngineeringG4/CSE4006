# JinMyeong Lee
from flask import redirect, url_for, flash, session
from db.dbconn import curs, conn


class Admin():

    userIdCheck = u"SELECT `person_id` FROM `User` WHERE `person_id` = %s"
    PwssCheck = u"SELECT `password` FROM `User` WHERE `person_id` = %s"
    boardCheck = u"SELECT `BID` FROM `Board` WHERE `board_name` like %s"
    blacklistCheck = u"SELECT `BID` FROM `BlakcList` WHERE user_id like %s \
    and BID = (SELECT BID from Board where board_name like %s)"

    def __init__(self):
        self.selectquery = ""

    def AddBlackList(self, target_board_name, target_user_id):
        error = None

        InsertToBlackList = u"INSERT INTO `BlackList`(BID, user_id) \
        VALUES((SELECT BID from Board where board_name like %s), %s)"

        if "" in [target_board_name, target_user_id]:
            error = "Invalid Input!"
        else:
            self.selectquery = u"SELECT EXISTS (" + self.userIdCheck + u")"
            curs.execute(self.selectquery, (target_user_id, ))
            userid_ = curs.fetchone()

            self.selectquery = u"SELECT EXISTS (" + self.boardCheck + u")"
            curs.execute(self.selectquery, (target_board_name, ))
            board_name_ = curs.fetchone()

            self.selectquery = u"SELECT EXISTS (" + self.blacklistCheck + u")"
            curs.execute(self.selectquery,
                         (target_user_id, target_board_name, ))
            blacklist_ = curs.fetchone()

            if userid_[0] == 0 and board_name_[0] == 0:
                error = "Invalid"
            elif blacklist_[0] != 0:
                error = "Already Exist"
            else:
                flash("Added to BlackList")
                curs.execute(InsertToBlackList,
                             (target_board_name, target_user_id, ))
                conn.commit()

        return error

    def RemoveBlackList(self, target_board_name, target_user_id):
        error = None
        RemoveFromBlackList = u"DELETE FROM BlackList WHERE user_id like %s \
        and BID = (SELECT BID from Board where board_name like %s)"
        if "" in [target_board_name, target_user_id]:
            error = "Invalid Input!"
        else:
            self.selectquery = u"SELECT EXISTS (" + self.userIdCheck + u")"
            curs.execute(self.selectquery, (target_user_id, ))
            userid_ = curs.fetchone()

            self.selectquery = u"SELECT EXISTS (" + self.boardCheck + u")"
            curs.execute(self.selectquery, (target_board_name, ))
            board_name_ = curs.fetchone()

            self.selectquery = u"SELECT EXISTS (" + self.blacklistCheck + u")"
            curs.execute(self.selectquery, (target_user_id, target_board_name, ))
            blacklist_ = curs.fetchone()

            if userid_[0] == 0 and board_name_[0] == 0:
                error = "Invalid"
            elif blacklist_[0] == 0:
                error = "No data"
            else:
                flash("Successfully Removed!")
                curs.execute(RemoveFromBlackList,
                             (target_user_id, target_board_name, ))
                conn.commit()

        return error

    def BoardCreate(self, board_name):
        error = None
        # write_auth 1 means that everyone can write a post in this board
        # write_auth 0 menas that only manager can write a post in this board
        CreateBoard = u"INSERT INTO Board(board_name, write_auth) \
                        VALUES (%s, 1)"

        if board_name == "":
            error = "Invalid Input!"
        else:
            self.selectquery = u"SELECT EXISTS (" + self.boardCheck + u")"
            curs.execute(self.selectquery, (target_board_name, ))
            board_name_ = curs.fetchone()

            if board_name_[0] == 0:
                flash("Board Created!")
                curs.execute(CreateBoard, (board_name, ))
                conn.commit()
            else:
                error = "Already Exist"
        return error

    def BoardRemove(self, board_name):
        error = None
        RemoveBoard = u"DELETE FROM Board WHERE board_name like %s"
        if board_name == "":
            error = "Invalid Input!"
        else:
            self.selectquery = u"SELECT EXISTS (" + self.boardCheck + u")"
            curs.execute(self.selectquery, (target_board_name, ))
            board_name_ = curs.fetchone()

            if board_name_[0] == 0:
                error = "No data"
            else:
                flash("Board Removed!")
                curs.execute(RemoveBoard, (board_name))
                conn.commit()

        return error

    def AdminAppointment(self, target_user_id):
        error = None
        GiveAdmin = u"UPDATE User SET auth = 0 WHERE person_id like %s"
        if target_user_id == "":
            error = "Invalid Input!"
        else:
            self.selectquery = u"SELECT EXISTS (" + self.userIdCheck + u")"
            curs.execute(self.selectquery, (target_user_id, ))
            userid_ = curs.fetchone()

            if userid_[0] == 0:
                error = "No data"
            else:
                flash("Auth Changed!")
                curs.execute(GiveAdmin, (target_user_id, ))
                conn.commit()

        return error

    def AdminRemove(self, target_user_id):
        error = None
        RemoveAdmin = u"UPDATE User SET auth = 1 WHERE person_id like %s"
        if target_user_id == "":
            error = "Invalid Input!"
        else:
            self.selectquery = u"SELECT EXISTS (" + self.userIdCheck + u")"
            curs.execute(self.selectquery, (target_user_id, ))
            userid_ = curs.fetchone()

            if userid_[0] == 0:
                error = "No data"
            else:
                flash("Auth Changed!")
                curs.execute(RemoveAdmin, (target_user_id, ))
                conn.commit()
        return error
