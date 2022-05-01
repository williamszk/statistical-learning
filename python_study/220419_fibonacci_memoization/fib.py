"""
Build a function that calculates any fibonacci number
using recursion and memoization.
"""


class Fib:
    store = None

    def calculate(n):
        if Fib.store is None:
            Fib.store = dict()

        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            if Fib.store.get(n):
                return Fib.store.get(n)

            Fib.store[n] = Fib.calculate(n-2) + Fib.calculate(n-1)

            return Fib.store[n]


"""
A non OOP way to have some kind of memory

def fib(n, memoi_store = None):
    if memoi_store is None:
        memoi_store = {}
    if n == 0:
        return 1, memoi_store
    elif n == 1:
        return 1, memoi_store
    else:
        if memoi_store:
            if memoi_store.get(n):
                return memoi_store.get(n)
            
            memoi_store[n] = fib(n-2) + fib(n-1)

        return fib(n-2) + fib(n-1)
"""

def fib_no_memoi(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib_no_memoi(n-2) + fib_no_memoi(n-1)

if __name__ == "__main__":

    ROUNDS_FIB = 40

    from time import perf_counter

    start = perf_counter()
    for n in range(ROUNDS_FIB):
        fib_no_memoi(n)
    print(f"fib_no_memoi elapsed time: {perf_counter() - start}")

    start = perf_counter()
    for n in range(ROUNDS_FIB):
        Fib.calculate(n)

    print(f"Fib.calculate(n) elapsed time: {perf_counter() - start}")



# (.venv) C:\Users\william.suzuki\Documents\statistical-learning\python_study\220419_fibonacci_memoization>python fib.py
# fib_no_memoi elapsed time: 53.261612400000004
# Fib.calculate(n) elapsed time: 0.0001068999999986886