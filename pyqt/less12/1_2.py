import sqlite3
def get_result(name):
    name_db = name

    con = sqlite3.connect(name_db)
    cur = con.cursor()

    result = cur.execute("UPDATE films SET duration = '42' WHERE duration = '0'").fetchall()

    con.commit()
    con.close()