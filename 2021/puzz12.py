sample = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

class Graph:
  def __init__(self, data):
    """data is a container of pairs of nodes."""
    # self.nodes = []
    self.edges = []
    for e in data:
      #ensure set
      e = set(e)
      if e not in self.edges:
        self.edges.append(e)

  class Path:
    def __init__(self, edges):
      self.nodes = ['start']
      for e in edges:
        assert(graph.other_vertex(e, 'start'))

  def __str__(self):
    return str(self.edges)

  def other_vertex(self, edge, node):
    a, b = edge
    return a if b == node else b

  def neighbors(self, node):
    adjacencies = [e for e in self.edges if node in e]
    neighbors = []
    for x, y in adjacencies:
      neighbors.append(x if y == node else y)
    return neighbors

def build_graph(data):
  """data is in the puzzle format."""
  edge_list = []
  for line in data.split('\n'):
    # for [x, y] in line.split('-'):
    x, y = line.split('-')
    edge_list.append(set((x,y)))
  # g = Graph(edge_list)
  # print(g.neighbors('b'))
  return Graph(edge_list)

def df_paths(graph, start='start', end='end'):
  paths = [[start]]
  for b in graph.neighbors(start):



# def part_one(graph):


print(build_graph(sample))
