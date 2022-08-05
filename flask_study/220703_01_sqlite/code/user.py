import sqlite3
from flask_restful import Resource, reqparse


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


def find_by_id(id: int) -> User:
    connection = sqlite3.connect("../data.db")
    cursor = connection.cursor()
    query = """--sql
    SELECT * FROM users WHERE id=?;
    """
    result = cursor.execute(query, (id,))
    row = result.fetchone()
    if row:
        user = User(*row)
    else:
        user = None

    connection.close()

    return user


def find_by_username(username: str) -> User:
    connection = sqlite3.connect("../data.db")
    cursor = connection.cursor()
    query = """--sql
    SELECT * FROM users WHERE username=?;
    """
    result = cursor.execute(query, (username,))
    row = result.fetchone()
    if row:
        user = User(*row)
    else:
        user = None

    connection.close()

    return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True,
                        help="This field cannot be left blank.")
    parser.add_argument("password", type=str, required=True,
                        help="This field cannot be left blank.")

    def post(self):

        data = UserRegister.parser.parse_args()

        if find_by_username(data["username"]):
            return {"error": "A user with that username already registered."}, 400

        connection = sqlite3.connect("../data.db")
        cursor = connection.cursor()

        query = """--sql
        INSERT INTO users VALUES (NULL, ?, ?);
        """

        cursor.execute(query, (data["username"], data["password"]))

        connection.commit()
        connection.close()
        # 201 means created
        return {"message": "User created successfully."}, 201
