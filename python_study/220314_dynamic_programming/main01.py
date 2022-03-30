import time


def fib(n):
    if n < 2:
        return n
    
    return fib(n-1) + fib(n-2)
# this is a O(2^n) complexity very inneficient

start = time.perf_counter()
print(fib(30), "Time:", time.perf_counter() - start)


# this is algorithm have O(n) complexity
# it uses a technique called memoization
def fib_memoization(n, cache={}):
    if n < 2:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fib_memoization(n - 1, cache) + fib_memoization(n - 2, cache)

    return cache[n]

start = time.perf_counter()
print(fib_memoization(30), "Time:", time.perf_counter() - start)



