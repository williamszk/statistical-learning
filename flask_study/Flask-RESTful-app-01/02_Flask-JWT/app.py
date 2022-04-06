# https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960152#overview
"""
Here we implement Flask-JWT into our API.

The ideas of using JWT is to authenticate the user to call certain APIs.

So the client needs first to have a JWT, then it needs to insert the JWT in the request.
And only then the get request (e.g.) will respond with the correponding information.

"""
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = "mysecretekey" # this in production should be in a secret file, not commited

jwt = JWT(app, authenticate, identity) # JWT will create a new endpoint called /auth
# can we use a custom endpoint instead of /auth for authentication?

# Flask RESTful and Authentication

items = []

class Item(Resource):
    @jwt_required() # with this decorator we need to authenticate first before being able to call this endpoint
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)

        return {"item":item}, "200" if item else "404"
    
    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": "The item already exists"}, "400"

        data = request.get_json()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return {"item": item}, "201" # 201 for created
    
    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "Item deleted"}, "200"

    @jwt_required()
    def put(self, name):
        """
        The implementation of the put request should be idempotent
        that is, if we make the request multiple times in a row
        the result should be the same as if we made it once.
        This behavior should be implemented in the code.
        """
        data = request.get_json()
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            item.update(data) # this will make a change in the "items" object this is an implicit change
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



app.run(port=5000, debug=True)
