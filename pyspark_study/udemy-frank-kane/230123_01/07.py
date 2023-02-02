
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

lines = sc.textFile("./datasets/1800.csv")
lines.take(10)
for line in lines.take(10):
    print(line.split(","))

# 0 - station id
# 1 -
# 2 - entry type
# 3 - temperature
def parseLine(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return (stationID, entryType, temperature)

parsedLines = lines.map(parseLine)
parsedLines.take(3)
minTemps = parsedLines.filter(lambda x: "TMIN" in x[1])
minTemps.take(3)
stationTemps = minTemps.map(lambda x: (x[0], x[2]))
stationTemps.take(3)
minTemps = stationTemps.reduceByKey(lambda x, y: min(x,y))
results = minTemps.collect()

for result in results:
    print(result[0] + "\t{:.2f}F".format(result[1]))

# ======================================================================
# count the frequency of station id

lines = sc.textFile("./datasets/1800.csv")

def parseLine02(line):
    fields = line.split(',')
    station_id = fields[0]
    return (station_id, 1)

parsedLines = lines.map(parseLine02)
parsedLines.take(3)

sum_per_station_id = parsedLines.reduceByKey(lambda x,y: x+y)
sum_per_station_id.take(3)

# ======================================================================
# count the frequency of station id
# Calculate the maximum temperature for each weather station

lines = sc.textFile("./datasets/1800.csv")

def parseLine03(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return (stationID, entryType, temperature)

parsedLines = lines.map(parseLine03)
maxTemp = parsedLines.filter(lambda x: "TMAX" in x[1])
stationTemps = maxTemp.map(lambda x: (x[0], x[2]))
maxTemp = stationTemps.reduceByKey(lambda x, y: max(x,y))
results = maxTemp.collect()

for result in results:
    print(result[0] + "\t{:.2f}F".format(result[1]))



