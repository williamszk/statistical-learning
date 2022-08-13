import sqlite3


class UserModel(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        connection = sqlite3.connect("../data.sqlite")
        cursor = connection.cursor()

        query = """--sql
        INSERT INTO users VALUES (NULL, ?, ?);
        """

        cursor.execute(query, (self.username, self.password))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}

    @classmethod
    def find_by_id(cls, id: int) -> "UserModel":

        connection = sqlite3.connect("../data.sqlite")
        cursor = connection.cursor()
        query = """--sql
        SELECT * FROM users WHERE id=?;
        """
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        connection.close()

        if row:
            username = row[1]
            password = row[2]

            return cls(username, password)

        else:
            return None


        return user

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":

        connection = sqlite3.connect("../data.sqlite")
        cursor = connection.cursor()
        query = """--sql
        SELECT * FROM users WHERE username=?;
        """

        result = cursor.execute(query, (username,))
        row = result.fetchone()
        connection.close()

        if row:
            password = row[2]

            return cls(username, password)
        else:
            return None

