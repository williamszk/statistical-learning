#%%
import findspark
from numpy.lib.twodim_base import triu_indices_from
findspark.init("/home/william/Documents/statistical-learning/spark-3.1.2-bin-hadoop3.2")

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ops").getOrCreate()
# %%
df = spark.read.csv(
    "../data/appl_stock.csv",
    inferSchema=True,
    header=True)
# %%
df.show()
# %%
df.printSchema()
# %%
df.filter("Open < 500").show()
# %%
df.filter("Open < 500").select(["Open","Close"]).show()
# %%
df.filter(df["Close"] < 500).select(["Open","Close"]).show()
# %%
df.filter((df["Open"]<200) & (df["Close"]>200)).show()
# %%
df.filter((df["Open"]<200) & ~(df["Close"]>200)).show()
# %%
df.filter(df["Low"] == 197.16).show()
# %%
df.filter(df["Low"] == 197.16).collect()
# %%
result = df.filter(df["Low"] == 197.16).collect()
# %%
row = result[0]
# %%
row.asDict()
# %%
row.asDict()["Date"]
# %%
row.asDict()["Adj Close"]
# %%
