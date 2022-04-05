import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = """
--sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, -- we need to use INTEGER to make this autoincrementing columns
    username text,
    password text
) 
;
"""

cursor.execute(create_table)

connection.commit()

connection.close()

