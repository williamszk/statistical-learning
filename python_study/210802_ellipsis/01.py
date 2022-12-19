# https://stackoverflow.com/questions/42190783/what-does-three-dots-in-python-mean-when-indexing-what-looks-like-a-number/42191121
import numpy as np


for i,x in np.ndenumerate(a):
    x[...] = 2 * x


# https://stackoverflow.com/questions/42190783/what-does-three-dots-in-python-mean-when-indexing-what-looks-like-a-number/42191121
# The ellipsis ... means as many : as needed.
X = np.reshape(np.arange(9), (3,3))

Y = np.reshape(np.arange(2*3*4), (2,3,4))

X
X[:,0]
X[...,0]

Y[0,:,:]
Y[1,:,:]

Y[0,...]
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

Y
# array([[[ 0,  1,  2,  3],
#         [ 4,  5,  6,  7],
#         [ 8,  9, 10, 11]],

#        [[12, 13, 14, 15],
#         [16, 17, 18, 19],
#         [20, 21, 22, 23]]])

Y[0,...,0]
# array([0, 4, 8])














