from dataclasses import dataclass


def main():
    out1 = my_func(11)
    print("out1: ", out1)
    print(f"{isinstance(out1, Option)=}")

    out2 = my_func(9)
    print("out2: ", out2)
    print(f"{isinstance(out2, Option)=}")

    # In Python the child class instance is considered the be an instance of
    # the parent class.
    # This is a way to achieve polymorphism.
    # In Rust this would be achieved in a more idiomatic way using Enums and
    # match with the Option Enum and its variants Some and None.

    # In Python this way of achieving the same syntax wouldn't be idiomatic.


@dataclass
class Option:
    pass


@dataclass
class OptionNone(Option):
    pass


@dataclass
class OptionSome(Option):
    pass


def my_func(arg1: int) -> Option:
    if arg1 > 10:
        return OptionSome()

    else:
        return OptionNone()


if __name__ == "__main__":
    main()
# my_func(11)
# out1:  OptionSome()
# isinstance(out1, Option)=True

# my_func(9)
# out2:  OptionNone()
# isinstance(out2, Option)=True