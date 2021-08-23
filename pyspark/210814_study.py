
"""
# how make python know where spark is
# in the terminal write:

export SPARK_HOME="/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2"
export PATH=$SPARK_HOME:$PATH
export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
export PYSPARK_DRIVER_PYTHON="jupyter"
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
export PYSPARK_PYTHON=python3

# to give permission to spark directory
sudo chmod 777 spark-3.1.2-bin-hadoop3.2

"""

#%%
# import sys
# import os
# 
# os.getcwd()
# sys.path.append("../")
# we need to import from a parent directory

# import pyspark
#%%
# we can use package findspark
# pip3 install findspark
# import findspark
# findspark.init('path to spark directory')
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

#%%
from pyspark.sql import SparkSession

#%%
spark = SparkSession.builder.appName("Basics").getOrCreate()

df = spark.read.json("../data/people.json")

df.show()
type(df)

df.printSchema()

df.columns

df.describe()
df.describe().show()


#%%
# how to define a schema in spark
from pyspark.sql.types import (
    StructField, 
    StringType, 
    IntegerType, 
    StructType
)

data_schema = [
    StructField('age', IntegerType(), True),
    StructField('name', StringType(), True)
]

final_struct = StructType(fields=data_schema) 

df = spark.read.json('../data/people.json', schema=final_struct)
df.show()
df.printSchema()
type(df)
# pyspark.sql.dataframe.DataFrame
#%%
df["age"]
type(df["age"])
# pyspark.sql.column.Column
# in this way we return a column object
# not a data frame
#%%
df.select("age")
type(df.select("age"))
# pyspark.sql.dataframe.DataFrame

df.select("age").show()
#%%
df.head(2)
# [Row(age=None, name='Michael'), Row(age=30, name='Andy')]
# this returns a list of row objects
type(df.head(2))
# list

df.head(2)[0]
# Row(age=None, name='Michael')
# this is a row object
type(df.head(2)[0])
# pyspark.sql.types.Row
#%%
# how to select multiple columns?
df.select(["age","name"])
df.select(["age","name"]).show()

#%%
# how to define a new column
df.withColumn('newage', df["age"])
df.withColumn('newage', df["age"]).show()
df.show()

df.withColumn('double_age', df["age"]*2).show()

#%%
# how to rename a column?
df.withColumnRenamed("age","my_new_age").show() 


#%%
# sql query
# this registers 'people' as a sql temporary view 
# that is we make 'df' as 'people' in the world
# of sql
df.createOrReplaceTempView('people')
results = spark.sql("SELECT * FROM people")
results.show()

new_results = spark.sql(
    "SELECT * FROM people "
    "WHERE age>=30"
)
new_results.show()

#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%




