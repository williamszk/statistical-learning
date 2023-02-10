# https://www.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/22166648?start=15#overview

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import pyspark.sql.functions as func
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    FloatType,
)

conf = SparkConf().setMaster("local").setAppName("CustomerTotalExpenditure")
sc = SparkContext(conf=conf)
spark = SparkSession.builder.appName("SparkSQL").getOrCreate()


# 0 - customerId
# 1 - itemId
# 2 - amountSpent

schema = StructType(
    [
        StructField("customerId", StringType(), True),
        StructField("itemId", StringType(), True),
        StructField("amountSpent", FloatType(), True),
    ]
)

df00 = spark.read.schema(schema).csv("./datasets/customer-orders.csv")
df00.show(10)
df00.printSchema()

df01 = df00.select("customerId", "amountSpent").groupBy("customerId").sum("amountSpent")

df02 = (
    df01.withColumn("amountSpent", func.round(func.col("sum(amountSpent)"), 2))
    .select("customerId", "amountSpent")
    .sort("amountSpent")
)

df02.show()

# =============================================================================
# Solution from Frank Kane

df01 = df00.groupBy("customerId").agg(
    func.round(func.sum("amountSpent"), 2).alias("amountSpent")
).sort("amountSpent")

df01.show(df01.count())