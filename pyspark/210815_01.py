#https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/learn/lecture/6688216?start=15#overview
# groupby and aggregate functions


#%%
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("aggregate").getOrCreate()

#%%
df = spark.read.csv(
    "../data/sales_info.csv",
    inferSchema=True,
    header=True
    )

df.show()
df.printSchema()
# %%
df.groupBy("Company")
# <pyspark.sql.group.GroupedData at 0x7fae09deadf0>
# %%
df.groupBy("Company").mean()

df.groupBy("Company").mean().show()

df.groupBy("Company").sum().show()

df.groupBy("Company").max().show()

df.groupBy("Company").count().show()
# %%
df.groupBy("Person").mean().show()

# %%

# how to find the total sum of a column?
# +-------+-------+-----+
# |Company| Person|Sales|
# +-------+-------+-----+
# |   GOOG|    Sam|200.0|
# |   GOOG|Charlie|120.0|
# |   GOOG|  Frank|340.0|
# |   MSFT|   Tina|600.0|
# |   MSFT|    Amy|124.0|
# |   MSFT|Vanessa|243.0|
# |     FB|   Carl|870.0|
# |     FB|  Sarah|350.0|
# |   APPL|   John|250.0|
# |   APPL|  Linda|130.0|
# |   APPL|   Mike|750.0|
# |   APPL|  Chris|350.0|
# +-------+-------+-----+

df.show()
df.agg({"Sales":"sum"}).show()

df.agg({"Sales":"max"}).show()

# %%
# we can also find the sum using a groupBy syntax
df.groupBy().sum().show()

#%%
# how can we find the sum of sales for each Company?
# there are some ways:

# 1. 
df.groupBy("Company").sum().show()

# 2.
group_data = df.groupBy("Company")
group_data.agg({"Sales":"sum"}).show()

#%%

from pyspark.sql.functions import countDistinct, avg, stddev


df.select(countDistinct("Sales")).show()

# how many unique companies do we have?
df.select(countDistinct("Company")).show()

# how many unique sales person do we have?
df.select(countDistinct("Person")).show()

# find the total average of Sales in the data frame
df.select(avg("Sales")).show()

# is there another way to take the averate of the entire column?
df.groupBy().mean().show()

# is there another way to take the average
# of groups of companies?

#%%

df.select(avg("Sales").alias("average_sales")).show()
# we can change the name of the column using alias


#%%
# how to format the Double
df.select(stddev("Sales")).show()


#%%

from pyspark.sql.functions import format_number

df_sales_std = df.select(stddev("Sales").alias("std_sales"))
df_sales_std.show()

df_sales_std.select(format_number("std_sales",2)).show()

df_sales_std.select(format_number("std_sales",2).alias("std_sales")).show()

# can we do the operation above in just one line?

#%%
# how to order and sort?

# sort in Sales
df.orderBy("Sales").show()

# how to order data frame in descending order?
df.orderBy(df["Sales"].desc()).show()


