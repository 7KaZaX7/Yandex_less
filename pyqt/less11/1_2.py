import sqlite3
name_db = input()

con = sqlite3.connect(name_db)
cur = con.cursor()
name = '2000'
result = cur.execute("""SELECT title FROM films
            WHERE title like name""").fetchall()

for elem in result:
    print(*elem)

con.close()