# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f)
    print(f"{type(f) = }")
    print(f"{dir(f) = }")

    print(f"{type(f.__call__) = }")  # <class 'method-wrapper'>, what is a method-wrapper?
    f.__call__("presunto", "ovo")

    print(f"{type(f.__annotations__) = }")
    print(f"{f.__annotations__ = }")


def f(ham: str, eggs: str = 'eggs') -> str:
    """Example function, mix ham and eggs.

    :param ham:
    :param eggs:
    :return:
    """
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
