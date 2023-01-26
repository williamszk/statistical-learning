from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

lines = sc.textFile("./datasets/ml-100k/u.data")
type(lines)

ratings = lines.map(lambda x: x.split()[2])

type(ratings)

key_value_ratings = ratings.map(lambda x: (x,1))

type(key_value_ratings)

res01 = key_value_ratings.reduceByKey(lambda x,y: x+y)

type(res01)
res01.collect()

dict(res01.collect())

key_value_ratings.groupByKey()

key_value_ratings.groupByKey().collect()

