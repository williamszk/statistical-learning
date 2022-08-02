import sqlite3


class ItemModel:

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def json(self):
        return {
            "name": self.name,
            "price": self.price
        }

    @classmethod
    def get_all_items(cls):
        connection = sqlite3.connect("../data.sqlite")
        cursor = connection.cursor()

        query = """ --sql
        SELECT * FROM items;
        """

        items = []
        for row in cursor.execute(query):
            name = row[1]
            price = row[2]
            item = cls(name, price).json()
            items.append(item)

        connection.close()
        return {'items': items}

    @classmethod
    def find_by_name(cls, name: str):

        connection = sqlite3.connect("../data.sqlite")
        cursor = connection.cursor()

        query = """ --sql
        SELECT * FROM items WHERE name=?;
        """

        # querydata = next(cursor.execute(query, (name,)), None)
        row = cursor.execute(query, (name,)).fetchone()
        connection.close()

        if row is None:
            return None

        price = row[2]

        return cls(name, price)

    def post_an_item(self):

        connection = sqlite3.connect("../data.sqlite")
        cursor = connection.cursor()

        query = """ --sql
        INSERT INTO items VALUES (NULL, ?, ?) ;
        """

        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()

        return {'name': self.name, 'price': self.price}

    def delete_an_item(self):

        connection = sqlite3.connect("../data.sqlite")
        cursor = connection.cursor()

        query = """ --sql
        DELETE FROM items WHERE name=?;
        """

        cursor.execute(query, (self.name,))

        connection.commit()
        connection.close()

        return {"message": f"Item '{self.name}' deleted"}

    def update(self, new_price: float):

        connection = sqlite3.connect("../data.sqlite")
        cursor = connection.cursor()

        query = """ --sql
        UPDATE items SET price=? WHERE name=?;
        """
        cursor.execute(query, (new_price, self.name))

        connection.commit()
        connection.close()

        return {"message": "price updated"}
