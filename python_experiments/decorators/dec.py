# decorators
# an experiment with decorators
# 


def add(x,y ):
    return x + y

# python3 -i dec.py
# >>> add(20,10)

add.__name__

# >>> add.__name__
# 'add'

# what happens when we use __name__ on the script?

# >>> __name__
# '__main__'

# >>> add.__module__
# '__main__'

def add(x,y=10):
    return x + y

# >>> add.__defaults__
# (10,)

# >>> add.__code__
# <code object add at 0x7f82f08783a0, file "/home/william/Documents/statistical-learning/python_experiments/decorators/dec.py", line 25>

# >>> add.__code__.co_code
# b'|\x00|\x01\x17\x00S\x00'
# the byte code for the function

# >>> add.__code__.co_nlocals
# 2
# number of local variables
# what does this means?

def add2(x,y=10,z=30):
    return x + y + z

# >>> add2.__code__.co_nlocals
# 3

# what are the variable names
# >>> add.__code__.co_varnames
# ('x', 'y')

# >>> add2.__code__.co_varnames
# ('x', 'y', 'z')

from inspect import getsource

# >>> getsource(add)
# 'def add(x,y=10):\n    return x + y\n'

# >>> print(getsource(add))
# def add(x,y=10):
#     return x + y

from inspect import getfile
# >>> getfile(add)
# '/home/william/Documents/statistical-learning/python_experiments/decorators/dec.py'


# print('add(10)',      add(10))
# print('add(20,30)',   add(20,30))
# print("add('a','b')", add('a','b'))

from time import time

# before = time()
# print('add(10)',      add(10))
# after = time()
# print("elapsed time:", after - before)

# before = time()
# print('add(20,30)',   add(20,30))
# after = time()
# print("elapsed time:", after - before)

# before = time()
# print("add('a','b')", add('a','b'))
# after = time()
# print("elapsed time:", after - before)


def add3(x,y=10):
    before = time()
    rv = x + y
    after = time()
    print("Elapsed time:", after - before)

    return rv

# eventhough y is a keyword argument we can pass to the function
# add3(20,10) and then 10 would be recognized as the value for
# for keyword argument y
# then for a keyword argument the position is also a valide
# way to pass its value

# print('add3(10)',      add3(10))
# print('add3(20,30)',   add3(20,30))
# print("add3('a','b')", add3('a','b'))


def sub(x, y=10):
    return x - y

def mult(x, y=10):
    return x*y

# run time representations

def timer(func, x,y):
    before = time()
    rv = func(x,y)
    after = time()
    print("Elapsed time:", after - before)
    return rv

    


















