import sqlite3
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be blank"
                        )

    @jwt_required()
    def get(self, name):

        item = self.find_by_name(name)
        if item:
            return item
        return {"message": "Item not found"}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        # item = next(filter(lambda x: x["name"] == name, items), None)
        # return {"item": item}, 200 if item else 404
        query = """--sql
        SELECT * FROM items WHERE  name=?;
        """
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()
        if row:
            return {"item": {"name": row[0], "price": row[1]}}

    @jwt_required()
    def post(self, name):
        if self.find_by_name(name):
            return {"message": f"An item with name '{name}' already exists."}, 400

        data = request.get_json()

        item = {"name": name, "price": data["price"]}
        try:
            self.insert(item)
        except Exception as e:
            print(e)
            # if this error occurs it is not the client's mistake
            # it is the server's error "Internal Server Error"
            return {"message": "An error occurred inserting the item."}, 500

        return item, 201  # 201 is for "created"

    @classmethod
    def insert(cls, item):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """--sql
        INSERT INTO items VALUES (?, ?);
        """
        cursor.execute(query, (item["name"], item["price"]))
        connection.commit()
        connection.close()

        return item

    def delete(self, name):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """--sql
        DELETE FROM items WHERE name=?;
        """
        cursor.execute(query, (name,))
        connection.close()

        return {"message": "Item deleted"}

    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        update_item = {"name": name, "price": data["price"]}

        if item is None:
            try:
                self.insert(update_item)
            except Exception as e:
                print(e)
                return {"message": "An error occurred inserting the item."}, 500
        else:
            try:
                self.update(update_item)
            except Exception as e:
                print(e)
                return {"message": "An error occurred updating the item."}, 500
            
        return update_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """--sql
        UPDATE items SET price=? WHERE name=?;
        """
        cursor.execute(query, (item["price"], item["name"]))
        connection.close()

        return {"message": "Item deleted"}


class ItemList(Resource):
    @jwt_required()
    def get(self):
        try:
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()

            query = """--sql
            SELECT * FROM items;
            """
            # cursor.execute(query)
            # items = cursor.fetchall()
            result = cursor.execute(query)
            items = []
            for row in result:
                items.append({"name": row[0], "price": row[1]})

            connection.close()
        except Exception as e:
            print(e)
            return {"message": "An error occurred while getting all the item."}, 500

        return {"items": items}, 200
