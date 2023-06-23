
import Data.Complex
import Data.Ratio

n0 :: Int
n0 = 5
-- :type n0

n1::Double
n1 = 5.0
-- :type n1
-- :info n1

n2 :: Complex Double
n2 = 2 :+ 3
-- :type n2

n3 :: Ratio Int
n3 = 2 % 3

main :: IO()
main = do
    print n0
    print n1
    print n2
    print n3
