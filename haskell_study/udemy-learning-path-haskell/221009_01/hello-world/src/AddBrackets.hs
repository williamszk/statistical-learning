-- https://www.udemy.com/course/learning-path-haskell-functional-programming-and-haskell/learn/lecture/6898594#overview


-- s needs to be a string
-- ++ will concatenate the strings
addBrackets s = "[" ++ s ++ "]"

-- first argument of map is a function the second argument is a list
result = map addBrackets ["one", "two", "three"]

main = print result