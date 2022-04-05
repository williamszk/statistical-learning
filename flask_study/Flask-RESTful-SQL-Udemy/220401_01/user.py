import sqlite3
from unittest import result

from debugpy import connect

class User:
    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

    @classmethod # class methods are used in situations where we don't need information specific of the instance, but we use the class
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """
        --sql
        SELECT * FROM users WHERE username=? 
        ;
        """

        result = cursor.execute(query, (username,)) # the argument for the ? needs to be a tuple and for a single tuple we need to use (item,)

        row = result.fetchone() # take the first row of the results, I imagine that results is an generator
        
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        
        connection.close()

        return user
    
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = """
        --sql
        SELECT * FROM users WHERE id=? 
        ;
        """

        result = cursor.execute(query, (_id,))

        row = result.fetchone()
        
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        
        connection.close()

        return user

