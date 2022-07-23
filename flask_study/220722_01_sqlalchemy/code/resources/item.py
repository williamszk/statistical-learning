from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models import item as it
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank.")

    @jwt_required()
    def get(self, name):
        item_instance = ItemModel.find_by_name(name)
        if item_instance:
            item = item_instance.json()
            return {"item": item}, 200

        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name: str):

        data = Item.parser.parse_args()
        item_instance = ItemModel(name, data["price"])
        item_instance.save_to_db()
        return item_instance.json(), 200

    @jwt_required()
    def delete(self, name):
        item_instance = ItemModel.find_by_name(name)
        if item_instance is None:
            return {"message": f"Item with name '{name}' does not exist. We can't delete it."}

        item_instance.delete_from_db()

        return {"message": f"Item '{item_instance.name}' deleted"}

    @jwt_required()
    def put(self, name):
        """Used to change the price of an item.
        """
        data = Item.parser.parse_args()

        item_instance = ItemModel.find_by_name(name)
        if item_instance is None:
            # return {"message": f"Item with name '{name}' does not exist. We can't update it."}
            item_instance = ItemModel(name, data["price"]) 
        else:
            item_instance.price = data["price"]

        try:
            item_instance.save_to_db()
            return item_instance.json(), 200
        except Exception as e:
            print(e)
            return {"message": "Something went wrong with the server while inserting the new item"}, 500


class ItemList(Resource):
    @jwt_required()
    def get(self):

        items = ItemModel.get_all_items()
        items_json = [x.json() for x in items]

        return {'items': items_json}, 200
