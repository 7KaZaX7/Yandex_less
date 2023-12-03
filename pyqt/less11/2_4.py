import sqlite3
name_db = input()

con = sqlite3.connect(name_db)
cur = con.cursor()

result = cur.execute("""SELECT title FROM films
            WHERE title LIKE '%Астерикс%' and title not LIKE '%Обеликс%'""").fetchall()

for elem in result:
    print(*elem)

con.close()