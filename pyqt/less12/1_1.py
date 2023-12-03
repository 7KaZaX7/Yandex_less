import sqlite3
def get_result(name):
    name_db = name

    con = sqlite3.connect(name_db)
    cur = con.cursor()

    result = cur.execute("DELETE from films WHERE genre = (SELECT id FROM genres WHERE title = 'комедия')").fetchall()

    con.commit()
    con.close()

get_result("films_db.sqlite")