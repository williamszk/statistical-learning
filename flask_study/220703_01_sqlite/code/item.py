
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from typing import Union

QueryOuput = Union[tuple, None]

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank."
                        )

    @jwt_required()
    def get(self, name):

        row = find_by_name(name)

        if row:
            item = {
                "name": row[1],
                "price": row[2],
            }
            return {"item": item}, 200

        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name: str):
        # we could create a model, class, interface for the output of this function

        row = find_by_name(name)
        if row:
            return {'message': f"An item with name '{name}' already exists."}, 400

        data = Item.parser.parse_args()

        connection = sqlite3.connect("../data.db")
        cursor = connection.cursor()

        query = """ --sql
        INSERT INTO items VALUES (NULL, ?, ?) ;
        """

        price = data["price"]
        cursor.execute(query, (name, price))

        connection.commit()
        connection.close()

        item = {'name': name, 'price': data['price']}

        return item, 200

    @jwt_required()
    def delete(self, name):

        # maybe we should include a check to see if item exists
        if find_by_name(name) is None:
            return {"message": f"Item with name '{name}' does not exist. We can't delete it."}

        connection = sqlite3.connect("../data.db")
        cursor = connection.cursor()

        query = """ --sql
        DELETE FROM items WHERE name=?;
        """

        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {"message": f"Item '{name}' deleted"}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect("../data.db")
        cursor = connection.cursor()

        query = """ --sql
        SELECT * FROM items;
        """

        items = []
        for row in cursor.execute(query):
            item = {
                "name": row[1],
                "price": row[2],
            }
            items.append(item)
       
        connection.close()
        return {'items': items}


def find_by_name(name: str) -> QueryOuput:

    connection = sqlite3.connect("../data.db")
    cursor = connection.cursor()

    query = """ --sql
    SELECT * FROM items WHERE name=?;
    """

    # querydata = next(cursor.execute(query, (name,)), None)
    row = cursor.execute(query, (name,)).fetchone()

    connection.close()

    return row
