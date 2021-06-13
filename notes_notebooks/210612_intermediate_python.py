# https://www.youtube.com/watch?v=HGOBQPFzWKo&ab_channel=freeCodeCamp.org

my_list = [1,"apple",2,3,"banana","cherry"]
# print(my_list)


my_list_2 = list()
# print(f"my_list_2: {my_list_2}")

my_list_3 = []
# print(f"my_list_3: {my_list_3}")

from collections import Counter

a = "aaaaabbbbcccc"
my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# for i in my_counter.items():
#     print(i)

# print({"a":2,"C":[True,False]}.items())

text = "genetically similar, but morphologically distinct, leading scientists to recognize them as separate species. The animal was first known to science after an individual was observed in 2004, and S. durrelli was described as a new species in 2010. A small, reddish-brown carnivore,"
list_text = text.split(" ")

# print(Counter(list_text))

# if we pass a list to a Counter
# the Counter function returns a dictionary
# where the key is element of the list
# and the values are the times that each element appears
# it is really similar to value_counts from pandas


my_counter = Counter(list_text)
# print(my_counter.most_common(1))
# it return a list of tuples
# 
# print(type(my_counter))
# print(my_counter)
# print(my_counter.elements())
# for i in my_counter.elements():
#     print(i)


from collections import namedtuple

# namedtuple will create a class
# that is why Point is capitalized
Point = namedtuple('Point','x,y')
point = Point(1,-4)
# print(type(point))
# print(point.x)
# print(point.y)


from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2

# print(ordered_dict)
# ordered_dict.pop("b")

# print(type(ordered_dict))

from collections import defaultdict

d = defaultdict(list)
d['a'] = 1
d['b'] = 2
d['c'] = "b"
d['d'] = "10"

# print(d["f"])


from collections import deque

d = deque()

d.append(1)
d.append(2)

# print(d[0])

# # print(type(d))
# d.appendleft(3)
# print(d)
# d.popleft()
# print(d)
# d.pop()
# print(d)

# d.clear()
# print(d)

# %timeit d.extend([3,4])
# d.extend([3,4])
# 248 ns ± 0.455 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
# print(d)

# d2 = d + deque([3,4])
# print(d2)

# %timeit d2 = d + deque([3,4])
# 383 ns ± 6.34 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)


# d.extendleft([43,4])
# print(d)
# d.rotate(1)
# print(d)

# does list have rotate method?
# R: no, only deques have rotate
# a = [1,2,3]
# a.rotate(1)

# String: ordered, immutable, text representation
# https://youtu.be/HGOBQPFzWKo?t=3542







