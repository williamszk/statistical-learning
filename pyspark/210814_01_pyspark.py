
#%%
import findspark
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("operations").getOrCreate()

#%%
# df = spark.read.csv("../data/appl_stock.csv")
# the problem with this read is that spark does not infer header

df = spark.read.csv("../data/appl_stock.csv", inferSchema=True, header=True)

df.show()

df.printSchema()

df.head(1)[0]

#%%
# this is using a sql like query
df.filter("Close < 500").show()

df.filter("Close < 500").select("Open").show()

df.filter("Close < 500").select(["Open", "Close"]).show()

# here we use a boolean mask more like python
df.filter(df["Close"] < 500).show()
df["Close"] < 500
type(df["Close"] < 500)
# pyspark.sql.column.Column

df.filter(df["Close"] < 500).select("Volume").show()

#%%
# grab all lines that have Close < 200
# and Open > 200

df.filter(
    (df["Close"] < 200) & 
    (df["Open"] > 200)
    ).show()

# an example of ~ to negate the boolean column
df.filter(
    (df["Close"] < 200) & 
    ~(df["Open"] > 200)
    ).show()


df.filter(df["Low"]==197.16).select("Date").show()

# the method collect() will transform the spark data frame 
# into a list
result = df.filter(df["Low"]==197.16).collect()
result[0]
result[0].asDict()
# {'Date': '2010-01-22',
#  'Open': 206.78000600000001,
#  'High': 207.499996,
#  'Low': 197.16,
#  'Close': 197.75,
#  'Volume': 220441900,
#  'Adj Close': 25.620401}

# how can we transform a spark data frame into a pandas data frame?



#%%







# %%






