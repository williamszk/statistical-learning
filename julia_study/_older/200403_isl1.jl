
using Pkg
Pkg.add("RCall") #install package RCall

#https://github.com/JuliaData/RData.jl
Pkg.add("RData") #to read R data from Julia


#http://juliainterop.github.io/RCall.jl/stable/gettingstarted
using RCall #to call R code into julia
