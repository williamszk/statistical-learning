result  = 0
n = 1_000_000
for i in 1:n
    result += sin(rand())
end
show(result)

# inside the repl write
# @time include("glob.jl")