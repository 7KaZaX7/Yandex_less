import sqlite3

def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("UPDATE films SET duration = duration / 2 WHERE year = '1973'")
    conn.commit()
    conn.close()