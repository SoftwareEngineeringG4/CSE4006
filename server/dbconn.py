import pymysql

#  DEFAULT VALUES
IP_VAL = 'sw-eng-cse4006.c8qib0sqfrqd.us-east-1.rds.amazonaws.com'
USER = 'JinMyeong'
PASSWORD = 'swcse4006'
DB_NAME = 'CS_Community'
CHAR_SET = 'utf8'

#  MySQL Connection 연결
conn = pymysql.connect(host=IP_VAL, user=USER, password=PASSWORD,
                       db=DB_NAME, charset=CHAR_SET)
print(conn)

# Connection 으로부터 Cursor 생성
curs = conn.cursor()
