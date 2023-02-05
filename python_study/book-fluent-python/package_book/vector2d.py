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

import math

class Vector:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    # not finished yet...