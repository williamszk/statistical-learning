
def main():
    a = 17
    b = 21
    print(f"main:\t a = {a}, b = {b}")
    swap(a,b)
    print(f"main:\t a = {a}, b = {b}")

    def swap2(a, b):
        a, b = b, a
        print(f"swap2: a = {a}, b = {b}")

    swap2(a,b)
    print(f"main:\t a = {a}, b = {b}")

    def swap3():
        a, b = b, a # this will give error
        # the function can only see global variables
        # not a local one that is declared in a higher scope
        print(f"swap3: a = {a}, b = {b}")

    swap3()
    print(f"main:\t a = {a}, b = {b}")



def swap(a, b):
    a, b = b, a
    print(f"swap:\t a = {a}, b = {b}")

if __name__ == "__main__":
    main()