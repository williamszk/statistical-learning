
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

from pyspark.sql import SparkSession, Row, Column
spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

people = spark.read.option("header", "true").option("interSchema","true")\
    .csv("datasets/fakefriends-header.csv")

type(people)
people.take(2)

people.printSchema()
people.show()
people.count()

people.select("name").show()

# filter only people with less than 21 years old
people.filter(people.age < 21).show()
type(people.age)
type(people.age < 21)
(people.age < 21)

# group by age
people.groupBy("age").count().sort("age").show(100)

# Make everyone 10 years older
people.select("name","age").show()
spark.stop()
