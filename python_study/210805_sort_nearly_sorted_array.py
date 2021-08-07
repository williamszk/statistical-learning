# https://www.geeksforgeeks.org/nearly-sorted-algorithm/



def sort_insertion_method_k_sorted(arr, k=4):
    arr_sorted = arr.copy()
    for i, num in enumerate(arr[:-1], start=1):
        print(i)
        j = i
        while j > 0 and arr_sorted[j-1] > arr_sorted[j] and j >= i - k :
            arr_sorted[j-1],arr_sorted[j] =  arr_sorted[j], arr_sorted[j-1]
            j -= 1
    return arr_sorted


arr = [10, 9, 8, 7, 4, 70, 60, 50]
sort_insertion_method_k_sorted(arr, k=4)
# [4, 7, 8, 9, 10, 50, 60, 70]


