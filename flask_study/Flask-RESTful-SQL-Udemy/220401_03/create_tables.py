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


create_table = """
--sql
CREATE TABLE IF NOT EXISTS items (
    name text,
    price real
) 
;
"""

cursor.execute(create_table)

cursor.execute("""
--sql
INSERT INTO items VALUES ("test", 10.99) 
;
""")


connection.commit()

connection.close()
