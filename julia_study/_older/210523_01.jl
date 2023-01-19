1 + 1

β = 1
γ = 2

α = β + γ

println("hello")


println("α = ", α)




println("I love crunching data.")

a = 2
b = 106

c = a + b

println(c)


year = 2015

condition = true

letter = "J"

mass_sun = 1.9e30

flower = "iris"

typeof(year)

typeof(flower)

typeof(mass_sun)


# julia is strongly typed
# it prohibts operations with different data types
flower + 28

1.2 + 2

typeof(1.2)


isa(1.2, Int64)

isa(1.2, Float64)

typeof(3)

convert(Float64, 3)

convert(Int64, 3.43)

Int64(3.21)

Int64(3.00)

year

Float64(year)

range(1; length=10)

# ?range

char1 = "I"

char2 = "β"


typeof(char1)

typeof(char2)

species = "I. versicolor"

species[1]

typeof(species)
# String

typeof(species[1])
# Char


# string interpolation
println("The first iris species is: $species")
@printf "The first iris species is: %s" species



































