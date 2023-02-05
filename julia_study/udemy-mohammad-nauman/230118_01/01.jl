
# Prepare julia to be used inside jupyter notebooks
using Pkg
Pkg.add("IJulia")

#=
]
add IJulia
=#

s = "hey "
s ^ 3

versioninfo()


using Pkg
Pkg.add("Plots")

awesome_var = 25
😸
🥻
😄
α
β
γ
Γ
🐈
🐱

😸 = "😸"
😸

typeof(😸)
typeof('a')
typeof("a")

σ = 2.5

sqrt(σ^2)

println("σ = ", σ)

# ? println

answer = 42
typeof(answer)

π = 3.1415
typeof(π)

a, b = 10, 20
println(a)
println(b)

:4
typeof(:4)

:b
typeof(:b) # Symbol

:this_is_symbol
typeof(:this_is_symbol)

[1,2,3.4]

# builtin support for rational numbers
4//2

5//2 + 4//2

5//2 + 9//3

convert(Float64, 1)
typeof(convert(Float64, 1))

convert(Int64, 20.23)
convert(Int64, 20.000)

typeof(9//2) # Rational{Int64}

convert(Float64, 9//2) # 4.5

true && false
true || false

name = "Bob"
age = 20
println("The customer's name is $(name) who is $(age) years old.")

# String concatenation
s1 = "Awesome"
s2 = "Blossom"

s1 * s2

join([s1, s2], " ")

# repeat the string 3 times
s1 ^ 3

# https://www.udemy.com/course/julia-programming-language-from-zero-to-expert/learn/lecture/25889912#overview











