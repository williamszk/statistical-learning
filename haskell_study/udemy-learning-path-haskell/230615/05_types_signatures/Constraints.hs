myFold :: (a -> b -> b) -> b -> [a] -> b
myFold _ b [] = b
myFold f b (a : as) = myFold f (f a b) as
-- this is like an accumulator or a reduce

main :: IO ()
main = print $ myFold (+) 0 [10, 20, 30]
