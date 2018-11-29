from dbconn import curs


class CheckPWDDup:

    passwd = 0
    
    
    def __init__(self, passwd):
        self.passwd = passwd
        
    def AlreadyInDB():
        curs.execute(sql)
        
    def CheckDup():
        return ""
        
