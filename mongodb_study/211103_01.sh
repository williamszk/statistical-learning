# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11758260#overview

mongosh

show dbs

use shop

show collections

# delete the collection
db.products.drop()

db.products.insertOne(
    {
        "name": "A book",
        "price": 12.99
    }
)

db.products.insertOne(
    {
        "name": "A T-Shirt",
        "price": 20.99
    }
)

db.products.insertOne(
    {
        "name": "A Computer",
        "price": 1299,
        "details": {
            "cpu": "Intel i7"
        }
    }
)

db.products.find()

# to delete all documents in collection
db.products.deleteMany({})


db.products.insertOne(
    {
        "name": "A book",
        "price": 12.99,
        "details": null
    }
)

db.products.insertOne(
    {
        "name": "A T-Shirt",
        "price": 20.99,
        "details": null
    }
)

db.products.insertOne(
    {
        "name": "A Computer",
        "price": 1299,
        "details": {
            "cpu": "Intel i7"
        }
    }
)


db.products.find()

# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11758262#overview

# data types
# text or string
# boolean, true or false
# number:
# int32 = Integer
# int64 = NumberLong
# Float = NumberDecimal
# Double
# ObjectId
# ISODate
# Timestamp
# Embedded documents
# Array
# 

# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11758264#overview

# drop the shop database

mongosh

show dbs

use shop

db.dropDatabase()

use companyData

db.companies.insertOne(
    {
        "name": "Fresh Apples Inc",
        "isStartup": true,
        "employees": 33,
        "funding": 12345678901234567890,
        "details": {
            "ceo": "Mark Super"
        },
        "tags": [
            {
                "title": "super"
            },
            {
                "title": "perfect"
            }
        ],
        "foundingDate": new Date(),
        "insertedAt": new Timestamp()
    }
)

db.companies.find()


db.numbers.insertOne({"a":1})

db.stats()

db.companies.drop()

db.stats()

db.numbers.deleteMany({})

db.stats()

db.numbers.insertOne({"a": NumberInt(1)})

db.numbers.deleteMany({})

db.stats()

db.numbers.insertOne({"a":1.0})

db.stats()

typeof db.numbers.findOne().a


# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11758266#overview

# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11758270#overview

use hospital

# reference approach

db.patients.insertOne({"name":"Max", "age": 29, "diseaseSummary":"summary-max-1"})

db.patients.findOne()

db.diseaseSummaries.insertOne({"_id":"summary-max-1", "diseases":["cold","broken leg"]})

db.diseaseSummaries.findOne()

db.patients.findOne()
db.patients.findOne().diseaseSummary

# mongosh is based on JavaScript
# dsid = disease id
var dsid = db.patients.findOne().diseaseSummary

typeof dsid

db.diseaseSummaries.findOne()

db.diseaseSummaries.findOne({"_id":dsid})

# experiment with embeded model

# delete the patients collection
db.patients.drop()

show collections

db.patients.insertOne(
    {
        "name":"Max", 
        "age": 29, 
        "diseaseSummary":{
            "diseases":["cold","broken leg"]
        }
    }
)

# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11758272#overview
# one to one, using references

use carData

db.persons.insertOne({"name":"Max", "car":{"model": "BMW", "price": 40000}})

db.persons.findOne()

db.persons.deleteMany({})

db.persons.insertOne({"name":"Max", "age":29, "salary": 3000})

db.cars.insertOne({"model":"BMW", "price":40000, "owner": ObjectId("61830695613aab9d1e44fbaa")})

db.cars.findOne()




















