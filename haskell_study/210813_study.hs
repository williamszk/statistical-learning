-- https://www.youtube.com/watch?v=fJRBeWwdby8&t=1563s&ab_channel=DistroTube
-- single comment line
{-
multiline comment
-}

{-
ghci

-- load file
:l 
-- reload file
:r
-}

-- all variables in haskell are immutable


-- http://learnyouahaskell.com/chapters

-- https://www.youtube.com/watch?v=fJRBeWwdby8&t=1563s&ab_channel=DistroTube

-- IMPORTS
import Data.List ()

-- TYPES
-- Bool, Int, Integer, Float, Double, Char, [Char], Tuples

-- Lists in Haskell need to have single type items
-- Tuples in Haskell can have multiple types

trueAndFalse :: Bool
trueAndFalse = True && False
-- use command
-- :l
-- to load the file
trueOrFalse :: Bool
trueOrFalse = True || False

notTrue :: Bool 
notTrue = not(True)

-- Int type
-- type Int does have a limit
-- Integer does not have a limit
maxInt :: Int
maxInt = maxBound :: Int

-- *Main> maxInt
-- 9223372036854775807

-- to reload the program, type:
-- :r

minInt :: Int 
minInt = minBound :: Int

-- :: Integer
-- Unbounded whole number

numFive :: Integer
numFive = 5

numFive' :: Float
numFive' = 5.0

boolFive :: Bool
boolFive = 5 > 4

myDouble :: Double
myDouble = 1.0 + 2
-- Haskell can handle sum of two different types

-- :: Char
-- use single quotes
singleChar :: Char
singleChar = 'a'

-- Strings are lists of characters

myName :: [Char]
myName = "Derek"

myName' :: [Char]
myName' = ['D','e','r','e','k']

-- above are the same things, they different ways to write

-- Math
addNum :: Integer
addNum = 3 + 6

modNum :: Integer
modNum = mod 9 2
-- prefix operator

modNum' :: Integer
modNum' = 9 `mod` 2
-- infix operator

addNeg :: Integer
addNeg = 4 + (-4)

{-
-- other math operators
pi
exp
log
sin
cos
tan
asin
acos
atan
-}


truncDouble :: Integer
truncDouble = truncate 1.2312341231

roundDouble :: Integer
roundDouble = round 1.2312341231

ceilDouble :: Integer
ceilDouble = ceiling 1.2312341231

floorDouble :: Integer
floorDouble = floor 1.2312341231















