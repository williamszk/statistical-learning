# https://sparkbyexamples.com/pyspark/pyspark-cast-column-type/
#%%
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SparkByExamples.com").\
    getOrCreate()

# %%
simpleData = [("James",34,'2006-01-01',"true","M",3000.60),
    ("Michael",33,'1980-01-10',"true","F",3300.80),
    ("Robert",37,'06-01-1992',"false","M",5000.50)
  ]

# with this format we can get SQL data in the format
# of a list of tuples than convert it into a 
# spark data frame

# %%
columns = ["firstname","age","jobStartDate","isGraduated","gender","salary"]
# %%
type(spark)
df = spark.createDataFrame(data = simpleData, schema = columns)

#%%
# schema can be just a list
# or it can be more elaborate 
# just an experiment

from pyspark.sql.types import (
    StructField,
    StructType,
    StringType,
    IntegerType,
    DateType,
    BooleanType,
    DoubleType
)

#%%

data_schema = [
    StructField("firstname", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("jobStartDate", StringType(), True),
    StructField("isGraduated", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("salary", DoubleType(), True)
]

final_struct = StructType(fields=data_schema)

#%%

type(final_struct)

df_with_schema_list = spark.createDataFrame(
    data = simpleData, 
    schema = columns)

df_with_schema_list.printSchema()

#%%

df_with_schema_struct = spark.createDataFrame(
    data = simpleData, 
    schema = final_struct)

df_with_schema_struct.printSchema()


#%%
df.printSchema()
df.show()

df.show(truncate=False)
#%%
