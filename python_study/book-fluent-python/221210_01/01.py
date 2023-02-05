import sys
from array import array

sys.path.append("..")
from package_book import vector2d_v0

my_vec = vector2d_v0.Vector2d(1, 2)
my_iter = iter(my_vec)
for i in my_iter:
    print(i)

print(repr(my_vec))

print(str(my_vec))
print(my_vec)

print(bytes(my_vec))

# v1 = Vector2d(3,4)

print(my_vec.typecode)
print(bytes(ord(my_vec.typecode)))

print(array)