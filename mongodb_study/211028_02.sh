# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/practice/1060372/introduction#overview

mongosh

show dbs

use medicalRecordsChallenge

db.patients.insertMany([
    {
        "firstName": "Max",
        "lastName": "Schwarzmueller",
        "age": 29,
        "history": [
            {"disease": "cold", "treatment": "rest"}
        ]
    },
    {
        "firstName": "Bob",
        "lastName": "Bobson",
        "age": 40,
        "history": [
            {"disease": "HIV", "treatment": "pills"}
        ]
    },
    {
        "firstName": "Alice",
        "lastName": "Alicedaughter",
        "age": 21,
        "history": [
            {"disease": "headache", "treatment": "rest"}
        ]
    }
])


db.patients.find()

db.patients.updateOne(
    {"firstName":"Alice", "lastName": "Alicedaughter"},
    {$set:
        {
            "age": 25, 
            "history":[
                {"disease": "headache", "treatment": "rest"},
                {"disease": "cold", "treatment": "pills"}
            ]
        }
    }
)

# find all patients that are older than 30 and return only their names
db.patients.find({"age": {"$gt": 21}}, {"firstName": 1, "lastName": 1, "_id": 0})

# delete all patients with cold
db.patients.deleteMany(
    {"history.disease": "cold"}
)

db.patients.find({"history.disease": "cold"})


