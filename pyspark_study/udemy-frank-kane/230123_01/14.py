
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)
spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

import  pyspark.sql.functions as func 

book = spark.read.option("header", "true").text("datasets/book.txt")
book.take(2)

# func.explode()
# func.split()
# func.lower()
# We can pass columns as parameters
# func.split(df.value, "\\W+")
# filter(df.word != "")
# func.col("colname")

# Data Frames should be used with structured data
# If the data is unstructured try to use RDDs

# We can use RDD and DataFrames in the same program.
# Convert to one and the other when it seems fit.

book = spark.read.text("datasets/book.txt")
book.take(2)

words = book.select(func.explode(func.split(book.value,"\\W+")).alias("word"))
words.show(10)
type(words)
words.printSchema()
words.count()

words = words.filter(words.word != "")
words.count()

lowercaseWords = words.select(func.lower(words.word).alias("word"))
lowercaseWords.show(10)

wordsCount = lowercaseWords.groupBy("word").count()
wordsCount.show(10)

wordsCountSorted = wordsCount.sort("count")
wordsCountSorted.show(10)
wordsCountSorted.count()

wordsCountSorted.show(wordsCountSorted.count())
