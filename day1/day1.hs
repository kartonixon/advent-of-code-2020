-- Advent of Code 2020 Day 1

getNumbers :: String -> [Integer]
getNumbers str = map read (lines str) :: [Integer]

main = do
    contents <- readFile "input.txt"
    let numbers = getNumbers contents

    -- PART 1
    print(filter (>0) [if (x + y == 2020) then x*y else 0 | x<-numbers, y<-numbers])
    
    -- PART 2 
    print(filter (>0) [if (x + y + z == 2020) then x*y*z else 0 | x<-numbers, y<-numbers, z<-numbers])
