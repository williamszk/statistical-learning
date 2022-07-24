
def main():
    import ctypes

    NUM = 16
    # libfun loaded to the python file
    # using fun.myFunction(),
    # C function can be accessed
    # but type of argument is the problem.
    c_functions = ctypes.CDLL("./libfun.so")
    # Now whenever argument
    # will be passed to the function
    # ctypes will check it.

    c_functions.myFunction.argtypes = [
        ctypes.c_int
    ]

    return_value = c_functions.myFunction(NUM)

    print(f"{return_value = }")


if __name__ == "__main__":
    main()
