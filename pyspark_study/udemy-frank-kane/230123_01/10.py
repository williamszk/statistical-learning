# Spark SQL
# DataFrame API


from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

from pyspark.sql import SparkSession, Row
# the spark object already exists
spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

df00 = spark.read.json("datasets/some_data.json")

df00.collect()
type(df00)

df00.show()

df00.createOrReplaceTempView("myStructuredStuff")

df01 = spark.sql("SELECT foo FROM bar ORDER BY foobar")

df01.select("someFieldName")

df01.filter(df01["someFieldName"]>200)

df01.groupBy(df01["someFieldName"]).mean()

def mapperFunction():
    pass

df00.rdd().map(mapperFunction)

df01.show()


# "DataSets"
# Scala

# User defined function inside sql

from pyspark.sql.types import IntegerType

def square(x):
    return x*x

spark.udf.register("square", square, IntegerType())

df00 = spark.sql("select square('someNumericField') from tableName")




