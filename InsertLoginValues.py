import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "insert into logininfo values (?, ?)"
data = (("spenceta", "password"),
        ("lovelljr", "soup"))
cursor.executemany(sql, data)
conn.commit()
conn.close()
