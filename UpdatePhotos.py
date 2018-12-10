import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = '''update celebs set photo=replace(photo,'nphinity','software4rfid')'''
cursor.execute(sql)
conn.commit()
conn.close()
