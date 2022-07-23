import sqlite3
from db import db

# Each table in the database should have a model
# and the model should inherit from sqlalchemy

class UserModel(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


def find_by_id(id: int) -> UserModel:
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    query = """--sql
    SELECT * FROM users WHERE id=?;
    """
    result = cursor.execute(query, (id,))
    row = result.fetchone()
    if row:
        user = UserModel(*row)
    else:
        user = None

    connection.close()

    return user


def find_by_username(username: str) -> UserModel:
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    query = """
    SELECT * FROM users WHERE username=?;
    """
    result = cursor.execute(query, (username,))
    row = result.fetchone()
    if row:
        user = UserModel(*row)
    else:
        user = None

    connection.close()

    return user
