#%%
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("basics").getOrCreate()

# %%
df = spark.read.json("../data/people.json")
# %%
df.show()
# %%
df.printSchema()
# %%
df.columns
# %%
df.describe().show()
# %%
from pyspark.sql.types import StructField, StringType, IntegerType, StructType
# %%
data_schema = [
    StructField("age", IntegerType(), True),
    StructField("name", StringType(), True)]
# %%
final_struct = StructType(fields=data_schema)
# %%
df = spark.read.json("../data/people.json", schema=final_struct)
# %%
df.show()
# %%
df.printSchema()
# %%
df["age"]
# %%
type(df["age"])
# spark column object
# %%
df.select("age")
# %%
df.select("age").show()
# %%
type(df.head(2)[0])
# spark have a row type
# %%
df.select(["age","name"]).show()
# %%
df.withColumn("double_age", df["age"]*2).show()
# %%
df.withColumnRenamed("age","my_new_age").show()
# %%
df.createOrReplaceTempView("people")
# %%
results = spark.sql("SELECT * FROM people")
# %%
results.show()
# %%
results = spark.sql("SELECT * FROM people WHERE age > 20")
# %%
results.show()
# %%
