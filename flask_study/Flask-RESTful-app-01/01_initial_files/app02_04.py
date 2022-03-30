from flask import Flask
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

# Flask RESTful and Authentication

items = []

class CustomApi(Api):
    def handle_error(self, e):
        abort(e.code, str(e))


class Item(Resource):
    def get(self):
        found_item = None
        if found_item:
            return found_item
        else:
            # https://flask-restful.readthedocs.io/en/latest/api.html#flask_restful.abort
            return {"Error": "Item not found."}, "400-10"
            # abort("400")


api.add_resource(Item, "/")




app.run(port=5000, debug=True)

# fail