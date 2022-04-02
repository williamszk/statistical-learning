import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This is field is needed."
    )

    @jwt_required()
    def get(self, name):
        # item = next(filter(lambda x: x["name"] == name, items), None)

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """
        --sql
        SELECT * FROM items WHERE name=? 
        ;
        """
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {"item": {"name": row[0], "price": row[1]}}, 200
        else:
            return {"message": "Item not found."}, 404


    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": "The item already exists"}, "400"

        data = Item.parser.parse_args()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return {"item": item}, "201"  # 201 for created

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "Item deleted"}, "200"

    @jwt_required()
    def put(self, name):
        """
        """
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            # this will make a change in the "items" object this is an implicit change
            item.update(data)
        else:
            item = {"name": name, "price": data["price"]}
            items.append(item)

        return item, "200"


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": items}, "200"