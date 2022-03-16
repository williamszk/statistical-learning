
import time


input_arr = [-7, 3, 4, -2, -3, 1, -3]

# cache = {}

# def sum_array(start, end, input_arr, cache):
    
#     sum(input_arr[start:end])


# assert sum_array(0, 3, input_arr) == 0


# -------------------------------------------------- #
# this is O(n^2)
# not dynamic, and inneficient
def min_subarray_sum(array):
    if len(array) == 0:
        return 0
    
    min_sum = float("inf")

    for i in range(len(array)):
        for j in range(i + 1, len(array) + 1):
            subarray = array[i:j]
            min_sum = min(min_sum, sum(subarray))
    
    return min_sum

start = time.perf_counter()
[min_subarray_sum(input_arr) for _ in range(10000)]
print("Elapsed Time 1:", time.perf_counter() - start)

# -------------------------------------------------- #
array = [20, -7, -3, 9, -4, 6, -9, 10]

# this next solution is O(n) linear
# and it saves the information of the previous step in the current_min
# this is also dynamic programming
def min_subarray_sum_dp(array):
    if len(array) == 0:
        return 0

    min_sum_using_element = [array[0]]
    min_sum = array[0]

    for i in range(1, len(array)):
        num = array[i]
        current_min = min(num, num+min_sum_using_element[i-1])
        min_sum_using_element.append(current_min)
        min_sum = min(min_sum, current_min)
    
    return min_sum












