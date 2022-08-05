# This is the current way to do type anotation

from collections import namedtuple
from typing import Optional

def square(x: float, k: float) -> float:
    return x * x

square("hi there")


def log(s: str, *, filename: Optional[str] =None) -> None:
    ...



x: int = "str" 


from typing import NamedTuple

class NT(NamedTuple):
    x: int
    y: int

# should we use NamedTuple or dataclass
# https://stackoverflow.com/questions/51671699/data-classes-vs-typing-namedtuple-primary-use-cases
# https://peps.python.org/pep-0557/#why-not-just-use-namedtuple



