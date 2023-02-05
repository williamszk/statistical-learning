# In the terminal run the repl
# pyspark
from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

lines = sc.textFile("./datasets/ml-100k/u.data")
# lines.collect()
lines.take(10)

ratings = lines.map(lambda x: x.split()[2])
ratings.take(10)

result = ratings.countByValue()
result
type(result)

result.items()

result.keys()

result["4"]

sorted_results = sorted(result.items())

for key, value in sorted_results:
    print(f"{key}: {value}")

# -------------------------------------------------------
# Key-value RDD

nums = sc.parallelize([1,2,3,4,5,6,7])

# this will create a key-value RDD 
totals_by_age = nums.map(lambda x: (x, 1))

type(totals_by_age)

totals_by_age







