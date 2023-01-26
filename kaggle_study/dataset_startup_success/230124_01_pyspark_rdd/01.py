# Make some data exploration with pyspark
# Objectives:
# 1. ingest the csv
# 2. Make some kind of operation in the data.
# Transform the .csv into .parquet

import json
from pyspark import SparkConf, SparkContext
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

rdd01 = sc.textFile("./datasets/big_startup_secsees_dataset.csv")
header = rdd01.first()
rdd02 = rdd01.filter(lambda row: row != header)
rdd03 = rdd02.map(lambda row: row.split(","))
header2 = header.split(",")

rdd03.count() # 66368

first_row = rdd03.take(1)[0]
len(header2) # 14
len(first_row) #  14
dict_first_row = {f"{cnt} - {key}":value for cnt, key, value in zip(range(14), header2, first_row)}
print(json.dumps(dict_first_row, indent=2))

# >>> print(json.dumps(dict_first_row, indent=2))
# {
#   "0 - permalink": "/organization/-fame",
#   "1 - name": "#fame",
#   "2 - homepage_url": "http://livfame.com",
#   "3 - category_list": "Media",
#   "4 - funding_total_usd": "10000000",
#   "5 - status": "operating",
#   "6 - country_code": "IND",
#   "7 - state_code": "16",
#   "8 - region": "Mumbai",
#   "9 - city": "Mumbai",
#   "10 - funding_rounds": "1",
#   "11 - founded_at": "",
#   "12 - first_funding_at": "2015-01-05",
#   "13 - last_funding_at": "2015-01-05"
# }

# Count the frequency region and city
# they are index 8 and 9 respectively

freq_region = rdd03.map(lambda x: x[8]) \
    .map(lambda x: (x, 1))  \
    .reduceByKey(lambda x,y: x+y)

freq_region.count() # 1156
freq_region02 = freq_region.collect()
freq_region03 = {key: value for key, value in freq_region02}

fig = plt.figure()
pd.Series(freq_region03).plot()
fig.savefig("output.png")

# Ideally we should use a Map to figure out where in the world they are...









