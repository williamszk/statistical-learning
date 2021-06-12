#https://www.youtube.com/watch?v=8981sTtV3bI

# maybe you need to install CSV package
# import Pkg
# Pkg.add("CSV")
using CSV

# Pkg.add("DataFrames")
using DataFrames

pwd()

auto = CSV.read("Auto.csv")


typeof(auto)

println(first(auto,5))

println(last(auto,5))

println(names(auto))

typeof(names(auto))

size(auto)

println(describe(auto))

auto.cylinders

println(auto.cylinders)

println(typeof(auto.cylinders))

println(names(auto))
auto[:,1]
println(auto.mpg)

auto[:,[1,2,3]]
auto[:,[1,2,3]]
first(auto[:,[1,2,3]],5)

auto[1:5,:]





