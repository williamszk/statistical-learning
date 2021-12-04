
#%%
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("challenge").getOrCreate()
# %%
df_00 = spark.read.csv("../data/walmart_stock.csv",header=True, inferSchema=True)

#%%
# What are the column names?
df_00.printSchema()

# print the columns of the data frame
df_00.columns
# %%
# print the first 5 columns
df_00.head()
type(df_00.head())

#%%
# spark how to select the first rows of dataframe
list_rows = df_00.head(5)
type(list_rows)
# list
type(list_rows[0])
# pyspark.sql.types.Row
#%%
# pyspark transform Row into dictionary
list_dict = [row.asDict() for row in list_rows]
list_dict[0]
# list_dict[0]
# {'Date': '2012-01-03',
#  'Open': 59.970001,
#  'High': 61.060001,
#  'Low': 59.869999,
#  'Close': 60.330002,
#  'Volume': 12668800,
#  'Adj Close': 52.619234999999996}
#%%
df_00.describe().show()

# +-------+----------+------------------+-----------------+-----------------+-----------------+-----------------+-----------------+
# |summary|      Date|              Open|             High|              Low|            Close|           Volume|        Adj Close|
# +-------+----------+------------------+-----------------+-----------------+-----------------+-----------------+-----------------+
# |  count|      1258|              1258|             1258|             1258|             1258|             1258|             1258|
# |   mean|      null| 72.35785375357709|72.83938807631165| 71.9186009594594|72.38844998012726|8222093.481717011|67.23883848728146|
# | stddev|      null|  6.76809024470826|6.768186808159218|6.744075756255496|6.756859163732991|  4519780.8431556|6.722609449996857|
# |    min|2012-01-03|56.389998999999996|        57.060001|        56.299999|        56.419998|          2094900|        50.363689|
# |    max|2016-12-30|         90.800003|        90.970001|            89.25|        90.470001|         80898100|84.91421600000001|
# +-------+----------+------------------+-----------------+-----------------+-----------------+-----------------+-----------------+

# the data frame have 1258 rows

#%%
# show 
table_describe = df_00.describe()
table_describe.show()



# this doesn't work bechase the "Open" and all other variables are strings
# table_describe.select(format_number("Open",2)).show()
table_describe.printSchema()
# we need first to convert them into float before proceeding
# casting with select
from pyspark.sql.functions import col
table_describe2 = table_describe
table_describe2.select(col("Open").cast("float"))

# the .select() method will create a new dataframe, we can't assign it to a
# column in another dataframe 

# casting with .cast method for pyspark column
table_describe2["Open"].cast("float")


# we use withColumn to change a column of pyspark
# casting with withColumn
table_describe2.withColumn("Open",table_describe2["Open"].cast("float")).show()
table_describe2.withColumn("Adj Close", table_describe2["Adj Close"].cast("float")).show()
# +-------+----------+------------------+-----------------+-----------------+-----------------+-----------------+---------+
# |summary|      Date|              Open|             High|              Low|            Close|           Volume|Adj Close|
# +-------+----------+------------------+-----------------+-----------------+-----------------+-----------------+---------+
# |  count|      1258|              1258|             1258|             1258|             1258|             1258|   1258.0|
# |   mean|      null| 72.35785375357709|72.83938807631165| 71.9186009594594|72.38844998012726|8222093.481717011| 67.23884|
# | stddev|      null|  6.76809024470826|6.768186808159218|6.744075756255496|6.756859163732991|  4519780.8431556|6.7226095|
# |    min|2012-01-03|56.389998999999996|        57.060001|        56.299999|        56.419998|          2094900| 50.36369|
# |    max|2016-12-30|         90.800003|        90.970001|            89.25|        90.470001|         80898100|84.914215|
# +-------+----------+------------------+-----------------+-----------------+-----------------+-----------------+---------+

# a test to create a new column in spark dataframe
table_describe2.withColumn("my_new_column", table_describe2["Close"].cast("float")).show()
# +-------+----------+------------------+-----------------+-----------------+-----------------+-----------------+-----------------+-------------+
# |summary|      Date|              Open|             High|              Low|            Close|           Volume|        Adj Close|my_new_column|
# +-------+----------+------------------+-----------------+-----------------+-----------------+-----------------+-----------------+-------------+
# |  count|      1258|              1258|             1258|             1258|             1258|             1258|             1258|       1258.0|
# |   mean|      null| 72.35785375357709|72.83938807631165| 71.9186009594594|72.38844998012726|8222093.481717011|67.23883848728146|     72.38845|
# | stddev|      null|  6.76809024470826|6.768186808159218|6.744075756255496|6.756859163732991|  4519780.8431556|6.722609449996857|    6.7568593|
# |    min|2012-01-03|56.389998999999996|        57.060001|        56.299999|        56.419998|          2094900|        50.363689|        56.42|
# |    max|2016-12-30|         90.800003|        90.970001|            89.25|        90.470001|         80898100|84.91421600000001|        90.47|
# +-------+----------+------------------+-----------------+-----------------+-----------------+-----------------+-----------------+-------------+

#%%
def cast_columns_pyspark(dataframe, list_columns, type):
    for variable in list_columns:
        dataframe = dataframe.withColumn(variable, dataframe[variable].cast(type))
    return dataframe
#%%
dataframe = table_describe2
list_columns = ["Open", "High", "Low", "Close", "Volume", "Adj Close"]
type = "float"
table_describe3 = cast_columns_pyspark(dataframe, list_columns, type)

