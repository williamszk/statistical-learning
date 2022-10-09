
import sqlite3

connection = sqlite3.connect("./db.sqlite")

cursor = connection.cursor()

# create users table
create_table_users = """ --sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);
"""
cursor.execute(create_table_users)

# create default user
create_default_user = """--sql
INSERT INTO users VALUES (NULL, ?, ?);
"""
cursor.execute(create_default_user, ("admin", "password"))


# create users table
create_table_items = """ --sql
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL 
);
"""
cursor.execute(create_table_items)


connection.commit()
connection.close()
