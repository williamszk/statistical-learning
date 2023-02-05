
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

friends00 = sc.textFile("./datasets/fakefriends.csv")
type(friends00)
friends00.take(3)
friends00.count()

# 0 - index
# 1 - name
# 2 - age
# 3 - number of friends

def parseLine(line):
    fields = line.split(",")
    age = int(fields[2])
    numFriends = int(fields[3])
    return (age, numFriends)

friends01 = friends00.map(parseLine)
friends01.take(3)

friends01\
    .mapValues(lambda x: (x, 1))\
    .take(3)

totalsByAge = friends01\
    .mapValues(lambda x: (x, 1))\
    .reduceByKey(lambda x,y: (x[0]+y[0], x[1]+y[1]))

averagesByAge = totalsByAge.mapValues(lambda x: x[0]/x[1])
averagesByAge_collected = averagesByAge.collect()

for result in averagesByAge_collected:
    print(result)

