
-- this is a comment

{- this is 
a multiple line comment
-}

-- https://www.youtube.com/watch?v=fJRBeWwdby8&ab_channel=DistroTube


{-
how to run the haskell program?
in the terminal wirte: ghci
then write :l tutorial.hs
to reload the program, write :r 
you can write the variable in the console 
and it will show the value, e.g.
> trueAndFalse
to clear the screen of ghci
> :!clear
-}

-- lazy language

-- learnyouahaskell.com
-- haskell.org

-- IMPORTS
import Data.List

-- TYPES
-- Bool, Int, Integer, Float, Double, Char, [Char], Tuples ()

-- ::Bool
-- True or False
trueAndFalse = True && False
trueOrFalse = True || False
notTrue = not(True)

-- :: Int
-- Whole number -2^63  2^63
maxInt = maxBound :: Int
-- 9223372036854775807

minint = minBound :: Int
-- -9223372036854775808


-- :: Integer
-- unbounded whole number
numFive :: Integer
numFive = 5
-- numFive :: Integer

{-
:t numFive
to get the type of numFive
-}

numFive' :: Float
numFive' = 5.0
-- numFive' :: Float

numSix = 6 :: Float

boolFive = 5 > 4

myFloat = 1.0 + 2.5
-- myFloat :: Double
-- the compiler sets by default Double

myDouble = 1.55555555555 + 0.0000000001

-- :: Char
-- 

singleChar = 'a'

myName = "Derek"
myName' = ['D','e','r','e','k' ]
-- :r
-- :t myName

-- -- MATH -- -- -- -- -- -- -- -- -- -- 

addNum = 3 + 6
subNum = 3 - 6
multNum = 3 * 6
divNum = 3 / 6
modNum = mod 9 2
-- prefix operator mod

modNum' = 9 `mod` 2
-- infix operator

addNeg = 4 + (-10)


-- pi 
-- 3.141592653589793

{-
pi, exp, log, sin, cos, tan, asin, acos, atan
-}

truncDouble = truncate myDouble
roundDouble = round myDouble
ceilDouble = ceiling myDouble
floorDouble = floor myDouble

-- squareFive = sqrt numFive
-- the above gives an error because numFive is an Integer

-- :t sqrt
-- sqrt :: Floating a => a -> a
squareFive = sqrt numFive'


-- LISTS
-- lists need to contain just one type of data

numList = [1,2,3,4,5]

rangeList = [1..5]

alphaList = ['a'..'z']
-- "abcdefghijklmnopqrstuvwxyz"
alphaList2 = ['A'..'Z']
-- "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphaList3 = ['A'..'z']
-- "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz"

evenNums = [2,4..20]
-- [2,4,6,8,10,12,14,16,18,20]

oddNums = [1,3..20]
-- [1,3,5,7,9,11,13,15,17,19]

oddAlphabet = ['a','c'..'z']
-- "acegikmoqsuwy"

sumNumList = sum [1..5]

sumNumList2 = sum numList

prodNumList = product numList

-- how to figure out if an element is part of a list?
elemList = elem 5 numList
-- True

elemList' = 6 `elem` numList
-- False


fibNumbers = [1,1,2,3,5,8]
moreFibs = [13,21,34,55,89,144]

combineFibs = fibNumbers ++ moreFibs
-- *Main> combineFibs 
-- [1,1,2,3,5,8,13,21,34,55,89,144]

-- https://youtu.be/fJRBeWwdby8?t=1563











