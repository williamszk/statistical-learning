import sqlite3
from db import db 


class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    # print(f"{id = }") # id = Column(None, Integer(), table=None, primary_key=True, nullable=False)
    # print(f"{type(id) = }") # type(id) = <class 'sqlalchemy.sql.schema.Column'>
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    def save_to_db(self):
        """upsert to db
        This function will change the record if it exists. Or it will
        insert the record if it doesn't exist.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    # to use sqlalchemy flask we need to include it inside the
    # class so that it contains information about the table 
    @classmethod
    def find_by_name(cls, name: str):
        # SELECT * FROM items WHERE name=? LIMIT 1;
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all_items(cls) -> list["ItemModel"]:
        return cls.query.all()


