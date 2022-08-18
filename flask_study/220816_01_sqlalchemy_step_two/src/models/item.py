"""In the models directory there should not be any code that is related to
the endpoints. So the implementation inside the models package should not 
know anything about how the endpoints are implemented. This is a job for the code inside the 
resources directory.

Inside the models package we should include code that deals directly to the database
this can be via a database connector or it can be via an ORM like
SQLAlchemy.
The job of the code inside the models package should be to transform and communicate two
mediums of data: (i) the data that lives in the database, and 
(ii) the data that lives inside the programming language (Python or any other).

The purpose of the resource is to call functions/methods from the models package
so that it can serve the endpoints.

Hence:
- Everything that the client knows are the endpoints and resources.
- Everthing that the resources know are the client and the models package.
- Everything that the models package knows is the resources and the database itself.

The models package knows the schema of tables inside the database.
The resource package should not know anything about the schema or the existence of the
database. For the resources package the data that comes out of the models functions
could come from just in memory data, it could come from MongoDB, Redis,
CockroachDB, Redshift, from anywhere. Because the resouces will use the data
in the native language format, that is arrays, dictionaries, objects. 
That implies that the resources package shouldn't contain any code 
related to queries to the database.

One missing piece of this explanation and architecture is the core domaing logic.
The core domain logic should be the source of all change.
The core domain logic should not depend on anything else inside the system.
Everything else will revolve around the core domain logic.
Every change should be implemented to accomodate the core domain logic's needs.

The endpoints and the resources package should change to accomodate the needs and conditions
of the core domain logic.
The database and the models package should change to fit to the needs of the
core domain logic. 


"""


from db import db


class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship("StoreModel")

    def __init__(self, name: str, price: float, store_id: int) -> None:
        self.name = name
        self.price = price
        self.store_id

    def json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(cls, name: str) -> "ItemModel":
        # connection = sqlite3.connect("./db.sqlite")
        # cursor = connection.cursor()

        # query = """ --sql
        # SELECT * FROM items WHERE name=?;
        # """
        # # querydata = next(cursor.execute(query, (name,)), None)
        # row = cursor.execute(query, (name,)).fetchone()
        # connection.close()

        # if row:
        #     item = cls(name, row[2])
        #     # item = cls(*row)
        #     return item

        # return None
        return cls.query.filter_by(name=name).first()

    def save_to_db(self) -> None:
        # connection = sqlite3.connect("./db.sqlite")
        # cursor = connection.cursor()

        # query = """ --sql
        # INSERT INTO items VALUES (NULL, ?, ?) ;
        # """

        # cursor.execute(query, (self.name, self.price))

        # connection.commit()
        # connection.close()
        db.session.add(self)
        db.session.commit()

    # def save_to_db(self):
    #     connection = sqlite3.connect("./db.sqlite")
    #     cursor = connection.cursor()

    #     query = """--sql
    #     UPDATE items SET price=? WHERE name=?;
    #     """
    #     cursor.execute(query, (self.price, self.name))

    #     connection.commit()
    #     connection.close()

    def delete_from_db(self):
        # connection = sqlite3.connect("./db.sqlite")
        # cursor = connection.cursor()

        # query = """ --sql
        # DELETE FROM items WHERE name=?;
        # """

        # cursor.execute(query, (self.name,))

        # connection.commit()
        # connection.close()
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls) -> list["ItemModel"]:
        # connection = sqlite3.connect("./db.sqlite")
        # cursor = connection.cursor()
        # query = """ --sql
        # SELECT * FROM items;
        # """
        # items = []
        # for row in cursor.execute(query):
        #     item = cls(row[1], row[2])
        #     items.append(item)

        # connection.close()

        # return items

        # return [item for item in cls.query.all()]
        return list(cls.query.all())
