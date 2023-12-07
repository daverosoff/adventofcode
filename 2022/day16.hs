import Data.List
import qualified Data.Map as Map

data Valve = Valve
  { flowRate :: Int
  , tunnels :: [String]
  } deriving (Show)

instance Eq Valve where
  v1 == v2 = flowRate v1 == flowRate v2 && tunnels v1 == tunnels v2
  v1 /= v2 = not (v1 == v2)

type Valves = Map.Map String Valve

data State = State
  { time :: Int
  , pressure :: Int
  , location :: String
  , valves :: Valves
  , visited :: [String]
  , opened :: [String]
  } deriving (Show)

instance Eq State where
  s1 == s2 =
    let t = time s1 == time s2
        p = pressure s1 == pressure s2
        lo = location s1 == location s2
        vs = valves s1 == valves s2
        vis = visited s1 == visited s2
        op = opened s1 == opened s2
    in t && p && lo && vs && vis && op
  s1 /= s2 = not (s1 == s2)

instance Ord State where
  compare s1 s2 = compare (pressure s1) (pressure s2)

-- nextStates :: State -> [State]
-- nextStates (State t p lo vs vis op) =
--   let neighbors = tunnels $ (Map.! vs) lo
      -- openable = filter ((/= 0) . flowRate . Map.! vs) $ filter (`notElem` vis) neighbors

-- neighbors :: Valves -> String -> [Valve]
-- neighbors name vs = tunnels $ Map.lookup vs name

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
  let next_valves = mapM_ putStrLn t
    where v = Map.lookup "AA" valves
          t = tunnels v
  
  -- print $ tunnels "AA"
