from dotenv import dotenv_values
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


secrets_dotenv = dotenv_values(".env")

app = Flask(__name__)
app.secret_key = secrets_dotenv["SECRETKEY"]
api = Api(app)

jwt = JWT(app, authenticate, identity)  # creates a new endpoint, "/auth" POST
# when we call /auth the username and password variables are passed to the authenticate function
# and the function returns the "user"
# And then the endpoint sends a JWT (JSON Web Token)
# we need to use this token to call other endpoints
# this is how we establish authentication using password and username
# When we use JWT in other endpoint, the jwt object uses the identity()
# function. It uses the payload that has the JWT and sees if it matches
# an internal map of tokens and users, if they match then it allows the
# endpoint to be called.

# Flask JWT made the process of authentication easier.
#

# https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960168#overview

items = []


class Item(Resource):

    # given that we include parser in the level of the class
    # every instance of this class will have the same parser
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True,
                        help="This field cannot be left blank")
    # if we only keep "price", any other field will be erased from the parse_args

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404
        # return (item, 200) if item else ({"Item": None}, 404)

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": f"An item with name '{name}' already exists."}, 400

        data = Item.parser.parse_args()
        # data = request.get_json()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201  # 201 is for "created"

    def delete(self, name):
        global items
        # if we don't use global here we get an error
        # because python will think that items is being created for the first time here
        # and it can't use items inside its own definition
        # UnboundLocalError: local variable 'items' referenced before assignment

        items = list(filter(lambda x: x["name"] != name, items))

        return {"message": "Item deleted"}

    def put(self, name):
        if len(items) == 0:
            return {"message": "the list 'items' is empty"}, 400

        data = Item.parser.parse_args()
        # data = request.get_json()
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item is None:
            item = {"name": data["name"], "price": data["price"]}
            items.append(item)
        else:
            item.update(data)
            # give that item comes from items
            # item is referencing to an object inside items
            # then if we change item
            # we'll change items
        return item


class ItemList(Resource):
    def get(self):
        return {"items": items}, 200


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)
