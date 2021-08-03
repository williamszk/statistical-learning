

temperature = [98.1, 87.1, 102.2]

flu_status = [false, false, true]

species1 = "I. setosa"
species2 = "I. versicolor"
species3 = "I. virginica"

iris_species = [species1, species2, species3]

iris_species[3]
iris_species[2:3]

# iris_species[4] = "I. albicans"
# gives error
iris_species[3] = "I. albicans"

typeof(iris_species)

length(iris_species)

arr1 = collect(1:5)

arr2 = Float64[]
push!(arr2, 5.1)
push!(arr2, 3.5)
# when the fucntion have exclamation points means that
# the object itself is changed

println("")
show(arr2)
println("")

# produce random vectors
randn(5)
# this is a standard Gaussian distribution

rand(10)
# this is a uniform 0 to 1 distribution

# maybe I could use the Statistics with R and apply Julia to the book

for s in iris_species
    print(s, " / ")
end
# I. setosa / I. versicolor / I. virginica /

arr3 = [11, "Julia", 3.14, "α"]
# vectors in Julia can have any type
# they are different from np.array
# they can have more than 1 type of data

for item in arr3
    println(item,": ",typeof(item))
end


# arrays are used a lot in data science code
