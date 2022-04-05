import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = """
    --begin-sql
    CREATE TABLE users (
        id int,
        username text,
        password text
    )
    -- this defines the schema
;
"""
cursor.execute(create_table)

user = (1, "jose", "asdf")

insert_query = """
--sql
    INSERT INTO users VALUES (?, ?, ?)
;
"""
# the cursor is smart enough to substitute the ? with the values in the tuple
cursor.execute(insert_query, user)

users = [
    (2, "rolf", "asdf"),
    (3, "anne", "xyz")
]
# executemany will execute the insert_query many times
cursor.executemany(insert_query, users)


select_query = """
--sql
    SELECT * FROM users
;
"""
for row in cursor.execute(select_query):
    print(row)

# when we insert data we need to commit the changes
connection.commit()

connection.close()
