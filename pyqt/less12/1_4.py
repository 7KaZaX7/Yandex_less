import sqlite3
def get_result(name):
    name_db = name

    con = sqlite3.connect(name_db)
    cur = con.cursor()

    result = cur.execute("DELETE from films where title = 'Я%а'").fetchall()

    con.commit()
    con.close()