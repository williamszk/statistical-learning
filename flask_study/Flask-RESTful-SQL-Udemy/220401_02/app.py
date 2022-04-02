# https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960152#overview
"""
Here we implement Flask-JWT into our API.

The ideas of using JWT is to authenticate the user to call certain APIs.

So the client needs first to have a JWT, then it needs to insert the JWT in the request.
And only then the get request (e.g.) will respond with the correponding information.

"""
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
api = Api(app)
app.secret_key = "mysecretekey"

jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This is field is needed."
    )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)

        return {"item": item}, "200" if item else "404"

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": "The item already exists"}, "400"

        data = Item.parser.parse_args()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return {"item": item}, "201"  # 201 for created

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "Item deleted"}, "200"

    @jwt_required()
    def put(self, name):
        """
        """
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            # this will make a change in the "items" object this is an implicit change
            item.update(data)
        else:
            item = {"name": name, "price": data["price"]}
            items.append(item)

        return item, "200"


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": items}, "200"


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

app.run(port=5000, debug=True)
