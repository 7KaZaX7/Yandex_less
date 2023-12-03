import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE films SET duration = '100' WHERE genre = (SELECT id FROM genres 
        WHERE title = 'мюзикл') AND duration > 100"""
    )

    conn.commit()
    conn.close()