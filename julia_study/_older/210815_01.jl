a = 1
# using functions

function sum_2(x,y,z)
    return x + y + z
end

# generic functions can recieve many
# types of inputs

show(sum_2(2,3,4))
sum_2(2.1, 3.2, 4.3)
sum_2(true, false, true)

typeof(sum_2)

typeof(true)

function sum_prod(x, y)
    x+y, x*y
end

# this will give an error
# sum_2("Iris", 7, true)

# we can specify the types of data
function sum_3(x::Int64, y::Int64, z::Int64)
    return x + y + z
end


sum_3(2,3,4.2)

function sump(x::Int64, y::Int64, z::Int64 )
    p::Int64 = x * y * z
    return x + y + z + p
end

sump(2,3,4)

sump(2,3,4.2)

# what to do when the number of arguments is variable
# in Python we would use *args, **kwargs
function sumvar(args...)
    # the three dots is called the "splat operator"
    # this function sums a variable number of
    # arguments
    sum = 0
    for n in args
        sum += n
    end
    return sum
end

sumvar(1,2,3)
sumvar(1,2,3.4,8.1)
# the splat operetor works with 0 arguments
sumvar()

# ------------------------------------- #
# optional arguments
# in python those are called keyword arguments

function sum_4(n1, n2, n3=5, n4=-9)
    return n1 + n2 + n3 + n4
end

sum_4(1,2)
sum_4(1,2,3)
sum_4(1,2,3,10)

function sum_5(n1, n2, n3=5; n4=-9)
    return n1 + n2 + n3 + n4
end

sum_5(1,2,9,n4=10)
# this is strange

# ------------------------------------- #
# anonymous function
# lambda expression

(x,y,z) -> x + y + z

arr = rand(100)

# map function with anonymous function
arr2 = map(x -> x^2, arr)
# map is a function
# one of its arguments is another funtion

# julia has list comprehensions
arr3 = [x^2 for x in arr]

# isodd is a builtin function in julia
isodd(2)
isodd(10)

# this is another way to build function is julia
isodd_2(n) = (n % 2 != 0)

isodd_2(10)

round.(Int64, rand(100)*100)
# maybe the (.) dot is used to tell julia
# that we want to use a function that works with atomic data
# to pass in all elements of an array

round(Int, 3.123)

Int64(1.0)
convert(Int64, 2.)

typeof(rand(100)*100)
# vector of floats

[round(x) for x in rand(100)*100]

round(3.123)

[round(Int64, x) for x in rand(100)*100]

round.(rand(100)*100)

round.(Int, rand(100)*100)
# Int is Int64 by default


filter(isodd_2, [1,2,3,4,5])

filter(isodd_2, round.(Int, rand(100)*100))

# writing the same vector
filter(n -> n % 2 != 0, round.(rand(100)*100))

# In both R and Julia we have the concept of vectors

# another way to filter data using list comprehensions
[x for x in round.(rand(100)*100) if isodd_2(x)]

# see performance of code and functions
@time round.(Int64, rand(100)*100)
# sump (generic function with 1 method)
#   0.000008 seconds (3 allocations: 2.625 KiB)

function dummy_function()
    result = 0
    n = 1_000_000
    for i in 1:n
        result += sin(rand())
    end
    return result
end


@time dummy_function()
# 0.046266 seconds

# julia macros start with a @

@time include("210815_02_test_time_macro.jl")
# 0.328680 seconds (477.89 k allocations: 22.184 MiB)
# when we change the initial type to a float and not an integer
# we can increase performance
# 0.069083 seconds (18.77 k allocations: 1.085 MiB)

# when calling another script julia takes much more time
# when we include scripts we can use find in project
# to find where a certain function was defined