#%%
table_describe3.show()
# finish casting all variables of interest into float
table_describe3.printSchema()
# root
#  |-- summary: string (nullable = true)
#  |-- Date: string (nullable = true)
#  |-- Open: float (nullable = true)
#  |-- High: float (nullable = true)
#  |-- Low: float (nullable = true)
#  |-- Close: float (nullable = true)
#  |-- Volume: float (nullable = true)
#  |-- Adj Close: float (nullable = true)

#%%
# next step print the dataframe, but the float variables needs to have
# 2 decimal positions
from pyspark.sql.functions import format_number

def format_decimal_pyspark(dataframe, list_columns, n_decimal):
    for variable in list_columns:
        dataframe = dataframe.withColumn(variable, format_number(dataframe[variable], n_decimal))

    return dataframe
#%%
dataframe = table_describe3
list_columns = ["Open", "High", "Low", "Close", "Volume", "Adj Close"]
n_decimal = 2

table_describe4 = format_decimal_pyspark(dataframe, list_columns, n_decimal)
#%%
table_describe4.show()
# +-------+----------+--------+--------+--------+--------+-------------+---------+
# |summary|      Date|    Open|    High|     Low|   Close|       Volume|Adj Close|
# +-------+----------+--------+--------+--------+--------+-------------+---------+
# |  count|      1258|1,258.00|1,258.00|1,258.00|1,258.00|     1,258.00| 1,258.00|
# |   mean|      null|   72.36|   72.84|   71.92|   72.39| 8,222,093.50|    67.24|
# | stddev|      null|    6.77|    6.77|    6.74|    6.76| 4,519,781.00|     6.72|
# |    min|2012-01-03|   56.39|   57.06|   56.30|   56.42| 2,094,900.00|    50.36|
# |    max|2016-12-30|   90.80|   90.97|   89.25|   90.47|80,898,096.00|    84.91|
# +-------+----------+--------+--------+--------+--------+-------------+---------+

#%%
table_describe4.printSchema()

# root
#  |-- summary: string (nullable = true)
#  |-- Date: string (nullable = true)
#  |-- Open: string (nullable = true)
#  |-- High: string (nullable = true)
#  |-- Low: string (nullable = true)
#  |-- Close: string (nullable = true)
#  |-- Volume: string (nullable = true)
#  |-- Adj Close: string (nullable = true)

# All the variables that were previously float are now string
# that means that the format_number cast numerics into strings again
# for printing purposes this is ok.
# And we should use format_number for printing purposes only... (?)
#%%
df_00.columns
df_00.withColumn("HV Ratio", df_00["High"]/df_00["Volume"]).show()

#%%
# #### What day had the Peak High in Price?
df_00.select("High").describe().show()

df_00.filter(df_00["High"] == 90.970001).show()

# +----------+---------+---------+-----+---------+-------+---------+
# |      Date|     Open|     High|  Low|    Close| Volume|Adj Close|
# +----------+---------+---------+-----+---------+-------+---------+
# |2015-01-13|90.800003|90.970001|88.93|89.309998|8215400|83.825448|
# +----------+---------+---------+-----+---------+-------+---------+

#%%
#### What is the mean of the Close column?
from pyspark.sql.functions import avg, max, min
df_00.select(avg("Close")).show()
# +-----------------+
# |       avg(Close)|
# +-----------------+
# |72.38844998012726|
# +-----------------+
#%%
#### What is the max and min of the Volume column?
df_00.select(max("Volume"), min("Volume")).show()
# +-----------+-----------+
# |max(Volume)|min(Volume)|
# +-----------+-----------+
# |   80898100|    2094900|
# +-----------+-----------+
# %%
#### How many days was the Close lower than 60 dollars?
df_00["Close"] < 60
# pyspark column how to convert to list
df_00.filter(df_00["Close"]<60).count()
# pyspark how to know the number of lines in data frame?
# 81
#%%
#### What percentage of the time was the High greater than 80 dollars ?
#### In other words, (Number of Days High>80)/(Total Days in the dataset)
df_00["High"].count()
df_00.select("High").filter(df_00["High"] > 80).count()/df_00.select("High").count()
# 0.09141494435612083
#%%
#### What is the Pearson correlation between High and Volume?
#### [Hint](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrameStatFunctions.corr)
# pyspark correlation stats
from pyspark.ml.stat import Correlation

Correlation.corr(df_00, ["High", "Volume"], "pearson")
# What is the difference between the "pearson" and "spearman" correlation?

#%%
#### What is the max High per year?
df_00.columns
df_00.printSchema()
# how to convert string to datetime
from pyspark.sql.functions import year
df_00.select(year(df_00["Date"])).show()
df_01 = df_00.withColumn("Year", year(df_00["Date"]))
df_01.show()

df_01.select(["Year", "High"]).groupBy("Year").max("High").orderBy("Year").show()

# +----+---------+
# |Year|max(High)|
# +----+---------+
# |2012|77.599998|
# |2013|81.370003|
# |2014|88.089996|
# |2015|90.970001|
# |2016|75.190002|
# +----+---------+

#%%

# What is the average Close for each Calendar Month?
# In other words, across all the years, what is the average Close price for 
# Jan,Feb, Mar, etc... Your result will have a value for each of these months. 

from pyspark.sql.functions import month

df_01 = df_00.withColumn("Month", month(df_00["Date"]))

df_01.cube("Month").count().orderBy("Month").show()

df_01.groupBy("Month").count().orderBy("Month").show()

df_01.show()

df_01.groupBy("Month").mean("Close").orderBy("Month").show()


