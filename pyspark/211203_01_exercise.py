
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




#%%




