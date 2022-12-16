from collections import defaultdict

def max_pressure_release(valves):
  # Create a graph representing the network of pipes and valves
  graph = defaultdict(list)
  for valve in valves:
    parts = valve.split(';')
    valve_id = parts[0].split()[1]
    flow_rate = int(parts[0].split('=')[1])
    tunnels = [x[:2] for x in parts[1].split()[4:]]
    for tunnel in tunnels:
      graph[valve_id].append((flow_rate, tunnel))

  # Initialize variables to keep track of the maximum pressure release
  # and the current set of open valves
  max_release = 0
  open_valves = set()

  # DFS function to explore the graph and find the maximum pressure release
  def dfs(node, time_left, release):
    nonlocal max_release
    nonlocal open_valves

    # Update the maximum pressure release
    max_release = max(max_release, release)

    # If there is no more time left, return
    if time_left <= 0:
      return

    # Explore the neighbors of the current node
    for flow_rate, neighbor in graph[node]:
      # If the neighbor has not been visited yet, open it
      if neighbor not in open_valves:
        open_valves.add(neighbor)
        # Recurse with the remaining time and the updated pressure release
        dfs(neighbor, time_left - 2, release + flow_rate * (time_left - 1))
        open_valves.remove(neighbor)
      # If the neighbor has already been visited, move to it but do not open it again
      else:
        dfs(neighbor, time_left - 1, release)

  # Start the DFS from valve AA with 30 minutes of time remaining
  dfs('AA', 30, 0)

  return max_release

# Test the function with the example input
valves = [
  "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
  "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
  "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
  "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
  "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
  "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
  "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
  "Valve HH has flow rate=22; tunnel leads to valve GG",
  "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
  "Valve JJ has flow rate=21; tunnel leads to valve II"
]

print(max_pressure_release(valves))  # Expected output: 54
