import sqlite3
from typing import Union

QueryOuput = Union[tuple, None]


class ItemModel:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}


def find_by_name(name: str) -> QueryOuput:

    connection = sqlite3.connect("../data.db")
    cursor = connection.cursor()

    query = """
    SELECT * FROM items WHERE name=?;
    """

    row = cursor.execute(query, (name,)).fetchone()

    connection.close()

    return row


def update(name, price):
    connection = sqlite3.connect("../data.db")
    cursor = connection.cursor()

    query = """
    UPDATE items SET price=? WHERE name=?;
    """
    cursor.execute(query, (price, name))

    connection.commit()
    connection.close()


def insert_new_item(name, price):

    connection = sqlite3.connect("../data.db")
    cursor = connection.cursor()

    query = """
    INSERT INTO items VALUES (NULL, ?, ?) ;
    """

    cursor.execute(query, (name, price))

    connection.commit()
    connection.close()
