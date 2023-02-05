
#=
I'm having problems trying to run C code inside julia...
=#

using Libdl

# ------------------------------------------------------------------------
Ccode = """
#include <stdio.h>

int my_func(int x){
    printf("Hello World %d\n", x);
    return 0;
}
"""

const Clib = tempname() # make temporary file
open(`gcc -fPIC -O3 -shared -xc -o $(Clib * "." * Libdl.dlext) -`, "w") do f
    print(f, Ccode)
end

#  c_sum(x) = ccall(("c_sum", Clib),  Float64, (Csize_t, Ptr{Float64}), length(x), x)
my_func(x) = ccall(("my_func", Clib), Cint, (Int64,), x)
my_func(42)

# ------------------------------------------------------------------------

x = rand(10^7)
# C implementation

# this is just a string
Ccode = """
#include <stddef.h>
double c_sum(size_t n, double *x){
    double s = 0.0;
    for (size_t i = 0; i < n; ++i){
        s += x[i];
    }
    return s;
}
"""

# compile to shared library by piping Ccode to gcc
const Clib = tempname() # make temporary file
open(`gcc -fPIC -O3 -shared -xc -o $(Clib * "." * Libdl.dlext) -`, "w") do f
    print(f, Ccode)
end

`gcc -fPIC -O3 -shared -xc -o $(Clib * "." * Libdl.dlext) -`
tempname()
"gcc -fPIC -O3 -shared -xc -o $(Clib * "." * Libdl.dlext) -"

# the same as above but with a -ffast-math flag added
const Clib_fastmath = tempname() # make temporary file
open(`gcc -fPIC -O3 -shared -ffast-math -xc -o $(Clib_fastmath * "." * Libdl.dlext) -`, "w") do f
    print(f, Ccode)
end
`gcc -fPIC -O3 -shared -xc -o $(Clib_fastmath * "." * Libdl.dlext) -`

# define the julia native function equivalent from C
c_sum(x) = ccall(("c_sum", Clib), Float64, (Csize_t, Ptr{Float64}), length(x), x)

c_fastmath_sum(x) = ccall(("c_sum", Clib_fastmath), Float64, (Csize_t, Ptr{Float64}), lenght(x), x)

c_sum(x)

