import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "insert into members values (?, ?, ?, ?, ?, ?)"
data = ((1, "Joshua", "Lovell", 20, "josh.lovell98@gmail.com", "Born in Baltimore City"),
        (2, "Tristen", "Spencer", 21, "spenceta@dukes.jmu.edu", "Born in Virginia Beach"),
       cursor.executemany(sql, data)
conn.commit()
conn.close()
