import numpy as np

sample = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944582
"""

sample2 = """19999
19111
11191
"""

import numpy as np
import pythonds3

class Record:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __lt__(self, other):
        return self.key < other.key
    
    def __le__(self, other):
        return self.key <= other.key

    def __eq__(self, other):
        return self.key == other.key

class MinPriorityQueue(pythonds3.BinaryHeap):
    def add_with_priority(self, key, value):
        self.insert(Record(key, value))
    # def decrease_priority    

class Graph:
    def __init__(self, input: str):
        lines = input.splitlines()
        rows = len(lines)
        cols = len(lines[0])
        self.vertices = np.fromstring(input).reshape(rows, cols)
        self.edges = {
            (x + dx, y + dy)
        }
    
    def neighbors(self, v):
        pass

def dijkstra(graph, init):
    dist = {}
    prev = {}
    dist[init] = 0

    pq = MinPriorityQueue()

    for v in graph.vertices:
        if v != init:
            dist[v] = float("inf")

        pq.add_with_priority(v, dist[v])

    while pq:
        u = pq.get_min()
        for v in graph.neighbors(u):
            if v.value not in [x.value for x in pq]:
                alt = dist[u] + graph.edges(u, v)
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    # pq.decrease_priority(v, alt)
    
    return dist, prev

with open("input15.dat") as f:
    lines = f.read()

# puzzle = build_risk_table(lines)
risks = build_risk_table(sample)
cum_risks = risks.copy()
cum_risks = populate(risks, cum_risks)
print(cum_risks)
