
a :: Int; a = 1234

-- it is not yet evaluated
:sprint a
:type a
a
:sprint a

b :: Integer; b = 2 ^ 70
:sprint b
:type b
b
:sprint b

import Data.List
:type intercalate
intercalate ":" ["/path/to/dir0", "/path/to/dir1"]

formatList s e sep xs = s ++ (intercalate sep (map show xs)) ++ e
formatList s e sep xs = s ++ (intercalate sep (map show xs)) ++ e

formatList "[" "]" "," ["1","2", "3"]
xs = ["1","2", "3"]
xs = ["a","b", "c"]
show xs
map show xs









