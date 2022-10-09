import sqlite3


class ItemModel:

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(cls, name: str) -> "ItemModel":

        connection = sqlite3.connect("./db.sqlite")
        cursor = connection.cursor()

        query = """ --sql
        SELECT * FROM items WHERE name=?;
        """
        # querydata = next(cursor.execute(query, (name,)), None)
        row = cursor.execute(query, (name,)).fetchone()
        connection.close()

        if row:
            item = cls(name, row[2])
            # item = cls(*row)
            return item

        return None

    def update(self):
        connection = sqlite3.connect("./db.sqlite")
        cursor = connection.cursor()

        query = """--sql
        UPDATE items SET price=? WHERE name=?;
        """
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()

    def insert(self) -> None:
        connection = sqlite3.connect("./db.sqlite")
        cursor = connection.cursor()

        query = """ --sql
        INSERT INTO items VALUES (NULL, ?, ?) ;
        """

        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()

    def delete(self):
        connection = sqlite3.connect("./db.sqlite")
        cursor = connection.cursor()

        query = """ --sql
        DELETE FROM items WHERE name=?;
        """

        cursor.execute(query, (self.name,))

        connection.commit()
        connection.close()

    @classmethod
    def get_all(cls) -> list["ItemModel"]:
        connection = sqlite3.connect("./db.sqlite")
        cursor = connection.cursor()
        query = """ --sql
        SELECT * FROM items;
        """
        items = []
        for row in cursor.execute(query):
            item = cls(row[1], row[2])
            items.append(item)

        connection.close()

        return items
