import Data.List


-- we can parenthesize to make more evident how to write those function
--  those are lambda functions which only receive a single parameter
formatList::String->(String->(String->([String]->String)))
-- formatList::String->String->String->[String]->String
formatList start end separator xs = start ++ (intercalate separator (map show xs)) ++ end


main::IO()
main = putStrLn $ formatList "<list>" "</list>" "|" ["first","second","third","fourth"]