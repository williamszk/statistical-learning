-- this is a comment in lua

print("Hello World") -- this prints to the standard out

print("Oi")

--[[
  This is a 
  multiline comment
]]

print("Oi dois")

-- concatenate strings
print("Hello".." ".."Bob")

-- Data Types and Variables

-- nil
-- number
-- string
-- boolean
-- table
--

local my_var = 2
print(my_var)

local my_var_2
print(my_var_2)

my_var = true
print(my_var)

my_var = "Jackson"
print(my_var)

-- multiline string
local my_multiline_str = [[This is
a multiline
string]]

print(my_multiline_str)

-- to define a global variable just declare 
HELLO = 10
-- Or we can use
_G.HELLO3 = 30

print(HELLO)
print(HELLO3)

-- to see the type of a variable
print(type(HELLO))

-- Math
local my_num = "22"
print("type of my_num: "..type(my_num))
-- convert string to number
print("after conversion: "..type(tonumber(my_num)))

print("2^5: "..2^5)
print("10 % 3: "..10 % 3)

-- math library
print("math.pi: "..math.pi)
print("math.random(): "..math.random())

-- we can fix the randomness by using seeds
math.randomseed(1)
print("with seed math.random(): "..math.random())

-- using time to set seed
math.randomseed(os.time())
print("with time based seed math.random(): "..math.random())
print("os.time(): "..os.time())

-- create integer random values
math.random(10)
print(math.random(10))


-- strings
print(string.lower("HELLO THERE"))
print(string.upper("bye there"))

-- get length of string
local my_str = "Hi there again!"
print("length of my_str #my_str: "..#my_str)
-- alternative way of getting the string length
print("length of my_str string.len: "..string.len(my_str))















