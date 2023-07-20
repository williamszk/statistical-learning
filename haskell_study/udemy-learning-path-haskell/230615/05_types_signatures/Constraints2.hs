myFold :: (a -> b -> b) -> b -> [a] -> b
myFold _ b [] = b
myFold f b (a : as) = myFold f (f a b) as

-- the only difference is to define mySum
mySum :: Num a => [a] -> a
mySum = myFold (+) 0

main :: IO ()
main = print $ mySum [10, 20, 30]
