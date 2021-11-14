mongosh

show dbs

use support

show collections


# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11758276#overview

use support


db.questionThreads.insertOne(
    {
        "creator": "Max",
        "question": "How does that all work?",
        "answers": ["q1a1","q1a2"]
    }
)


db.questionThreads.insertOne(
    {
        "creator": "Alice",
        "question": "How does that all work again?",
        "answers": [
            "q2a1",
            "q2a2"
        ]
    }
)


db.questionThreads.findOne()


db.questionThreads.find()


db.answers.insertMany([
    {"_id":"q1a1", "text": "It works like that."},
    {"_id": "q1a2", "text": "Thanks!"}
])

# start again
db.questionThreads.deleteMany({})

db.questionThreads.find()

show collections
# One to many using embeded documents
# embed the answers into the question threads
db.questionThreads.insertOne(
    {
        "creator": "Max",
        "question": "How does that work?",
        "answer": [
            {
                "text": "It works like that."
            },
            {
                "text": "Thanks!"
            }
        ]
    }
)

db.questionThreads.find()

# One to Many using references
# Cities and citizens
# a citizen belongs to one city

# MongoDB have a limit of 60MB of size per document
# so for New York it wouldn't make sense to store information about the citizen
# in the collections about cities
# it is better to make a collections for citizens and there we reference to the city
# where they belong
# this rule of making the reference at the node that is not a hub is better

# there are two advantages in making the reference instead of the embeded schema
# (maybe this is also valid for relational databases)
# 1. we don't incur in the risk of creating excessively large documents
# 2. when we fetch data for citizens we don't need to fetch all the data 
# for New York City, which is unnecessary.
show dbs

use cityData

db.cities.insertOne(
    {
        "name": "New York City",
        "coordinates": {"lat": 21, "lng": 55}
    }
)

db.cities.findOne()


db.citizens.insertMany([
    {"name": "Max Scharzmueller", "cityId": ObjectId("618d463b104224289b32fe36")},
    {"name": "Manuel Lorenz", "cityId": ObjectId("618d463b104224289b32fe36")}
])

db.citizens.find()

# Many to many embeded
# example: customers and products that they bought
# usually many to many relationships are modeled with references

# another consideration to make when deciding if we go with a model based
# on reference or embeded is the frequency of reads
# for example: we need to retrieve the information from customers
# many times throughout the day, if we need to make joins many times
# this is time/resource consuming. 
# But if the information needed is embeded with the document this can be
# more advantageous because we save on time/resources.

show dbsuse

use shop






