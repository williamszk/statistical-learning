
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models import item as it


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank.")

    @jwt_required()
    def get(self, name):
        item_instance = it.find_by_name(name)
        if item_instance:
            item = item_instance.json()
            return {"item": item}, 200

        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name: str):
        item_instance = it.find_by_name(name)
        if item_instance:
            return {'message': f"An item with name '{name}' already exists."}, 400
        try:
            data = Item.parser.parse_args()
            item_instance = it.ItemModel(name, data["price"])
            item_instance.insert()
            item = item_instance.json()
            return item, 200

        except Exception as e:
            print(e)
            return {"message": "Something went wrong with the server while inserting the new item"}, 500

    @jwt_required()
    def delete(self, name):
        item_instance = it.find_by_name(name)
        if item_instance is None:
            return {"message": f"Item with name '{name}' does not exist. We can't delete it."}

        item_instance.delete()

        return {"message": f"Item '{item_instance.name}' deleted"}

    @jwt_required()
    def put(self, name):
        """Used to change the price of an item.
        """
        item_instance = it.find_by_name(name)
        if item_instance is None:
            return {"message": f"Item with name '{name}' does not exist. We can't update it."}

        data = Item.parser.parse_args()

        try:
            item_instance = it.ItemModel(name, data["price"])
            item_instance.update()
            return {"message": f"Item '{name}' changed"}
        except Exception as e:
            print(e)
            return {"message": "Something went wrong with the server while inserting the new item"}, 500


class ItemList(Resource):
    @jwt_required()
    def get(self):

        items = it.get_all_items()

        return {'items': items}
