# Install Pkg
using Pkg
Pkg.add("JuliaFormatter")

# Control Structures
x = 25

if x > 20
    println("x is greater than 20")
end

# FizzBuzz
n = 15
if (n % 3 == 0) & (n % 5 == 0)
    println("FizzBuzz")
elseif n % 3 == 1
    println("Fizz")
elseif n % 3 == 0
    println("Buzz")
else
    println(n)
end

# The ternary operator in general should be avoided
x = 3
y = 6
z = (x > y) ? x : y

# Iteration
i = 0
while i < 10
    println("i is: ", i)
    i += 1
end

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for var in nums
    println(var)
end

for var in 1:10
    println(var)
end

1:10

typeof(1:10)