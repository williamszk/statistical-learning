# pyspark

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

# reduceByKey(lambda x,y: x+y)
# groupByKey()
# sortByKey()
# keys(), values()

# join, rightOuterJoin, leftOuterJoin, cogroup, subtractByKey

# mapValues()
# flatMapValues()

friends00 = sc.textFile("./datasets/friends_example.csv")
type(friends00)
friends00.take(2)

friends01 = friends00.map(lambda x: x.split(","))
friends01.take(2)

# 0 - index
# 1 - name
# 2 - age
# 3 - number of friends

def parseLine(line):
    fields = line.split(",")
    age = int(fields[2])
    numFriends = int(fields[3])
    return (age, numFriends)

lines = sc.textFile("./datasets/friends_example.csv")
rdd00 = lines.map(parseLine)

rdd00.take(3)
rdd00.mapValues(lambda x: (x,1)).take(3)

rdd00.mapValues(lambda x: (x,1))\
    .reduceByKey(lambda x,y: (x[0]+y[0], x[1]+y[1]))\
    .take(3)

totalsByAge = rdd00\
    .mapValues(lambda x: (x, 1))\
    .reduceByKey(lambda x,y: (x[0]+y[0], x[1]+y[1]))

totalsByAge.collect()

averagesByAge = totalsByAge.mapValues(lambda x: x[0]/x[1])
averagesByAge_collected = averagesByAge.collect()

for result in averagesByAge_collected:
    print(result)
