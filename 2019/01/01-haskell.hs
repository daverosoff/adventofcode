import Data.Char

main = do
    contents <- getContents
    let allLines = lines contents
        allFuels = map lineToInt allLines
    putStrLn . show . aoc01'1 $ allFuels
    putStrLn . show . aoc01'2 $ allFuels

aoc01'1 = sum . map getFuel

aoc01'2 = sum . map getFuelRec

lineToInt :: [Char] -> Int
lineToInt xs =
    let
        digits = map digitToInt xs
        little = reverse digits
        powers = iterate (10*) 1
    in
        sum $ zipWith (*) little powers

fuel :: Int -> Int
fuel mass = mass `div` 3 - 2

getFuel :: Int -> Int
getFuel mass = max (fuel mass) 0

getFuelRec :: Int -> Int
getFuelRec = sum . tail . takeWhile (> 0) . iterate getFuel


