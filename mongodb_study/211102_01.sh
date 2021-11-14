# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11751226?start=0#overview

# how to delete a whole database?
use databaseName
db.dropDatabase()

# how to delete a whole collection?
db.myCollection.drop()

# ------------------

mongosh
show dbs

use shop
db.dropDatabase()

show collections

db.products.insertOne(
    {
        "name": "A book",
        "price": 12.99
    }
)

db.products.find()

db.products.insertOne(
    {
        "title": "T-shirt",
        "seller": {
            "name": "Max",
            "age": 29
        }
    }
)


























