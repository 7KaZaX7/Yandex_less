import sqlite3
name_db = input()

con = sqlite3.connect(name_db)
cur = con.cursor()

result = cur.execute("""SELECT year FROM films
            WHERE title LIKE 'Х%'""").fetchall()

for i in set([*result]):
    print(*i)
con.close()