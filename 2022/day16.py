sample = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

def build_graph(inp):
    graph = {}
    for line in inp.splitlines():
        parts = line.split(';')
        name = parts[0].split()[1]
        flow = int(parts[0].split('=')[1])
        graph[name] = (flow, [x[:2] for x in parts[1].split()[4:]])
    return graph

# def max_pressure_release(graph, start):

def dijkstra(graph, start, end, time):
    dist = {start: 0}
    prev = {}
    q = set(graph.keys())
    while q:
        u = max(q, key=lambda x: dist.get(x, float('-inf')))
        q.remove(u)
        if u == end:
            break
        for v in graph[u][1]:
            alt = dist[u] + graph[v][0] * (30 - time - 2)
            if alt > dist.get(v, float('-inf')):
                dist[v] = alt
                prev[v] = u
    return dist, prev

def part_one(inp):
    g = build_graph(inp)
    time = 0


part_one(sample)