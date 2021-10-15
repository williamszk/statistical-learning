#%%
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("challenge").getOrCreate()
# %%
type(spark)
df = spark.read.csv("../data/walmart_stock.csv",header=True, inferSchema=True)
df.count()
df.columns
df.show()
df.printSchema()
df.head(5)
df.describe().show()
#%%
df.describe().printSchema()




#%%
# show describe table with 2 decimal places for price
# columns

from pyspark.sql.types import (
    DoubleType
)

from pyspark.sql.functions import (
    format_number
)

list_cast_variables = ["Open", "High", "Low", "Close", "Volume", "Adj Close"]
df_describe = df.describe()

for variable in list_cast_variables:
    df_describe = df_describe.withColumn(variable, df_describe[variable].cast(DoubleType()))

for variable in list_cast_variables:
    df_describe = df_describe.withColumn(variable, format_number(df_describe[variable], 2))


df_describe.printSchema()
df_describe.show()
#%%
# show average prices per year and month

from pyspark.sql.functions import (
    month,
    year
)

df.columns

df_2 = df.withColumn("Year", year(df["Date"]))
df_2 = df_2.withColumn("Month", month(df["Date"]))
df_2.show()

df_2.groupBy("Year").mean()


#%%
def helper_generate_summary_mean(groupby_variable = "Month"):

    df_summary_month = df_2.groupBy(groupby_variable).mean()

    for variable in list_cast_variables:
        df_summary_month = df_summary_month.\
            withColumnRenamed(f"avg({variable})", variable)

    for variable in list_cast_variables:
        df_summary_month = df_summary_month.\
            withColumn(
                variable, 
                format_number(df_summary_month[variable], 2).
                alias(variable))

    df_summary_month = df_summary_month.select([groupby_variable]+list_cast_variables).orderBy(groupby_variable)

    return df_summary_month
#%%
helper_generate_summary_mean(groupby_variable = "Month").show()
helper_generate_summary_mean(groupby_variable = "Year").show()


#%%
# not finished
# HV ratio

