-- we read this as: 'main has type IO unit'
main :: IO ()
main = do
    -- we read this as: 'content is drawn from readFile "numbers.txt"'
    content <- readFile "numbers.txt"
    -- putStrLn "Hello World"
    putStrLn content
    -- print content -- this is raw
