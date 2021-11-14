mongosh

# insertOne
# insertMany
# find(filter, options)
# findOne()
# updateOne()
# updateMany()
# replaceOne()
# deleteOne()
# deleteMany()

show dbs

# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739206#overview

use flights

# how to show collections inside data base?
show collections

db.flightData.find()

# inside the function we pass a filter
# the filter is an object
db.flightData.deleteOne({"departureAirport":"TXL"})
# deleteOne() deletes the first document that matches the filter

# we can also pass an _id in the filter for deleteOne
db.flightData.deleteOne({"_id":"txl-lhr-1"})

db.flightData.find()

# we can't pass deleteMany without a filter
db.flightData.deleteMany()

# in the updateOne function the first argument
# determines the filter, which documents to update
# the second argument is how we want to change the 
# document
db.flightData.updateOne({"distance":12000}, {"marker":"delete"})
# we rececive an error
# MongoInvalidArgumentError: Update document requires atomic operators

# we need to include $set in the function, this is a special
# type of command in mongodb
db.flightData.updateOne({"distance": 12000}, {$set: {"marker": "delete"}})

db.flightData.find()

# update all documents in the collection
db.flightData.updateMany({}, {$set: {"marker": "toDelete"}})

# we can delete all documents from the collection
db.flightData.deleteMany({"marker":"toDelete"})

db.flightData.find()

# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739208#overview

mongosh
use flights

db.flightData.find()

# when we insert data with insertMany we pass an
# array of objects
db.flightData.insertMany([
    {
        "departureAirport": "MUC",
        "arrivalAirport": "SFO",
        "aircraft": "Airbus A380",
        "distance": 12000,
        "intercontinental": true
    },
    {
        "departureAirport": "LHR",
        "arrivalAirport": "TXL",
        "aircraft": "Airbus A320",
        "distance": 950,
        "intercontinental": false
    }
])

# -------------------------------------------------------------------------
# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739212#overview
# use find with a filter
db.flightData.find({"intercontinental":true})

# find all documents where flights are greater than 10000 km
db.flightData.find({"distance": 12000})

# here use another special operator $gt to find 
# flights that are greater than 10.000 km
db.flightData.find({"distance": {$gt: 10000}})
db.flightData.find({"distance": {$gt: 900}})

# what happens when we use findOne?
# only the first match is brought
db.flightData.findOne({"distance": {$gt: 900}})


# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739218#overview

db.flightData.find()

db.flightData.updateOne(
    {"_id": ObjectId("617ab212db35132e02ee7840")},
    {$set: {"delayed": true}}
    )

# what is the difference between "updateMany" and "update"?
# in the syntax of "update", we are actually overwriting the
# the whole document, instead of justing adding a new key
# so the recomendation is to not use "update"
# if we want to replace a document we should use "replaceOne"
# or "replaceMany"

db.flightData.replaceOne(
    {"_id":ObjectId("617ab212db35132e02ee7840")},
    {
        "departureAirport": "MUC",
        "arrivalAirport": "SFO",
        "aircraft": "Airbus A380",
        "distance": 12000,
        "intercontinental": true
    }
    )

db.flightData.find()



















