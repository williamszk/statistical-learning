# https://www.udemy.com/course/learning-path-julia-explore-data-science-with-julia/learn/lecture/6792674#overview

α = 20

println(α)

# initialize several variables at the same time
a = b = c = 4

n, m = 1, 2

# the last expression is evaluated to area
area = (r = 3; π*r^2)
area

x = begin
    a = 2
    b = 3
    a + b
end

x # 5
# the last expression is evaluated to x

body_temp = 38.5

if body_temp > 38
    println("This person has fever")
elseif 35 < body_temp <= 47
    println("This person has normal temperature")
else
    println("This person has hypothermia")
end
# This person has fever

# the if else can be an expression
n = 10; m = 15

max = if n > m  n
    else m
    end

max # 2

# using ternay operator
max = n > m ? n : m
# 2

year = 2016
while year <= 2020
    println("increase year")
    year += 1
end

while year <= 2050
    println("increase year")
    year += 1
    if year == 2047
        println("reached 2047")
        break
    end
end


while true
    println("I do not stop!")
end

blood_groups = ["A", "B", "AB", "O"]
# Vector of strings

typeof(blood_groups)
# Vector Strings

typeof(blood_groups[1])
# String

# we can loop over a vector
for blg in blood_groups
    print("$blg / ")
end

# we can use enumerate too
for (ix, blg) in enumerate(blood_groups)
    println("Blood-group no. $ix is $blg.")
end

for i in 1:5
    print("$i - ")
end

code = "X"
if code in blood_groups
    println("We have a supply of blood group $X")
else
    throw(DomainError)
end
# MethodError: no method matching DomainError()

if code in blood_groups
    println("We have a supply of blood group $X")
else
    error("Blood Group Unknown!")
    # we could just use the error() function
    # we can specify the message of what went wrong
end
# this is the traditional error handling adopted by:
# Python and JavaScript
# but different from Go



if code in blood_groups
    println("We have a supply of blood group $X")
else
    @warn("Blood Group Unknown!")
end
# warn is not defined
# Warning: Blood Group Unknown!
# └ @ Main ~/Documents/statistical-learning/julia_study/220426_01.jl:116
# It just gives a warning in the console
#%%
z = @async 26 * 78
println("In the mean time I calculate other things")
println(consume(z))
# consume is not define julia
# consume seems to be deprecated
# now we can use channels

#%%
# we can use try and catch
try
    open("test.txt")
catch ex
    println(ex)
    # showerror(STDOUT, ex)
    println("")
end
println("I recoverd from the exception")
# STDOUT not defined
# use alt+enter to run the code block
#%%
