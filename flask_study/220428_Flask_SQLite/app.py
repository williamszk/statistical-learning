from dotenv import dotenv_values
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister

from item import Item, ItemList



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


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
