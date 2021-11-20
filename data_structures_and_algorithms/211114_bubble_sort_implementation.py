"""
Our objective is to build a bubble sort implementation.

Bubble sort is one of the easiest sort algorithms to implement 
but it is very inneficient.

"""
from time import perf_counter
def time_execution(func, args=None, kwargs=None, n_iter=100):
    start = perf_counter()
    if args is None and kwargs is None:
        for _ in range(n_iter):
            func()
    elif args is not None and kwargs is None:
        for _ in range(n_iter):
            func(*args)
    else:
        for _ in range(n_iter):
            func(*args, **kwargs)

    execution_time = (perf_counter() - start)/n_iter

    return execution_time


def sort_bubble(unsorted_array):
    array_temp = unsorted_array.copy()
    
    len_holder = len(array_temp) - 1

    sort_checker = 0
    while len_holder > sort_checker:
        for i in range(len_holder):
            if array_temp[i] > array_temp[i+1]:
                array_temp[i+1], array_temp[i] = array_temp[i], array_temp[i+1]
                sort_checker = 0
            else:
                sort_checker += 1

    return array_temp


# unsorted_array = [7, 2, 10, 1, 5, 3]
# print(sort_bubble(unsorted_array))


# unsorted_array = [3,1,6,8,3,5,2,4,7]
# print(sort_bubble(unsorted_array))

unsorted_array = [3,1,6,8,3,5,2,4,7]
print(time_execution(sort_bubble, args=[unsorted_array], kwargs=None, n_iter=1000000))