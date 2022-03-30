# https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960152#overview

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Flask RESTful and Authentication

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)

        return {"item":item}, "200" if item else "404"
    
    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": "The item already exists"}, "400"

        data = request.get_json()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return {"item": item}, "201" # 201 for created
    
    def put(self, name):
        pass


class ItemList(Resource):
    def get(self):
        return {"items": items}, "200"





api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")



app.run(port=5000, debug=True)
