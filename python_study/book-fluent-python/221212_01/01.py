# array in python
# https://towardsdatascience.com/do-you-know-python-has-built-in-array-c2afa4200b97
# import array
from array import array

# array.typecodes
# 'bBuhHiIlLqQfd'


# u: unicode character
arr = array("u", "abcdefg")
arr
type(arr) # array.array
len(arr) # 7

arr.typecode # "u"

# check size of each item
arr.itemsize # 4

# to count the occurrence of a certain element in the array
my_list = ["a", "b", "c", "b", "z", "b"]
my_list.count("b")
my_list.count("a")
my_list.count("c")

table_frequencies = {key: my_list.count(key) for key in set(my_list)}
table_frequencies

arr.count("b")

arr.append("h")
arr

arr.extend("ijk")
arr

arr.index("c")

my_list.index("c")
my_list.index("C")

arr.insert(2, "x")
arr

my_list.insert(2, "x")
my_list

my_str = "".join([x for x in arr])
type(my_str)

arr
arr.pop(2)
arr

my_list
my_list.pop(2)
my_list

arr.reverse()
arr

my_list_1  = arr.tolist()
my_list_1







