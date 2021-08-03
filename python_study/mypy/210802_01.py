import numpy as np

# https://www.youtube.com/watch?v=H5CnZQDKfhU&ab_channel=anthonywritescode

def square(x: float) -> float:
    return x**2


def log(s:str, *, file=None) -> None:
    ...



from typing import Optional
def logs(s:str, *, filename: Optional[str] = None) -> None:
    ...

# Optional is like nullable

# typing module was added in python 3.5

x: int = 1
# x: int = ...
type(...)

from typing import NamedTuple

# study inheritance
# is this inheritance?
class NT(NamedTuple):
    x: int
    y: int


# python 3.9
from typing import Dict

# old way
def print_items(my_dict: dict[str, str]) -> None: ...


# a test with reveal_type()
reveal_type(NT(1,2).y)
# reveal_type(NT(1,np.int32(2)).y)
# when we run reveal_type, mypy will tell what
# is the type of the variable been passed











