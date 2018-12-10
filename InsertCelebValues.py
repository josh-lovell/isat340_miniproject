import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "insert into celebs values (?, ?, ?, ?, ?, ?, ?)"
data = ((1, "Angelina", "Jolie", 40, "angie@hollywood.us", "http://www.nphinity.com/pics/aj.jpg", "Acted in Mr. and Mrs. Smith"),
        (2, "Brad", "Pitt", 51, "brad@hollywood.us", "http://www.nphinity.com/pics/bp.jpg", "Owns Plan B Entertainment"),
        (3, "Snow", "White", 21, "sw@disney.org", "http://www.nphinity.com/pics/sw.jpg", "Lives with seven dwarfs"),
        (4, "Darth", "Vader", 29, "dv@darkside.me", "http://www.nphinity.com/pics/dv.jpg", "Luke's father"),
        (5, "Taylor", "Swift", 25, "ts@1989.us", "http://www.nphinity.com/pics/ts.jpg", "First hit song was 'Tim McGraw' released by Big Machine Records"),
        (6, "Beyonce", "Knwoles", 34, "beyonce@jayz.me", "http://www.nphinity.com/pics/bk.jpg", "Married to Shawn Corey Carter"),
        (7, "Selena", "Gomez", 23, "selena@hollywood.us", "http://www.nphinity.com/pics/sg.jpg", "Formerly acted in Wizards of Waverly Place"),
        (8, "Stephen", "Curry", 27, "steph@golden.bb", "http://www.nphinity.com/pics/sc.jpg", "Plays for the Golden State Warriors"))
cursor.executemany(sql, data)
conn.commit()
conn.close()
