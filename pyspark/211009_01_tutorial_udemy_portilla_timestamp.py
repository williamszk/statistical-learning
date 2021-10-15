#%%
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("dates").getOrCreate()

# %%
df = spark.read.csv("../data/appl_stock.csv", header=True, inferSchema=True)
#%%
df.show()
# %%
df.head(1)
# %%
df.select(["Date","Open"]).show()
# %%
from pyspark.sql.functions import (
    dayofmonth, 
    hour, 
    dayofyear, 
    month, 
    year,
    weekofyear,
    format_number,
    date_format
    )
# %%
# transform Date from string to datetime.datetime format

# 1. change after it was read

# 2. change the schema of the import

#%%
df = spark.read.csv("../data/appl_stock.csv", header=True, inferSchema=True)

df.count()
len(df.columns)

# %%
df.select()
# %%
from pyspark.sql.types import DateType
#%%
df.printSchema()
#%%
df.select(["Date"]).show()
df.select(dayofmonth(df["Date"])).show()
df.select(dayofmonth(df["Date"])).printSchema()
df.select(dayofmonth(df["Date"]).alias("dayofmonth")).show()

df.select(hour(df["Date"])).show()
df.select(dayofyear(df["Date"])).show()
df.select(month(df["Date"])).show()
df.select(year(df["Date"])).show()
df.select(weekofyear(df["Date"])).show()
# df.select(format_number(df["Date"], "d")).show()
df.select(date_format(df["Date"], "yyyy-MM-dd")).show()
df.select(date_format(df["Date"], "dd/MM/yyyy")).show()
df.select(date_format(df["Date"], "dd/MM/yyyy")).printSchema()
#%%
# what is the average closing price in the year?
df.select(year(df["Date"])).show()
# how to create a new column
df_2 = df.withColumn("Year", year(df["Date"]))

df.show()

df_2.select(["Date", "Year", "Close"]).show()

result = df_2.groupby("Year").mean().select(["Year","avg(Close)"])
result.show()

result_2 = result.withColumnRenamed("avg(Close)","average_close")
result_2.show()
result_3 = result_2.select(["Year",format_number("average_close", 2).alias("average_close")])
result_3.show()
