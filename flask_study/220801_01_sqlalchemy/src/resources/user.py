from flask_restful import Resource, reqparse
from models.user import UserModel


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

        username = data["username"]
        password = data["password"]

        user = UserModel(username, password)
        msg = user.register()

        # 201 means created
        return msg, 201
    
