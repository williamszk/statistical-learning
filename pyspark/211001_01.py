#%%
import findspark
from numpy.lib.twodim_base import triu_indices_from
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("aggs").getOrCreate()
# %%
df = spark.read.csv("../data/sales_info.csv", inferSchema=True, header=True)
# %%
df.show()
# %%
df.printSchema()
# %%
df.groupBy("Company")
# %%
df.groupBy("Company").mean()
# %%
df.groupBy("Company").mean().show()
# %%
df.groupBy("Company").sum().show()
# %%
df.groupBy("Company").count().show()
# %%
df.agg({"Sales":"sum"}).show()
# %%
df.agg({"Sales":"max"}).show()
# %%
group_data = df.groupBy("Company")
group_data.agg({"Sales":"mean"}).show()
# %%
from pyspark.sql.functions import countDistinct, avg, stddev
# %%
df.select(countDistinct("Sales")).show()
# %%
df.select(avg("Sales")).show()
# %%
df.select(stddev("Sales")).show()
# %%
df.select(avg("Sales").alias("Average Sales")).show()
# %%
from pyspark.sql.functions import format_number
# %%
sales_std = df.select(stddev("Sales").alias("std"))
sales_std.select(format_number("std", 2).alias("Standard Deviation")).show()
# %%
df.show()
# %%
# Sort (descending)
df.orderBy("Sales").show()
# %%
# How to make ascending sort
df.orderBy(df["Sales"].desc()).show()
# %%
