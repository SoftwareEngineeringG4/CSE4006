import pymysql

#  DEFAULT VALUES
IP_VAL = 'sw-eng-cse4006.c8qib0sqfrqd.us-east-1.rds.amazonaws.com'
USER = 'JinMyeong'
PASSWORD = 'swcse4006'
DB_NAME = 'CS_Community'
CHAR_SET = 'utf8'

#  MySQL Connection
conn = pymysql.connect(host=IP_VAL, user=USER, password=PASSWORD,
                       db=DB_NAME, charset=CHAR_SET)
print(conn)

# Connection to make cursor
curs = conn.cursor()
