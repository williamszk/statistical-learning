





my_tuple = (1,2)
my_int = 2


my_tuple + my_int
# this gives an error

my_tuple + (my_int)
# parenthesis doesn't make a difference, still error


# what if the internal elements of the tuple are numpy numbers?
import numpy as np
my_tuple_numpy = (np.int64(1), np.int64(2))
type(my_tuple_numpy)
type(my_tuple_numpy[0])

my_tuple_numpy + my_int
# this gives error


my_tuple_numpy + (my_int)
# this also gives error

# what if all numbers involved are numpy?
my_int_numpy = np.int32(2)

# with int numpy and tuple numpy
my_tuple_numpy + my_int_numpy
# this works but it will broadcast the sum
# and it will return a numpy array

my_tuple_numpy + (my_int_numpy)
# this will gie the same as above

type(my_tuple_numpy)
# tuple

type((my_int_numpy))
# numpy.int32

# Conclusion:
# we can sum a tuple to an np.intXX, but all the elements of the tuple
# must also be numpy numbers.



my_tuple_numpy + (my_int_numpy,)
# when we include a comma after inside the parenthesis the
# second object becomes a tuple, and a sum of tuples
# is a concatenation of tuples
# (1, 2, 2)
# each element is a numpy number
type((my_tuple_numpy + (my_int_numpy,))[0])
# numpy.int64



