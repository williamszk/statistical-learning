"""
vector2d.py: a simplistic class demonstrating some special methods.

It is simplistic for didactic reasons. It lacks proper error handling,
especially in the ``__add__`` and ``__mul__`` methods.
This example is greatly expanded later in the book.
Addition::
    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)
Absolute value::
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0
Scalar multiplication::
    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0
"""


from array import array
import math
from typing import Iterable

class Vector2d:
    typecode = "d" # this is called a class attribute

    def __init__(self, x,y ) -> None:
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}({self.x}, {self.y})"
        # return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self) -> str:
        return str(tuple(self))

    def __bytes__(self):
        return (bytes(ord(self.typecode))) + bytes(array(self.typecode, self))

    def __eq__(self, other) -> bool:
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))