# insertion sort

# https://stackabuse.com/sorting-algorithms-in-python
# https://www.youtube.com/watch?v=JU767SDMDvA&ab_channel=MichaelSambol

def sort_insertion_method(arr):
    arr_sorted = arr.copy()
    for i, num in enumerate(arr[:-1], start=1):
        print(i)
        j = i
        while j > 0 and arr_sorted[j-1] > arr_sorted[j]:
            arr_sorted[j-1],arr_sorted[j] =  arr_sorted[j], arr_sorted[j-1]
            j -= 1
    return arr_sorted

def test_sort_insertion_method_01():
    arr = [10, 9, 8, 7, 4, 70, 60, 50]
    assert sort_insertion_method(arr) == [4, 7, 8, 9, 10, 50, 60, 70]


def test_sort_insertion_method_02():
    arr = [1, 4, 1, 2, 7, 5, 2]
    assert sort_insertion_method(arr) == [1, 1, 2, 2, 4, 5, 7]


def test_sort_insertion_method_03():
    arr = [37,35,69,17,73,53,84,2,34,69,86]
    assert sort_insertion_method(arr) == [2, 17, 34, 35, 37, 53, 69, 69, 73, 84, 86]



