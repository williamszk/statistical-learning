from ctypes import *

lib = CDLL("./libbasic.so")

class SomeStructure(Structure):
    _fields_ = [
        ('i', c_int),
        ('c', c_char),
        ('s', c_char_p),
    ]


# notice that lib here is define above using CDLL
# which will read the .so file a shared object file
lib.someFunction.restype = c_double
lib.someFunction.argtypes = [POINTER(SomeStructure)]

s_obj = SomeStructure(3, 'q', b"hello world")
result = lib.someFuncion(byref(s_obj))
print(f"result: {result}, new value for text: {str(s_obj.s)}")
