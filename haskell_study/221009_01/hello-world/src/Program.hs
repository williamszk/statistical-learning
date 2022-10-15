main :: IO()
-- :: is pronounced has type
-- () is called a "unit" it is a tuple with no elements
main = do
    -- <- is called "from"
    content <- readFile "./src/numbers.txt"
    putStrLn content
    -- print content