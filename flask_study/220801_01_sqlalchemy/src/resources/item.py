from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank.")

    @jwt_required()
    def get(self, name):

        # row = ItemModel.find_by_name(name)
        item = ItemModel.find_by_name(name)

        if item:
            return {"item": item.json()}, 200

        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name: str):
        # we could create a model, class, interface for the output of this
        # function

        item = ItemModel.find_by_name(name)
        if item:
            return {'message': f"An item with name '{name}' already exists."}, 400
        try:
            data = Item.parser.parse_args()
            price = data["price"]
            item = ItemModel(name, price)
            msg = item.post_an_item()
            return msg, 200

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

        msg = item.delete_an_item()

        return msg

    @jwt_required()
    def put(self, name):
        """Used to change the price of an item.
        """

        item = ItemModel.find_by_name(name)

        if item is None:
            return {
                "message": f"Item with name '{name}' does not exist. We can't update it."}

        data = Item.parser.parse_args()

        try:
            price = data["price"]
            item = ItemModel(name, price)
            item.update(new_price=price)
            return {"message": f"Item '{name}' changed"}
        except Exception as e:
            print(e)
            return {
                "message": "Something went wrong with the server while inserting the new item"}, 500


class ItemList(Resource):
    @jwt_required()
    def get(self):

        msg = ItemModel.get_all_items()

        return msg