import sqlite3
name_db = input()

con = sqlite3.connect(name_db)
cur = con.cursor()

result = cur.execute("""SELECT title FROM films
            WHERE (year BETWEEN 1995 AND 2000) and 
                     (genre = (SELECT id FROM genres WHERE title = 'детектив'))""").fetchall()

for elem in result:
    print(*elem)

con.close()