# https://www.geeksforgeeks.org/nearly-sorted-algorithm/




def insertion_sort(arr):
    i, key, j = 0, 0, 0
    for i, v in enumerate(arr):
        key = arr[i]
        

import heapq
import copy

from numpy import sort

def sort_k(arr: list, k: int):
    """
    Parameters
    -------
    `arr`: Input array.
    `k`: Maximum distance which every element is away from its target position.
    """
    arr_hold = copy.deepcopy(arr)

    N = len(arr_hold)

    # list of the first k items
    heap = arr_hold[:k+1]

    # using heapify to convert list into heap or min heap
    heapq.heapify(heap)
    # why do we need this step? it makes the heap into a min heap
    # if we don't use this it will be treated as a max heap

    target_index = 0
    for rem_elem_index in range(k+1, N):
        arr_hold[target_index] = heapq.heappop(heap)
        heapq.heappush(heap, arr_hold[rem_elem_index])
        target_index += 1
    
    while heap:
        arr_hold[target_index] = heapq.heappop(heap)
        target_index += 1

    return arr_hold

def main():
    arr1 = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    out_arr1 = [2, 3, 5, 6, 8, 9, 10]

    print(sort_k(arr1, k) == out_arr1)


    arr2 = [10, 9, 8, 7, 4, 70, 60, 50]
    k = 4
    out_arr2 = [4, 7, 8, 9, 10, 50, 60, 70]

    print(sort_k(arr2, k) == out_arr2)

if __name__ == "__main__":
    main()


