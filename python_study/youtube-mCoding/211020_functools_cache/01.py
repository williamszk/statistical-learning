# https://www.youtube.com/watch?v=DnKxKFXB4NQ&ab_channel=mCoding
# The Single Most Useful Decorator in Python
from functools import cache
import timeit

def fib1(n):
    """
    """
    if n <= 1:
        return n
    return fib1(n - 1) + fib1(n - 2)

def wraper_func1():
    for i in range(100):
        fib1(i)        

# maybe we need to put the cache decorator on the 
# top of the recursive function
@cache
def fib2(n):
    """
    """
    if n <= 1:
        return n
    return fib2(n - 1) + fib2(n - 2)


def wraper_func2():
    for i in range(100):
        fib2(i)

def main():
    print("Fibonacci function without cache decorator:\n", timeit.timeit(wraper_func1, number=1))    
    print("Fibonacci function with cache decorator:\n", timeit.timeit(wraper_func2, number=1))    

if __name__ == "__main__":
    main()






