-- https://www.youtube.com/watch?v=fJRBeWwdby8&t=1563s&ab_channel=DistroTube
-- single comment line
{-
multiline comment
-}

-- all variables in haskell are immutable


-- http://learnyouahaskell.com/chapters

-- https://www.youtube.com/watch?v=fJRBeWwdby8&t=1563s&ab_channel=DistroTube

-- IMPORTS
import Data.List

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










