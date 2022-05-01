import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

# create a table in database -----------------

create_table = """
--sql
CREATE TABLE users (id int, username text, password text) 
;
"""

cursor.execute(create_table)

# insert a record into the database -----------------

user = (1, "Jose", "asdf")

insert_query = """
--sql
INSERT INTO users VALUES (?, ?, ?) 
;
"""
# we can just include the tuple "user" at the end
# of the execute function
# and the query will understand the position
# of the arguments
cursor.execute(insert_query, user)


# insert a list of tuples -------------------------

users = [
    (2, "Rolf", "asdf"),
    (3, "Anne", "xyz")
]


cursor.executemany(insert_query, users)

# to retrieve the data back -------------------------
select_query = """
--sql
SELECT * FROM users 
;
"""
select_generator = cursor.execute(select_query)
for row in select_generator:
    print(row)

# this will make the database know that we want to save
# the changes that we made
connection.commit()

connection.close()
