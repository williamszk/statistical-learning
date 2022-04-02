from importlib.metadata import requires
import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

    @classmethod # class methods are used in situations where we don't need information specific of the instance, but we use the class
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """
        --sql
        SELECT * FROM users WHERE username=? 
        ;
        """

        result = cursor.execute(query, (username,)) # the argument for the ? needs to be a tuple and for a single tuple we need to use (item,)

        row = result.fetchone() # take the first row of the results, I imagine that results is an generator
        
        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()

        return user
    
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """
        --sql
        SELECT * FROM users WHERE id=? 
        ;
        """

        result = cursor.execute(query, (_id,))

        row = result.fetchone()
        
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        
        connection.close()

        return user


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data["username"]):
            return {"message": f"A user with username '{data['username']}' already exists."}, 400


        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """
        --sql
        INSERT INTO users VALUES (NULL, ?, ?) 
        ;
        """
        
        cursor.execute(query, (data["username"], data["password"]))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201

