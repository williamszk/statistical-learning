# how to open julia repl?
# type the following in the terminal:
# $ julia

# we can use the julia extension from vscode to open a repl
# > julia repl

# how to run a julia script on the terminal?

# https://docs.julialang.org/en/v1/manual/style-guide/
# Use 4 spaces per indentation level.

# It is also worth emphasizing that functions should take arguments, instead of operating 
# directly on global variables (aside from constants like pi).
# https://github.com/invenia/BlueStyle

# functions should be snake case

count1 = 10
count2 = 20

function my_func_logger()
    total_count = count1 + count2
    println(total_count)
end

my_func_logger()
















