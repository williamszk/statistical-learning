iris = []

fname = "iris.txt"

# this is similar to context manager from python
open(fname) do file
    # after we finish the do, the file is closed
    for line in eachline(file)

        # println(line)

        # the species name start at column 17
        species = line[17:end]
        species = strip(species)
        push!(iris, species)
    end
end

# println(iris)
# println(length(iris)) # 150
# show(iris) # Any["I. setosa", "I. setosa", "I. setosa", "I. setosa", "I. setosa", ...

# counting species
species_freq = Dict{String, Int64}()
# this is how we define the types inside the dictionary
for species in iris
    haskey(species_freq, species) ? 
        species_freq[species] += 1 : 
        species_freq[species] = 1
    # note that we can use statements inside ternary opearator
    # can we do this with python or javascript?
    # we can do this with javascript
    # true ? a = 2 : a = 3 // 2
    # In Python:
    # a = 2 if True else a = 3 # this doesn't work
end

# sort the keys of the species dictionary
species = sort!(collect(keys(species_freq)))
# println(species) # ["I. setosa", "I. versicolor", "I. virginica"] 
for sp in species
    println("$sp : $(species_freq[sp])")
end
# I. setosa : 50
# I. versicolor : 50
# I. virginica : 50
