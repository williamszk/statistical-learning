
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank."
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json(), 200

        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name: str):

        item = ItemModel.find_by_name(name)
        if item:
            return {'message': f"An item with name '{name}' already exists."}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data["price"])
        try:
            item.insert()

            return item.json(), 200

        except Exception as e:
            print(e)
            return {
                "message": "Something went wrong with the server while inserting the new item"}, 500

    @jwt_required()
    def delete(self, name):

        item = ItemModel.find_by_name(name)
        if item is None:
            return {
                "message": f"Item with name '{name}' does not exist. We can't delete it."}

        item.delete()

        return {"message": f"Item '{name}' deleted"}

    @jwt_required()
    def put(self, name):
        """Used to change the price of an item.
        """
        data = Item.parser.parse_args()
        price = data["price"]

        item = ItemModel.find_by_name(name)
        if item is None:
            try:
                item = ItemModel(name, price)
                item.insert()
                return item.json(), 201
            except Exception as e:
                print(e)
                return {"message": "An error happened while inserting this item."}
        try:
            item = ItemModel(name, price)
            item.update()
            return {"message": f"Item '{name}' changed"}
        except Exception as e:
            print(e)
            return {
                "message": "Something went wrong with the server while inserting the new item"}, 500


class ItemList(Resource):
    @jwt_required()
    def get(self):
        items = ItemModel.get_all()
        return {"items": [x.json() for x in items]}
