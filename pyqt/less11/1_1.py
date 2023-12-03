import sqlite3
name_db = input()

con = sqlite3.connect(name_db)
cur = con.cursor()

result = cur.execute("SELECT title FROM films WHERE year >= 1997 and genre IN (SELECT id FROM genres WHERE title = 'анимация' or title = 'музыка')").fetchall()

for elem in result:
    print(*elem)

con.close()