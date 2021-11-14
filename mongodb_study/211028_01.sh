# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739222#overview
mongosh

use flights

# here we are creating a new Collection names
# passengers
db.passengers.insertMany(
    [
    {
        "name": "Max Schwarzmueller",
        "age": 29
    },
    {
        "name": "Manu Lorenz",
        "age": 30
    },
    {
        "name": "Chris Hayton",
        "age": 35
    },
    {
        "name": "Sandeep Kumar",
        "age": 28
    },
    {
        "name": "Maria Jones",
        "age": 30
    },
    {
        "name": "Alexandra Maier",
        "age": 27
    },
    {
        "name": "Dr. Phil Evans",
        "age": 47
    },
    {
        "name": "Sandra Brugge",
        "age": 33
    },
    {
        "name": "Elisabeth Mayr",
        "age": 29
    },
    {
        "name": "Frank Cube",
        "age": 41
    },
    {
        "name": "Karandeep Alun",
        "age": 48
    },
    {
        "name": "Michaela Drayer",
        "age": 39
    },
    {
        "name": "Bernd Hoftstadt",
        "age": 22
    },
    {
        "name": "Scott Tolib",
        "age": 44
    },
    {
        "name": "Freddy Melver",
        "age": 41
    },
    {
        "name": "Alexis Bohed",
        "age": 35
    },
    {
        "name": "Melanie Palace",
        "age": 27
    },
    {
        "name": "Armin Glutch",
        "age": 35
    },
    {
        "name": "Klaus Arber",
        "age": 53
    },
    {
        "name": "Albert Twostone",
        "age": 68
    },
    {
        "name": "Gordon Black",
        "age": 38
    }
    ]    
)


db.passengers.find()
# the find() command returns actually a cursor, like a generator in Python
# and then we can use it to just fetch the next item in the collection
# and not bring the entire collection


db.passengers.find().toArray()
# .toArray() will exhaust the cursor, and fetch all the data that find() brought

db.passengers.find().forEach( "inside here is dependent on the driver and programming language"  )

# inside the command of forEach we can pass any function
db.passengers.find().forEach(
    (passengerData) => {printjson(passengerData)}
    )

db.passengers.find().forEach(
    (passengerData) => {printjson(passengerData.name)}
    )

db.passengers.find().forEach(
    (passengerData) => {printjson(passengerData.age)}
    )

db.passengers.find().forEach(
    (passengerData) => {printjson(passengerData["name"])}
    )

db.passengers.find().forEach(
    (passengerData) => {printjson(passengerData["city"])}
    )

# I don't know if javascript syntax works by default in mongosh
# or JavaScript syntax would work inside Python

# in the forEach command each document is fetch individually
# instead of fetching all the data at once
# this saves bandwidth and memory



# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739228#overview
# Projection
# we just collect some keys, instead of the whole document.
# this saves bandwidth, and network resources
# the projection is a filter that is applied inside the mongodb server
# so it saves network resources while transfering the output

db.passengers.find()

db.passengers.find({}, {"name":1})

db.passengers.find({}, {"age":1})

db.passengers.find().forEach(
    (document) => {
        printjson(document.name)
    }
)
# here I don't think that we are fetching just name
# but we are asking for the whole document, and then
# just showing only name


db.passengers.find({}, {"name": 1, "_id":0})

db.passengers.find({}, {"name":1}).forEach(
    (document) => {
        printjson(document)
    }
)


db.passengers.find({}, {"name": 1, "_id": 0}).forEach(
    (document) => {
        printjson(document)
    }
)
# here I think that we are fetching from the server only
# "name", and excluding "_id".
# But the return is an array
# this is different from just find(), because when we use
# just find(), the command returns a cursor, which reads
# and fetch each line at a time, but does not read and
# fetch all the data at once.


# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739232#overview
# Embedded documents
# Nested documents
# low levels of nestings
# 60 MB max size of documents
# Arrays
# 

# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739234#overview

db.flightData.find()

db.flightData.updateMany({}, 
    {$set: {
        "status":{
            "description": "on-time",
            "lastUpdate": "1 hour ago",
            "details": {
                "responsible": "Max Schwarzmueller"
                }
            }
        }
    }
)


# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739236#overview

db.passengers.find()

db.passengers.updateMany(
    {"name": "Albert Twostone"}, 
    {$set: 
        {"hobbies": ["sports", "cooking"]}
    }
)


# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739240#overview

db.passengers.find(
    {"name": "Albert Twostone"}
)

db.passengers.findOne(
    {"name": "Albert Twostone"}
).hobbies

db.passengers.find(
    {"name": "Albert Twostone"},
    {"hobbies": 1, "_id": 0}
)


db.flightData.find()
# how to query documents where conditions are nested
# in other documents
db.flightData.find({"status.description": "on-time"})

db.flightData.find({"status.details.responsible":"Max Schwarzmueller"})



















