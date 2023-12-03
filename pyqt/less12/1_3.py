import sqlite3
def get_result(name):
    name_db = name

    con = sqlite3.connect(name_db)
    cur = con.cursor()

    result = cur.execute("UPDATE films SET duration = duration*2 WHERE genre = (SELECT id FROM genres WHERE title = 'фантастика')").fetchall()

    con.commit()
    con.close()