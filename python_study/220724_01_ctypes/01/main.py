
import ctypes

def main():
    so_file = "./my_functions.so"
    my_functions = ctypes.CDLL(so_file)

    # print(type(my_functions)) # class ctypes.CDLL

    print(f"{my_functions.square(10) = }")
    print(f"{my_functions.square(8) = }")

if __name__ == "__main__":
    main()
