import sys

sys.path.append("..")
from package_book.vector2d_v0 import Vector2d


v1 = Vector2d(3, 4)

print(v1.x, v1.y)
print(v1)
print(repr(v1))

x, y = v1
print(x, y)

# eval will receive a string and evaluate it as code
out01 = eval("10 + 2")
print(out01)

v1_clone = eval(repr(v1))
print(v1_clone)

v1 == v1_clone

abs(v1)

abs(Vector2d(3, 4))
