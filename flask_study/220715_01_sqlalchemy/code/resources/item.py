
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models import item as it

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank.")

    @jwt_required()
    def get(self, name):

        row = it.find_by_name(name)

        if row:
            item = it.ItemModel(*row).json()

            return {"item": item}, 200

        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name: str):
        # we could create a model, class, interface for the output of this function

        row = it.find_by_name(name)
        if row:
            return {'message': f"An item with name '{name}' already exists."}, 400

        try:
            data = Item.parser.parse_args()

            it.insert_new_item(name, data["price"])

            item = it.ItemModel(name, data["price"]).json()

            return item, 200

        except Exception as e:
            # we should log e
            print(e)
            return {"message": "Something went wrong with the server while inserting the new item"}, 500

    @jwt_required()
    def delete(self, name):

        if it.find_by_name(name) is None:
            return {"message": f"Item with name '{name}' does not exist. We can't delete it."}

        # create function here

        connection = sqlite3.connect("../data.db")
        cursor = connection.cursor()

        query = """
        DELETE FROM items WHERE name=?;
        """

        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {"message": f"Item '{name}' deleted"}

    @jwt_required()
    def put(self, name):
        """Used to change the price of an item.
        """
        if it.find_by_name(name) is None:
            return {"message": f"Item with name '{name}' does not exist. We can't update it."}

        data = Item.parser.parse_args()

        try:
            it.update(name, data["price"])
            return {"message": f"Item '{name}' changed"}
        except Exception as e:
            # log e
            return {"message": "Something went wrong with the server while inserting the new item"}, 500


class ItemList(Resource):
    @jwt_required()
    def get(self):

        # create function here

        connection = sqlite3.connect("../data.db")
        cursor = connection.cursor()

        query = """
        SELECT * FROM items;
        """

        items = []
        for row in cursor.execute(query):
            item = it.ItemModel(*row).json()
            items.append(item)

        connection.close()

        return {'items': items}
