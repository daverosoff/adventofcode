import Data.List (foldl1')
import Data.List (sortOn)
import Data.Maybe (fromJust)
import qualified Data.Map.Strict as Map

data Valve = Valve
  { flowRate :: Int
  , tunnels :: [String]
  } deriving (Show)

type Valves = Map.Map String Valve

data State = State
  { time :: Int
  , pressure :: Int
  , valves :: Valves
  , visited :: [String]
  } deriving (Show)

instance Eq Valve where
  v1 == v2 = flowRate v1 == flowRate v2 && tunnels v1 == tunnels v2
  v1 /= v2 = not (v1 == v2)

instance Eq State where
  s1 == s2 = time s1 == time s2 && pressure s1 == pressure s2 && valves s1 == valves s2 && visited s1 == visited s2
  s1 /= s2 = not (s1 == s2)

instance Ord State where
  compare s1 s2 = compare (pressure s1) (pressure s2)

-- Returns a list of all the possible next states given a current state
nextStates :: State -> [State]
nextStates (State t p vs lv) =
  let openable = filter ((/= 0) . flowRate . (vs Map.!)) $ filter (`notElem` lv) $ Map.keys vs
      visited' = lv ++ openable
      withOpen = map (\name -> State (t + 1) (p + flowRate (vs Map.! name)) (Map.insert name (vs Map.! name) vs) visited') openable
      withoutOpen = map (\name -> State (t + 1) p vs visited') $ filter (`notElem` visited') $ concatMap tunnels $ map (vs Map.!) openable
  in withoutOpen ++ withOpen

-- Returns the maximum pressure that can be released by the valves
maxPressure :: Valves -> Int
maxPressure vs = pressure $ fromJust $ search 30 vs (State 0 0 vs ["AA"])
  where
    search 0 vs' state = Nothing
    search t vs' state =
      let next = nextStates state
      in if null next
           then Just state
           else maximum $ map (search (t - 1) vs') next

-- correction 3b

-- Returns the maximum pressure that can be released by the valves
-- maxPressure :: Valves -> Int
-- maxPressure vs = pressure $ search 30 vs (State 0 0 vs ["AA"])
--   where
--     search 0 state = state
--     search t state =
--       let next = nextStates state
--       in if null next
--            then state
--            else foldl1' (\s1 s2 -> if pressure s1 > pressure s2 then s1 else s2) $ map (search (t - 1)) next

main :: IO ()
main = do
  let valves = Map.fromList
        [ ("AA", Valve 0 ["DD", "II", "BB"])
        , ("BB", Valve 13 ["CC", "AA"])
        , ("CC", Valve 2 ["DD", "BB"])
        , ("DD", Valve 20 ["CC", "AA", "EE"])
        , ("EE", Valve 3 ["FF", "DD"])
        , ("FF", Valve 0 ["EE", "GG"])
        , ("GG", Valve 0 ["FF", "HH"])
        , ("HH", Valve 22 ["GG"])
        , ("II", Valve 0 ["AA", "JJ"])
        , ("JJ", Valve 21 ["II"])
        ]
  print $ maxPressure valves
