# https://www.geeksforgeeks.org/nearly-sorted-algorithm/



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




def sort_insertion_method_k_sorted_2(arr, k=4):


    [(i,num) for i, num in enumerate(arr)]


