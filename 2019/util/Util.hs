module Util
( lineToInt
), where

lineToInt :: [Char] -> Int
lineToInt xs =
    let
        digits = map digitToInt xs
        little = reverse digits
        powers = iterate (10*) 1
    in
        sum $ zipWith (*) little powers