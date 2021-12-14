Data Direction = L | R | D | U
                 deriving (Read, Show, Eq, Enum)

Data Segment = Segment { dir :: Direction,
                         dist :: Int
                       } deriving (Read, Show, Eq, Enum)


wordToSegment d:ds = Segment d (lineToInt ds)

lineToInt :: [Char] -> Int
lineToInt xs =
    let
        digits = map digitToInt xs
        little = reverse digits
        powers = iterate (10*) 1
    in
        sum $ zipWith (*) little powers