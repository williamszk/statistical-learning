# https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960152#overview

from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

# Flask RESTful and Authentication

items = []

class Item(Resource):
    def get(self, name):
        found_item = next(filter(lambda x: x["name"] == name, items), None)
        if found_item:
            return found_item
        else:
            return {"Error": "Item not found."}, "400-10"
    
    def post(self, name):
        item = {"name": name, "price": 12.99}
        items.append(item)
        return item
    
    def put(self, name):
        pass



api.add_resource(Item, "/item/<string:name>")




app.run(port=5000, debug=True)


# fail