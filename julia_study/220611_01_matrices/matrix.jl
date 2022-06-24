
# can we build a struct with the same characteristics as this Array using C?
# lengths = Array(Float64, 1, 4) # create an empty (initialized with arbitrary values) array 
lengths = [0 0 0 0]

fname = "../data/iris.txt"

open(fname) do file
    for line in eachline(file)
        # println(line)
        mlengths = line[1:16]
        # println(mlengths)
        arr_temp = split(mlengths)
        # println(arr_temp)
        arr_mlengths = [parse(Float64, str) for str in arr_temp]
        arr_mlengths = reshape(arr_mlengths, 1, 4)
        # println(typeof(arr_mlengths))
        global lengths = vcat(lengths, arr_mlengths)
    end
end

# cut out the first line which have only values with zeros
lengths = lengths[2:end, :] 

println(lengths)

println(typeof(lengths))

println("size:", size(lengths))


using Statistics

mt_setosa = lengths[1:50,:]
println(mean(mt_setosa[:, 1]))
println(mean(mt_setosa[:, 2]))
println(mean(mt_setosa[:, 3]))








