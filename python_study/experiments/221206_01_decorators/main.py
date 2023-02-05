"""About decorators
"""
from typing import Callable, Any

# Make decorators using functions
def enchanting_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        # ----------------------
        print("Do something before...")
        # ----------------------
        out = func(*args, **kwargs)
        # ----------------------
        print("Do something after...")
        # ----------------------
        return out

    return wrapper


class terrific_decorator:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print("Do something before...")
        out = self.func(*args, **kwargs)
        print("Do something after...")
        return out


@enchanting_decorator
def foo():
    print("Doing some important stuff inside the foo function...")


@terrific_decorator
def bar():
    print("Doing some important stuff inside the bar function...")


def wonderful_decorator(arg1: str, arg2: str):
    def outer(func):
        def inner(*args, **kwargs):
            print(f"Do something before using {arg1 = }")
            out = func(*args, **kwargs)
            print(f"Do something after using {arg2 = }")
            return out

        return inner

    return outer


@wonderful_decorator("why's poignant guide", "do or do not, don't try")
def chunky():
    return "I love bacon!"


def main():
    foo()
    print(f"{type(foo) = }")

    bar()
    print(f"{type(bar) = }")

    print(f"{terrific_decorator.__mro__ = }")

    print(f"{chunky() = }")


if __name__ == "__main__":
    main()
