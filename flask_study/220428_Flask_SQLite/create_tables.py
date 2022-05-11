# https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/5965498#overview

import sqlite3
from venv import create

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = """ --sql
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text);
"""
# note that in sqlite the type comes after the name of the field
# and for auto increment we need to use INTEGER instead of just int
cursor.execute(create_table)

create_table = """ --sql
CREATE TABLE IF NOT EXISTS items (name text, price real);
"""
cursor.execute(create_table)


connection.commit()

connection.close()
