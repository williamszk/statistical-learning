# https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960152#overview
"""
Here we implement Flask-JWT into our API.

The ideas of using JWT is to authenticate the user to call certain APIs.

So the client needs first to have a JWT, then it needs to insert the JWT in the request.
And only then the get request (e.g.) will respond with the correponding information.

"""
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
api = Api(app)
app.secret_key = "mysecretekey"

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

app.run(port=5000, debug=True)
