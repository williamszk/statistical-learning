myFold :: (a -> b -> b) -> b -> [a] -> b
myFold _ b [] = b
myFold f b (a : as) = myFold f (f a b) as

-- the only difference here is that we don't care the type
-- mySum :: _
mySum :: [Integer] -> Integer
mySum = myFold (+) 0

main :: IO ()
main = print $ mySum [10, 20, 30]
