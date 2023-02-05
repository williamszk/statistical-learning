
# RDD = Resilient Distributed Dataset
# https://www.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3708830#overview
# to start pyspark repl in terminal
# pyspark

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext()

rdd01 = sc.textFile("../datasets/ml-100k/u.data")

type(rdd01)

nums = sc.parallelize([1,2,3,4,5,6,7])

type(nums)

# Transforming RDDs
# map
# flatmap
# filter
# distinct
# sample
# union, intersection, subtract, cartesian

nums.map(lambda x: x*x)

nums.collect()

type(nums.collect())

nums.take(2)

rdd01 = sc.textFile("datasets/ml-100k/u.data")
rdd01.take(10)
type(rdd01.take(10))
type(rdd01.take(10)[0])

#-------------------------------------------- #
nums = sc.parallelize([1,2,3,4,5,6,7])

nums.map(lambda x: x*x)

nums.map(lambda x: x*x).collect()


#-------------------------------------------- #

def square_it(x):
    return x**2

nums.map(square_it).collect()

#-------------------------------------------- #
# take the length of the rdd
nums.count()

nums.countByValue()

type(nums.countByValue())

