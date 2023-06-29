
myMap :: (a->b) -> [a] -> [b]
myMap _ [] = []                     -- base case
myMap f (a : as) = f a : myMap f as -- other cases

-- (a : as)
-- cons operator
-- `a` is the first element
-- `as` is the rest of the list
-- if (a : as) = [1, 2, 3, 4]
-- `a` = 1 and `as` = [2 ,3, 4]

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter _ [] = [] -- base case
myFilter f (a : as) = if f a then a : myFilter f as else myFilter f as


-- this is like reduce
-- it could be like (+ a b)
-- `b` acts as a initial value
-- `[a]` acts as a list of values
myFold :: (a -> b -> b) -> b -> [a] -> b
myFold _ b [] = b
myFold f b (a : as) = myFold f (f a b) as

main::IO()
main=do
    print $ myMap show [10,20,30]
    print $ myFilter (< 25) [10, 20, 30]
    print $ myFold (+) 100 [10, 20, 30]

-- monoid is a type where we can apply map, filter and reduce

