import sqlite3
name_db = input()

con = sqlite3.connect(name_db)
cur = con.cursor()

result = cur.execute("""SELECT title FROM films
            WHERE duration >= 60 and genre = (SELECT id FROM genres WHERE title = 'комедия')""").fetchall()

for elem in result:
    print(*elem)

con.close()