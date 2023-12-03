import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    cursor.execute(
        """DELETE from films where duration > 90 AND genre = (SELECT id FROM genres 
        WHERE title = 'фантастика') AND year < 2000"""
    )

    conn.commit()
    conn.close()