import sqlite3


class UserModel(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_id(cls, id: int) -> "UserModel":
        connection = sqlite3.connect("./db.sqlite")
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

    @classmethod
    def find_by_username(cls,username: str) -> "UserModel":
        connection = sqlite3.connect("./db.sqlite")
        cursor = connection.cursor()
        query = """--sql
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
    
    def insert(self):
        connection = sqlite3.connect("./db.sqlite")
        cursor = connection.cursor()

        query = """--sql
        INSERT INTO users VALUES (NULL, ?, ?);
        """

        cursor.execute(query, (self.username, self.password))

        connection.commit()
        connection.close()
