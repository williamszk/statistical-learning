"""
The objective here is to test python's implicit
modification of an object or instance, let's see how this works.
"""


def my_func_implicit_change(my_object):
    my_object["a"] = 10

    return None
    # notice that the function doesn't return anything
    # but internally in the function we are altering the
    # the object


class MyClassTestImplictModification:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return (
                f"a = {self.a}\n"
                f"b = {self.b}\n"
                f"c = {self.c}\n"               
        )


def my_func_implicit_change_class(my_instance):
    my_instance.a = 10
    return None


def main():
    print("The dictionary before the modification.")

    a_dictionary = {
        "a": 1,
        "b": 2,
        "c": 3,
    }

    print(a_dictionary)

    my_func_implicit_change(a_dictionary)

    print("The dictionary after the function for implicit modification.")

    print(a_dictionary)
    # the output is: {'a': 10, 'b': 2, 'c': 3}
    # which means that the function implicitly altered the object
    # because the value of key "a" is now is not 1 but 10

    print(
            "\n\n"
            "The function for implicit modification just returns None.\n"
            "So Python accepts implicit modification of an object.\n"
            "That is, the function will alter the state of the object\n"
            "internally. Without the need for explicit return of a new object.\n"
            "Inside the function Python will make modifications to an object, much\n"
            "like procedures, and not like pure functions.\n\n\n"
            "Maybe in JavaScript this is also the case, let's try doing this experiment.\n\n"
            "But before let's see if Python will implicitly modify an attribute of\n"
            "an instance.\n"
    )
    
    print("My instance before the function.")
    my_instance = MyClassTestImplictModification(1,2,3)
    print(my_instance)

    my_func_implicit_change_class(my_instance)
    
    print("My instance after the function.")
    print(my_instance)

    print(
            f"We can see that Python will implicilty modify the state of an object\n"
            f"in an implicit way.\n"
            f"In the same way that happens with an object like a dictionary,\n"
            f"the same will happen with an instance of a class.\n"
            )












if __name__ == "__main__":
    main()


