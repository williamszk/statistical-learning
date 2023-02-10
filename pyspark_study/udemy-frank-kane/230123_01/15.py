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

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf=conf)
spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

lines = sc.textFile("./datasets/1800.csv")
# 'ITE00100554,18000101,TMAX,-75,,,E,'


schema = StructType(
    [
        StructField("stationID", StringType(), True),
        StructField("date", IntegerType(), True),
        StructField("measure_type", StringType(), True),
        StructField("temperature", FloatType(), True),
    ]
)

df00 = spark.read.schema(schema).csv("datasets/1800.csv")
df00.show(10)
df00.printSchema()

minTemps = df00.filter(df00.measure_type == "TMIN")
minTemps.show(5)

stationTemps = minTemps.select("stationID", "temperature")
stationTemps.show(5)

minTempsByStation = stationTemps.groupBy("stationID").min("temperature")
minTempsByStation.show()

minTempsByStationF = \
    minTempsByStation.withColumn(
        "temperature", 
        func.round(
            func.col("min(temperature)")*0.1*(9.0/5.0)+32.0, 
            2
            ))\
        .select("stationID", "temperature")\
        .sort("temperature")

minTempsByStationF.show(10)

for row in minTempsByStationF.collect():
    print(f"{row.stationID}\t{row.temperature:.2f}F")


