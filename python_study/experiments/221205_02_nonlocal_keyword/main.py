# https://www.geeksforgeeks.org/python-nonlocal-keyword/

def main():
    foo()

def foo():
    name = "The name of foo"
    print(f"      from foo: {name}")

    def bar():
        nonlocal name 
        name = "The name of bar"
        print(f"      from bar: {name}")

    bar()

    print(f"again from foo: {name}")

if __name__ == "__main__":
    main()
