import sqlite3
DATABASE_NAME = "data.db"


class User:
    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        query = """
        --sql
        SELECT * FROM users WHERE username=? 
        ;
        """

        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()

        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        query = """
        --sql
        SELECT * FROM users WHERE id=?
        ;
        """

        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        return user
