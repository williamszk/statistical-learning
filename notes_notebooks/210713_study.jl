a = 1
b = 2

a + b

year = 2015
condition = true
letter = 'J'
mass_sum = 1.98e30
flower = "Iris"
flowers

typeof(year)

typeof(letter)

typeof(mass_sum)

typeof(condition)

typeof(flower)

flower + 23

# to find if a variable is of a certain type
isa(flower, String)
isa(flower, ASCIIString)

# there are different ways to convert data
# we can use the function convert() or we can use Float32()
# to conver to Float32
convert(Float32, year)
typeof(year)
Float32(year)

typeof(Float32)

# range
1:24

typeof(1:24)

range(1,10, length=10)
range(0,10,step=.2)
typeof(range(0,10,step=.2))

1.0:0.5:20.0
typeof(1.0:0.5:20.0)

char1 = 'I'

char2 = 'β'
typeof(char2)

species1 = "I. setosa"
typeof(species1)

aDifferentString = "Calçados"
typeof(aDifferentString)

# how to select characters inside a String
aDifferentString[1:3]

# formatted output in string
# string interpolation
println("The first iris species is: $species1")

species3 = "I. virginica"

using Printf
@printf("The 3rd iris species is: %s", species3)
# this is a macro
# macros start with an @ sign

# Symbol type
s1 = :male
typeof(s1)

# a string is an array of characters
# we can loop through them
println("")
for c in species1
    print(c,"-")
end

search(species1, ".")

search("xylophone", 'p')

findfirst(isequal('p'), "xylophone")

findfirst(isequal('.'), species1)

email_pattern = r"(.+)@(.+)"
input = "john.doe@mit.edu"

# the below does not work
ismatch(email_pattern, input)
occursin(email_pattern, input)

occursin('o', "Xylophon")
