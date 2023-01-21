
x = rand(10^7)

sum(x)

using PyCall

py"""
def py_sum(x):
    s = 0.0
    for i in x:
        s += i
    return s
"""

py_sum = py"py_sum"

py_builtin_sum = pybuiltin("sum")

py_sum(x)
py_builtin_sum(x)
sum(x)

py_sum(x) == sum(x)
py_sum(x) ≈ sum(x)
py_builtin_sum(x) ≈ sum(x)

# ---------------------------------------------------------
# NumPy implementation
numpy_sum = pyimport("numpy").sum
numpy_sum(x)

numpy_sum(x) ≈ sum(x)

# ---------------------------------------------------------
# Comparing with R
using RCall

R"""
r_sum <- function(x){
    s = 0.0
    for (i in 1:length(x)){
        s = s + x[i]
    }
    return(s)
}
"""

r_sum = R"r_sum"

# r_sum(x) ≈ sum(x)
r_sum(x)

r_buildint_sum = R"sum"

r_buildint_sum(x)

r_sum(x)[1] ≈ sum(x)

typeof(r_sum(x))
typeof(r_sum(x))
typeof(r_sum(x)[1])

r_buildint_sum(x)[1] ≈ sum(x)


# ---------------------------------------------------------
# Julia self implementation

function jl_sum(x)
    s = 0.0
    for i in x
        s += i
    end
    s
end


jl_buildin_sum = sum

# single instruction multiple data (simd)
function jl_simd_sum(x)
    s = 0.0
    @simd for i in x
        s += i
    end
    s
end


jl_sum(x) ≈ sum(x)
jl_simd_sum(x) ≈ sum(x)

# ---------------------------------------------------------------------------
#= 
# I'm having problems running C code inside julia
# C implementation
using Libdl

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
=#
# ---------------------------------------------------------------------------

using BenchmarkTools
# using Pkg
# Pkg.add("BenchmarkTools")

impls = [r_sum, r_buildint_sum, py_sum, py_builtin_sum, numpy_sum, jl_sum, 
    jl_buildin_sum, jl_simd_sum]

labels = ["R", "R built-in", "Python", "Python built-in", "Numpy", "Julia", 
    "Julia built-in", "Julia SIMD"]

times = map(impls) do impl
    # call function multiple times
    bench = @benchmark ($impl)($x)

    # minimum time in milliseconds
    minimum(bench.times) / 1e6
end

# ---------------------------------------------------------------------------
using UnicodePlots
# Pkg.add("UnicodePlots")

# sort times in increasing order
idx = sortperm(times)
labels = labels[idx]
time = times[idx]

# times for all implementations
barplot(labels, time, title="Time [milliseconds]")

# speedup for all implementations
barplot(labels, round.(Int, time[end] ./ time), 
    title="Speedup relative to slowest ($(labels[end]))")

