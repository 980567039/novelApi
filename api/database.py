import pymysql

Host = "localhost"
UserName = "root"
Password = "mysqltest"
database = "novel"

db = pymysql.connect(Host, UserName, Password, database)
cursor = db.cursor()