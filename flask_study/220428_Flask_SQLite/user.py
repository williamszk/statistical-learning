import sqlite3
from flask import request
from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """ --sql
        SELECT * FROM users WHERE username=?;
        """

        # user_data = next(cursor.execute(query, (username,)), None)
        row = cursor.execute(query, (username,)).fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        # no need to commit

        return user

    @classmethod
    def find_by_userid(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """
        --sql
        SELECT * FROM users WHERE id=?;
        """

        row = cursor.execute(query, (_id,)).fetchone()

        connection.close()

        if row:
            user = cls(*row)
        else:
            user = None

        return user


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True,
                        help="This field cannot be blank.")
    parser.add_argument("password", type=str, required=True,
                        help="This field cannot be blank.")

    def post(self):
        # data = request.get_json()
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data["username"]):
            return {"message": "A user with that username already exists"}, 400

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        username = data["username"]
        password = data["password"]

        query = """ --sql
        INSERT INTO users VALUES (NULL,?,?);
        """
        # id, username, password
        # the id is autoincrementing so we'll it to NULL
        cursor.execute(query, (username, password))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}
        # this method doesn't check if the username already exists...
