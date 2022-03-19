from cffi import FFI

CDEF = """\

"""

ffibuilder = FFI()
ffibuilder.cdef(CDEF)
ffibuilder.set_source(
    "_uuidcffi",
    "#include <uuid/uuid.h>",
    libraries=["uuid"],
    
)

