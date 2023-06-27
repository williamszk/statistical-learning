list00::[Int]
list00 = [1,2,3,4,5]

list01::[Int]
list01=[1..10]

list02::[Int]
list02=[1,3..10] -- [1,3,4,5,6,7,8,9]
-- why it went until 9 and not 10?

list03::[Int]
list03=[1..]

list04::[String]
list04=["aaa","bbb","ccc","ddd"]

list05::[Char]
list05=['a','b','c','d']
-- a list of chars is printed as a string
-- :info list05


list06::[Char]
list06="abcd"
-- we can just represent a list of chars as a string
-- question: haskell only understands ascii? not unicode?

main::IO()
main=do
    print list00
    print list01
    print list02
    -- print list03 -- this will generate infinitely the numbers during evaluation
    print (take 20 list03) -- use take to evaluate to just 20 values
    print list04
    print list05 -- "abcd"
    print list06

