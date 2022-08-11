


print("hello world")
-- This is a comment

--[[
    This is a multi line 
    comment
]]

-- Strings can be double or single quotes
name = "Bob"
name2 = 'Dennis'

-- An alternative way to print
io.write("Size of string ", #name, "\n")
-- #name gives the size of the string

-- we can change the type of the variable
name = 4

io.write("My name is ", name, "\n")

-- Lua only has floats, that are called just numbers
num1 = 99.00
io.write("My number's type is ", type(num1), "\n")


-- multiline string
longString = [[I 
am a long string 
that goes on forever.]]

io.write(longString,"\n")

-- concatenate strings

name = "Bobson"

longString2 = longString .. name
io.write(longString2,"\n")

isAbleToDrive = true
io.write("Type of isAbleToDrive ",type(isAbleToDrive) ,"\n")

-- everything in lua by default gets a value of nil
-- print an undeclared variable
io.write(type(madeupvar), "\n")

-- in lua it is not allowed to do:
-- var++
-- var--
-- var += 1 this is not allowed too
-- the alternative is var = var + 1

-- generate random numbers
math.randomseed(os.time())
-- without randomseed the random value is fixed
-- random number between 0 and 1
io.write("math.random() ",math.random(), "\n")
-- random number between 1 and 10
io.write("math.random(10) ",math.random(10), "\n")
-- random number between 5 and 100
io.write("math.random(5, 100) ",math.random(5, 100), "\n")

-- float point numbers work till 13 digits after the period
print(string.format("Pi = %.10f", math.pi))

-- in Lua not equal is ~= not !=
-- we use: and or not

age = 30 

if age < 16 then
    io.write("Too young", "\n")
    localVar = 10 -- this variable can't be found outside the if statement
elseif age >= 16 and age < 60 then
    io.write("You are an adult", "\n")
else
    io.write("You are old", "\n")
end

print("The localVar can't be found outside the if scope ", localVar)

print(string.format("not true = %s", tostring(not true)))

-- in Lua there is no ternary operator
-- canVote = age >= 18 ? true : false
-- this is an alternative
canVote = age > 18 and true or false
print(string.format("canVote = %s", tostring(canVote)))

-- there is no switch operators in Lua

-- Stoped at:
-- https://youtu.be/iMacxZQMPXs?t=1158 
