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

    
# timer(sub, 10,20)

# timer(mult, 20,2)

# timer(add2, 10, 10)

# print(getsource(add2))


def timer2(func):
    def f(x, y=10):
        before = time()
        rv = func(x,y)
        after = time()
        print("Elapsed time:", after-before)
        return rv

    return f


sub_timer = timer2(sub)
add_timer = timer2(add)

@timer2
def sub2(x,y):
    return x - y

# sub2(20,10)

# >>> sub2(20,10)
# Elapsed time: 4.291534423828125e-06
# 10


# add_timer(10)
# add_timer(10, 30)

# add_timer(10, y=50)

# add_timer(10, y=50, z=90)

def add4(x,y,z):
    return x + y + z


def timer3(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print("Elapsed time:", after-before)
        return rv

    return f

add_timer = timer3(add4)

# add_timer(1,2,3)

list1 = [1,2,3]
# *list1

def func_temp(*list1):
    for i in list1:
        print(i)

# func_temp(*list1)

def func_temp2(x,y,z):
    print(x); print(y); print(z)

# func_temp2(*list1)


def func_temp_3(a=1,b=2,c=3):
    print(a); print(b); print(c)


# func_temp_3()
input_dict = {'a':3, 'b':4, 'c':5}
# func_temp_3(*input_dict)
# func_temp_3(**input_dict)

def func_temp_4(*args, **kwargs):
    print(args)
    print(kwargs)


# func_temp_4(1,2,3)
# func_temp_4(1,2,3, a="ddd", b="vai", c=100)


# build a higher order function that is a decorator
# this decorator will make a function run 3 times
def run3times(func):
    def wrapper(*args, **kwargs):
        list_holder = []
        for i in range(3):
            print("run:", i)
            rv = func(*args, **kwargs)
            list_holder.append(rv)
        
        return list_holder

    return wrapper


@run3times
def add4(x,y,z):
    return x + y + z

# add4(1,2,3)


# higher order decorators
# build a decorator that makes any function run an arbitratry n number of times

n = 3
def run_n_times(n):

    def inner(func):
        
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print(f"Run {func.__name__}")
                rv = func(*args, **kwargs)
            return rv
        
        return wrapper
    
    return inner

@run_n_times(5)
def add5(x,y):
    return x + y

# add5(1,2)


add

add6 = run_n_times(4)(add)
# >>> add6(10,20)
# Run add
# Run add
# Run add
# Run add
# 30


# https://youtu.be/7lmCu8wz8ro





























