# https://www.udemy.com/course/learning-path-julia-explore-data-science-with-julia/learn/lecture/6792678?start=0#overview

# tuples and sets
# dictionaries

tuple_1 = (108, 3.14, "Julia", 'α')

typeof(tuple_1)

# unpacking tuples
a, b, c, d = tuple_1

# exchanging values between variables
a, b = b, a

# how to do string interpolation
println("a is now $a, b is now $b")

for element in tuple_1
    print(element, " - ")
end

# we can't change the elements inside a tuple

# if we want to make a colletion we need to use a set
my_set = Set(Int64[11,2, 2, 3, 7, 14])

my_set_2 = Set(Any[11, 3.14, "Julia", 'α'])
# Any is the most general type in Julia


# we can use set theory operations
intersect(my_set, my_set_2)
union(my_set, my_set_2)
setdiff(my_set, my_set_2)
issubset(my_set, my_set_2)

# dictionaries
iris_dict = Dict(
    "I. setosa" => 50,
    "I. versicolor" => 60,
    "I. virginica" => 70)

iris_dict["I. virginica"]
iris_dict["I. versicolor"]

# we can also use instead of string, symbols
# to represent keys
iris_dict_sym = Dict(
    :setosa => 50,
    :versicolor => 60,
    :virginica => 70)

iris_dict_sym[:setosa]
iris_dict_sym[:virginica]

# we can change the value inside a dict
iris_dict_sym[:versicolor] = 90

# we can use function on dict objects
haskey(iris_dict_sym, :setosa)

# we can access keys and values from dictionaries
values(iris_dict_sym)
keys(iris_dict_sym)

# we can also access the key and value of dicts using for loops
for (k, v) in iris_dict_sym
    println("$k has $v value")
end
