import sqlite3
name_db = input()

con = sqlite3.connect(name_db)
cur = con.cursor()

result = cur.execute("""SELECT title FROM films
            WHERE duration <= 85""").fetchall()

for elem in result:
    print(*elem)

con.close()