import sqlite3


class ItemModel:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    def insert(self):
        connection = sqlite3.connect("../data.db")
        cursor = connection.cursor()

        query = """ --sql
        INSERT INTO items VALUES (NULL, ?, ?);
        """
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect("../data.db")
        cursor = connection.cursor()

        query = """ --sql
        UPDATE items SET price=? WHERE name=?;
        """
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()

    def delete(self):
        connection = sqlite3.connect("../data.db")
        cursor = connection.cursor()

        query = """ --sql
        DELETE FROM items WHERE name=?;
        """
        cursor.execute(query, (self.name,))

        connection.commit()
        connection.close()
    
def get_all_items():
    connection = sqlite3.connect("../data.db")
    cursor = connection.cursor()

    query = """ --sql
    SELECT * FROM items;
    """

    items = []
    for row in cursor.execute(query):
        name = row[1]
        price = row[2]
        item = ItemModel(name, price).json()
        items.append(item)

    connection.close()

    return items


def find_by_name(name: str) -> ItemModel:
    connection = sqlite3.connect("../data.db")
    cursor = connection.cursor()

    query = """ --sql
    SELECT * FROM items WHERE name=?;
    """
    row = cursor.execute(query, (name,)).fetchone()
    connection.close()

    if row:
        price = row[2]
        item_instance = ItemModel(name, price)
        return item_instance

    else:
        return None
