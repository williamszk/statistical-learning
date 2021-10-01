#%%
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("miss").getOrCreate()
# %%
df = spark.read.csv("../data/ContainsNull.csv", header=True, inferSchema=True)
# %%
df.show()
# %%
# To drop observations with missing data
df.na.drop().show()
# %%
# Threshold for dropping observations
# the line must have at least 2 non missing values
# to be not droped
df.na.drop(thresh=2).show()
# %%
# Parameter how="all", drop if all columns
# are missing
df.na.drop(how="all").show()
# %%
# Drop if a subset of columns are missing
df.na.drop(subset=["Sales"]).show()
# %%
df.printSchema()
# %%
df.na.fill("FILL VALUE").show()
# %%
df.na.fill(0).show()
# %%
# Select the columns that we want to fill missing value
df.na.fill("No Name", subset=["Name"]).show()
# %%
from pyspark.sql.functions import avg
# %%
# Fill the missing values of Sales with the mean
result = df.select(avg("Sales").alias("average_sales")).select("average_sales").collect()
average_sales = result[0].asDict()["average_sales"]
# %%
df.na.fill(average_sales, subset=["Sales"]).show()
# %%
from pyspark.sql.functions import mean
mean_val = df.select(mean(df["Sales"])).collect()
mean_sales = mean_val[0][0]
# %%
df.na.fill(mean_sales, ["Sales"]).show()
# %%
