
a :: Int; a = 1234

a :: Int; a = 1234

-- it is not yet evaluated
:sprint a
:type a
a
:sprint a

b :: Integer; b = 2 ^ 70
:sprint b
:type b
b
:sprint b

import Data.List
:type intercalate
intercalate ":" ["/path/to/dir0", "/path/to/dir1"]

formatList s e sep xs = s ++ (intercalate sep (map show xs)) ++ e
-- formatList s e sep xs = s ++ (intercalate sep (map show xs)) ++ e

formatList "[" "]" "," ["1","2", "3"]
xs = ["1","2", "3"]
xs = ["a","b", "c"]
show xs
map show xs


formatList "(" ")" "," [1,2,3]

square x = x^2
squareSum x y = square x + square y
squareSum 3 4

-- $ is used as a way to reduce the use of parenthesis
f = let s = "hello world" in putStrLn $ "(" ++ s ++ ")"
f

f = let s = "hello world" in putStrLn ("(" ++ s ++ ")")
f


-- "function composition" according to the instructor is the act of
-- piping the return of a function into another so that we create another
-- function.
-- I called this act as "function chaining" or "method chaining".

doubleIt x = x * 2
:type doubleIt
doubleIt 5

addTen x = x + 10
:type addTen
addTen 15

addTen (doubleIt 5)
-- below is an alternative
addTen $ doubleIt 5
doubleIt $ addTen 5

-- below is another alternative
-- this is the composition syntax
-- "addTen composed with doubleIt applied to 5"
(addTen . doubleIt) 5
(doubleIt . addTen) 5

show (addTen (doubleIt 5))
show $ (addTen . doubleIt) 5
show $ addTen $ doubleIt 5
(show . addTen . doubleIt) 5

f = show . addTen . doubleIt
:type f

-- "map" is a higher order function
-- because we can pass functions to the map which is another function
map f [10, 11, 12, 13, 14]
-- this is the longer version
map (show . addTen . doubleIt) [10, 11, 12, 13, 14]

-- this is a lambda function
\x -> x + 1

-- lambda functions receive only one argument
-- any function can be composed in such a way so that it only receives one argument

\x y -> x + y
-- above is a syntax sugar for:
\x -> \y -> x + y

-- the function \x will return another function
\x -> (\y -> x + y)

:{
parenthesizeWords s = unwords $ map parenthesizeWord (words s)
    where parenthesizeWord s = "(" ++ s ++ ")"
:}

s = "We love Haskell"
words s
:type words

unwords $ words s

parenthesizeWords s


parenthesizeWords s = unwords $ map (\s -> "(" ++ s ++ ")") (words s)
parenthesizeWords s

-- two way of defining a function
parenthesizeWord s = "(" ++ s ++ ")"
parenthesizeWord = \s -> "(" ++ s ++ ")"

parenthesizeWords s = unwords $ map parenthesizeWord (words s)
parenthesizeWords s

parenthesizeWord = ("(" ++) . (++ ")")
parenthesizeWord s
-- this is a function
("(" ++) 
-- it prepends "(" on its operand
:type ("(" ++)

-- this is also a function
(++ ")") 
-- it appends a ")" on its operand

-- sections

-- infix function
func x y = show x ++ show y
:type func

func 1 2

x `func` y = show x ++ show y
1 `func` 2


leftSection = (5 `func`)
:type leftSection
leftSection 6

rightSection = (`func` "five")
:type rightSection
rightSection 1

foo x y z = x ++ y ++ z
foo "aaa" "bbb" "ccc"
-- function saturation happens when we pass all the necessary arguments
:type foo

-- partial application is when we pass fewer than necessary arguments
x = foo "aaa"
:type x

y = x "bbb"
:type y

y "ccc"
:type y "ccc"

z = y "ccc"
:type z


-- range 
[1..10]

-- filter less than 5
lessThanFive x = x < 5
filter lessThanFive [1..10]
filter (\x -> x < 5) [1..10]

:type (< 5)
(< 5) 10 -- False
(< 5) -- this is a function 
filter (< 5) [1..10]

-- which is faster R or Haskell?

map (* 2) $ filter (< 5) [1..10]











