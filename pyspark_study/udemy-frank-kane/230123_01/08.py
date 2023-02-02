
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

# ==============================================================================

lines = sc.textFile("datasets/redfox.txt")
lines.take(2)

rageCaps = lines.map(lambda x: x.upper())
rageCaps.collect()

# The flatMap will expand the RDD into a larger RDD
words = lines.flatMap(lambda x: x.split())
words.collect()

# ==============================================================================

lines = sc.textFile("datasets/book.txt")
lines.take(2)
words = lines.flatMap(lambda x: x.split())
words.take(2)
wordCounts = words.countByValue()

type(wordCounts)

for word, count in wordCounts.items():
    cleanWord = word.encode("ascii", "ignore")
    if (cleanWord):
        print(cleanWord, count)

# regular expressions
lines = sc.textFile("datasets/book.txt")

# ==============================================================================

import re

def normalizeWords(text):
    return re.compile(r"\W+", re.UNICODE).split(text.lower())

lines = sc.textFile("datasets/book.txt")
words = lines.flatMap(normalizeWords)
wordCounts = words.countByValue()

for word, count in wordCounts.items():
    cleanWord = word.encode("ascii", "ignore")
    if (cleanWord):
        print(cleanWord, count)


# ==============================================================================
# Count frequency of words the hard way
wordCounts = words.map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y) # type: ignore

wordCounts.take(2) # type: ignore
# [('self', 111), ('an', 178)]

# Flip the key and value, then sort by key 
wordCountsSorted = wordCounts.map(lambda x: (x[1], x[0])).sortByKey() # type: ignore
wordCountsSorted.take(10)
wordCountsSortedColl = wordCountsSorted.collect()
# [(1, 'achieving'), (1, 'contents'), (1, 'preparation'), (1, 'skillset'), (1, 'determination'), (1, 'blame'), (1, 'devoted'), (1, 'commuted'), (1, 'rewarded'), (1, 'marriage')]

for word, count in wordCountsSortedColl:
    print(word, count)



