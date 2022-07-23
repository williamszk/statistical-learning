import sqlite3
from flask_restful import Resource, reqparse
from models.user import find_by_username


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

        query = """
        INSERT INTO users VALUES (NULL, ?, ?);
        """

        cursor.execute(query, (data["username"], data["password"]))

        connection.commit()
        connection.close()
        # 201 means created
        return {"message": "User created successfully."}, 201
