import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "create table logininfo(username text PRIMARY KEY, password text)"
cursor.execute(sql)
conn.commit()
conn.close()
