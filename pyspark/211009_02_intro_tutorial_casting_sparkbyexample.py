# https://sparkbyexamples.com/pyspark/pyspark-cast-column-type/
#%%
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("casting").getOrCreate()

# %%
from pyspark.sql.types import (
    IntegerType,
    BooleanType,
    DateType)

#%%
from pyspark.sql.functions import (
    col
)

# %%
df = spark.read.csv("../data/appl_stock.csv", header=True, inferSchema=True)
# %%
df.printSchema()
# see Date, it is string
# we want it to be in date format
df.show()
# %%
df.Open
df["Open"]
# %%
# there are many ways to convert a column into integer
# 
df.withColumn("Open", df["Open"].cast(IntegerType())).show()

df.withColumn("Open", df["Open"].cast("int")).show()

df.withColumn("Open", df["Open"].cast("integer")).show()

#%%
# casting using select

df.select(col("Open").cast("int")).show()
df.select(col("Open")).show()
#%%
df.selectExpr("cast(Open as int)").show()
#%%
# to use SQL queries we first need to
# create a temp view of the data frame
df.createOrReplaceTempView("appl_stock")
#%%
spark.sql("""
SELECT INT(Open) from appl_stock
""").show()

# %%
df_2 =  df.withColumn("Date", df["Date"].cast(DateType()))
type(df["Date"])
df_2.show()
df_2.printSchema()
# %%
df.head(1)
# %%
from datetime import datetime
# %%
# does not work
# df.withColumn("Date", df["Date"].cast(datetime())).show()
# %%

#%%



