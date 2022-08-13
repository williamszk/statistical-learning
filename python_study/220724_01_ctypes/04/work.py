

def average(list_nums):
    import ctypes
    _lib = ctypes.cdll.LoadLibrary("./libwork.so")
    _lib.average.argtypes = [(ctypes.c_double*len(list_nums)), ctypes.c_int]
    _lib.average.restype = ctypes.c_double

    len_list = len(list_nums)
    list_nums_c = (ctypes.c_double*len(list_nums))(*list_nums)

    result = _lib.average(list_nums_c, len_list)
    print(f"{result = }")
