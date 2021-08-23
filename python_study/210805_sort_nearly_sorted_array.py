# https://www.geeksforgeeks.org/nearly-sorted-algorithm/


#%%
def sort_insertion_method_k_sorted(arr, k=4):
    arr2 = arr.copy()

    for i, num in enumerate(arr[:-1], start=1):
        j = i
        while j > 0 and arr2[j-1] > arr2[j] and j >= i - k :
            arr2[j-1],arr2[j] =  arr2[j], arr2[j-1]
            j -= 1
    return arr2


arr = [10, 9, 8, 7, 4, 70, 60, 50]
sort_insertion_method_k_sorted(arr, k=4)
# [4, 7, 8, 9, 10, 50, 60, 70]

#%%

def sort_insertion_method_k_sorted(arr, k=4):
    len_arr = len(arr)
    for i in range(1,len_arr):
        j = i
        while (j > 0) and (arr[j-1] > arr[j]) and (j >= i - k):
            arr[j-1],arr[j] =  arr[j], arr[j-1]
            j -= 1
    return arr


arr = [10, 9, 8, 7, 4, 70, 60, 50]
sort_insertion_method_k_sorted(arr, k=4)
# [4, 7, 8, 9, 10, 50, 60, 70]

#%%

def sort_insertion_method_k_sorted(arr, k=4):
    len_arr = len(arr)
    for i in range(1,len_arr):
        i_0 = 0 if i-k < 0 else i-k
        for j in range(i, i_0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] =  arr[j], arr[j-1]
            else:
                break

    return arr


arr = [10, 9, 8, 7, 4, 70, 60, 50]
sort_insertion_method_k_sorted(arr, k=4)
# [4, 7, 8, 9, 10, 50, 60, 70]
#%%
def sort_insertion_method_k_sorted_1(arr, k=4):
    len_arr = len(arr)
    for i in range(1,len_arr):    
        j = i
        while j > 0 and arr[j-1] > arr[j] and j >= i - k :
            arr[j-1], arr[j] =  arr[j], arr[j-1]
            j -= 1
    return arr

arr = [10, 9, 8, 7, 4, 70, 60, 50]
sort_insertion_method_k_sorted_1(arr, k=4)

#%%
arr = [10, 9, 8, 7, 4, 70, 60, 50]
i = 5
# def insert(arr, i):

e = arr[i]
i_initial = 0 if i-k < 0 else i-k
ids_larger = [j for j, x in enumerate(arr[i_initial: i]) if x > e]
j_substitute = i if len(ids_larger)==0 else ids_larger[0]


k = 4
def sort_insertion_method_k_sorted_1(arr, k=4):
    len_arr = len(arr)
    for i in range(1,len_arr):    
        [j for j in range(1,k+1)]

    return arr

arr = [10, 9, 8, 7, 4, 70, 60, 50]
sort_insertion_method_k_sorted_1(arr, k=4)

#%%
def sort_insertion_method_k_sorted_2(arr, k=4):
    len_arr = len(arr)
    for i in range(1, len_arr):    
        [(i,num) for i, num in enumerate(arr)]


# the sorted item
# list1.append()

import numpy as np
from numpy.core.fromnumeric import ndim

# def insert_smaller(i, arr, k=4)
k=4
i = 6
elem = arr[i]
i_0 = 0 if i-k < 0 else i-k
mask = np.array(arr[i_0:i+1]) > elem






def insert_wrong(e, arr):
    arr2 = None
    e = np.array(e, ndmin=1)
    arr = np.array(arr)
    # arr must be an ordered array
    mask = np.array(arr) < e
    first = arr[mask]
    last = arr[~mask]
    arr2 = np.concatenate([first, e, last]) 
    return arr2


arr = [2,4,6,7,9,11]
e = 5

def insert(e, arr):
    first = arr[0]
    rest = arr[-1]
    if first >= e:
        return [e,first,rest]
    else:
        return [first] + insert(e, [rest])


insert(5, [2,4,6,7,9,11]) 
insert(-10, [2,4,6,7,9,11]) 
insert(100, [2,4,6,7,9,11]) 
insert(8, [2,4,6,7,9,11]) 


def insertion_sort(arr):
    first = arr[0:1]
    rest = arr[1:]
    return insert(first, insertion_sort(rest))


insertion_sort([2,3,4,1,5,7634,23,4,32])
