from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

from pyspark.sql import SparkSession, Row
spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

# 0 - index
# 1 - name
# 2 - age
# 3 - number of friends

def mapper(line):
    fields = line.split(",")
    return Row(
        ID=int(fields[0]), 
        name=str(fields[1].encode("utf-8")),
        age=int(fields[2]),
        numFriends=int(fields[3])
        )

lines = spark.sparkContext.textFile("datasets/fakefriends.csv")
type(lines)
lines.take(2)

people = lines.map(mapper)
people.take(2)
type(people)

# Infer schema, and register the DataFrame as a table.
schemaPeople = spark.createDataFrame(people).cache()
# .cache() keeps the data frame in memory, it is good if we want to do
# lots of queries on the DataFrame later
type(schemaPeople)
schemaPeople.show()
schemaPeople.createOrReplaceTempView("people")

# SQL can be run over DataFrames that have been registered as a table.
teenagers = spark.sql("SELECT * FROM people WHERE age>=13 AND age<=19")
teenagers.show()

for teen in teenagers.collect():
    print(teen)

schemaPeople.groupBy("age").count().orderBy("age").show()

spark.stop()


