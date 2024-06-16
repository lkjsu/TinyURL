'''manage.py - Handles db migrations'''

import db


migrations = [
    """
        CREATE TABLE IF NOT EXISTS tinyurl (
            id BLOB PRIMARY KEY,
            original_url BLOB,
            short_url, BLOB,
            timestamp INTEGER,
            user_id BLOB
        )
    """

]


with db.sqlite3.connect(db.Db().db) as connection:
    cursor = connection.cursor()
    for cmd in migrations:
        cursor.execute(cmd)

