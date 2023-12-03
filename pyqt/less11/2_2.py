import sqlite3
name_db = input()

con = sqlite3.connect(name_db)
cur = con.cursor()

result = cur.execute("""SELECT title FROM genres WHERE id IN (SELECT genre FROM films
            WHERE year IN (2010, 2011))""").fetchall()

for elem in set(result):
    print(*elem)

con.close()