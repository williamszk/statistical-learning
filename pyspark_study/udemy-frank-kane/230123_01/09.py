
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

# ==============================================================================

# 0 - customerId
# 1 - itemId
# 2 - amountSpent


lines = sc.textFile("./datasets/customer-orders.csv")
lines.take(2)

def parseLine(line):
    fields = line.split(',')
    customerId = fields[0]
    amountSpent = fields[2]
    return (int(customerId), float(amountSpent))

amountSpentPerCustomer = lines\
    .map(parseLine)\
    .reduceByKey(lambda x,y: x+y)\
    .sortByKey()\
    .collect()

for customerId, amountSpent in amountSpentPerCustomer:
    print(f"{customerId} \t $ {amountSpent:.2f}")


# ==============================================================================
# Sort by amount spent

amountSpentPerCustomerSortByAmount = lines\
    .map(parseLine)\
    .reduceByKey(lambda x,y: x+y)\
    .map(lambda x: (x[1], x[0]))\
    .sortByKey()\
    .map(lambda x: (x[1], x[0]))\
    .collect()


for customerId, amountSpent in amountSpentPerCustomerSortByAmount:
    print(f"{customerId} \t $ {amountSpent:.2f}")














