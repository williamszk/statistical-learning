
# this is actually done for windows cmd
# but with some changes it can work with bash

# to show databases
show dbs

# mongodb shell
# called mongosh

# where is installed mongosh?
# C:\Users\william.suzuki\AppData\Local\Programs\mongosh\

# how to see paths that are included in PATH in cmd
echo %PATH%
# C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;
# C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;
# C:\Windows\System32\OpenSSH\;
# C:\Program Files\Intel\WiFi\bin\;
# C:\Program Files\Common Files\Intel\WirelessCommon\;
# C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;
# C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;
# C:\Program Files\PuTTY\;C:\Program Files\Git\cmd;
# C:\Program Files\Amazon\AWSCLIV2\;
# C:\Users\william.suzuki\AppData\Local\Microsoft\WindowsApps;
# ;
# C:\Users\william.suzuki\AppData\Local\Programs\Microsoft VS Code\bin;
# C:\Users\william.suzuki\null\Coursier\data\bin


# to start the mongosh
dir C:\Users\william.suzuki\AppData\Local\Programs\mongosh\
PATH=%PATH%;C:\Users\william.suzuki\AppData\Local\Programs\mongosh\

# to start the mongosh
mongosh

show dbs

# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739124#overview

# connect to a new databse even if the database does not exist
use shop

# how to insert a Document into a Collection
# that does not exist already
db.products.insertOne({
    "name":"A book",
    "age": 12.99
})
# the output should be something like the below
# it means that the insertion was successful
# {
#   acknowledged: true,
#   insertedId: ObjectId("616ef1e3179fe6d2b07733a9")
# }

# the code below gives all Documents in the 
# specified collection
db.products.find()
# the .pretty() is automatically applied in mongosh
db.products.find().pretty()

db.products.insertOne({
    "name":"A T-Shirt",
    "price": 29.99,
    "description": "This is a high quality T-Shirt."
})

db.products.find()

db.products.insertOne({
    "name":"A computer",
    "price":1229.90,
    "description":"A high quality computer.",
    "details":{
        "cpu":"Intel i7 8770",
        "memory":32
    }
})

db.products.find()


# 2021-10-21
# https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739180#overview
show dbs

# create and use a new database called flights
use flights

db.flightData.insertOne(
    {
        "departureAirport": "MUC",
        "arrivalAirport": "SFO",
        "aircraft": "Airbus A380",
        "distance": 12000,
        "intercontinental": true
    }
)

show dbs

db.flightData.find()

# BSON uses less spaces
# BSON supports other types like ObjectId


db.flightData.insertOne({
    "departureAirport": "LHR",
    "arrivalAirport": "TXL",
    "aircraft": "Airbus A320",
    "distance": 950,
    "intercontinental": false    
})


db.flightData.find()

# a test to set the id manually
db.flightData.insertOne({
    "_id":"txl-lhr-1",
    "departureAirport": "LHR",
    "arrivalAirport": "TXL"      
})

db.flightData.find()

# we can set the unique ids manually
# this will be important in the future











