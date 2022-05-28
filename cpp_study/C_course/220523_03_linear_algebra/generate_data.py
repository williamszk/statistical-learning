"""
This script is used to generate data to be used in a linear regression
in the C code.
"""

# Data a linear regression, data generating process
# for 1 feature
n = 30

import numpy as np

np.random.seed(123)

X = np.random.normal(loc=1, scale=2, size=30)
u = np.random.normal(size=30)
y = 3*X + u 

print(X)
print(y)