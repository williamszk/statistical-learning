#%%
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("casting").getOrCreate()

#%%
# https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.functions.to_date.html
df_example = spark.createDataFrame([("1997-02-28 10:30:00",)], ["timestamp"])
df_example.show()
#%%
# how to check type of column in pyspark?

# how to check statistics of a spark data frame
df_example.describe().show()

df_example.printSchema()
#%%
from pyspark.sql.functions import to_date

df_example.select(to_date(df_example["timestamp"])).show()
df_example.select(to_date(df_example["timestamp"]).alias("timestamp")).show()
df_example.select(to_date(df_example["timestamp"]).alias("timestamp")).printSchema()
#%% 
df_example = spark.createDataFrame([("1997-02-28 10:30:00",)], ["timestamp"])

df_example.select(to_date(df_example["timestamp"], "yyyy-MM-dd HH:mm:ss").alias("timestamp")).show()
df_example.select(to_date(df_example["timestamp"], "yyyy-MM-dd HH:mm:ss").alias("timestamp")).printSchema()