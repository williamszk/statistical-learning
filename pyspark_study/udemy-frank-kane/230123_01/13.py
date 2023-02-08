from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

from pyspark.sql import SparkSession
import  pyspark.sql.functions as sfunc 

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

people = spark.read.option("header", "true").option("interSchema","true")\
    .csv("datasets/fakefriends-header.csv")

people.show()

people.select(people.age,people.friends)\
    .withColumn("friends", people.friends.cast("int"))\
    .groupBy("age").avg("friends").sort("age").show(100)

# take average of friends by age, then round it and give a better name
people.select(people.age,people.friends)\
    .withColumn("friends", people.friends.cast("int"))\
    .groupBy("age").agg(sfunc.round(sfunc.avg("friends"),2).alias("friends_avg"))\
    .sort("age").show(100)
    



