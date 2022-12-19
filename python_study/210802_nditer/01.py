# https://numpy.org/doc/stable/reference/generated/numpy.nditer.html

# https://www.youtube.com/watch?v=XawR6CjAYV4&ab_channel=codebasics

import numpy as np

a = np.arange(12).reshape(3,4)

for row in a:
    print(row)


for row in a:
    for cell in row:
        print(cell)


# how to flat the ndarray?

for item in a.flatten():
    print(item)
# this gives the same result


# nditer
# n dimensional iterator

for x in np.nditer(a, order='C'):
    print(x)
# with C order this is equivalent to flatten()
# in the C order the iterator goes row by row
# in Fortran order the iterator goes column by column

a
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

for x in np.nditer(a, order='F'):
    print(x)

# 0
# 4
# 8
# 1
# 5
# 9
# 2
# 6
# 10
# 3
# 7
# 11























