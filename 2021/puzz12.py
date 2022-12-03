import string

sample = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

sample2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

sample3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

puzz12 = """end-MY
MY-xc
ho-NF
start-ho
NF-xc
NF-yf
end-yf
xc-TP
MY-qo
yf-TP
dc-NF
dc-xc
start-dc
yf-MY
MY-ho
EM-uh
xc-yf
ho-dc
uh-NF
yf-ho
end-uh
start-NF"""

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

  def __str__(self):
    return str(self.edges)

  def other_vertex(self, edge, node):
    a, b = edge
    return a if b == node else b

  def neighbors(self, node):
    adjacencies = [e for e in self.edges if node in e]
    neighbors = []
    for e in adjacencies:
      neighbors.append(self.other_vertex(e, node))
    return neighbors

  def is_big(self, node):
    return node.isupper()

  def extend_path(self, path, part=2):
    new_paths = []
    last = path[-1]
    naybs = self.neighbors(last)
    def is_extended():
      return any([n.islower() and path.count(n) == 2 for n in path])
    if part == 1:
      for n in naybs:
        if self.is_big(n) or n not in path:
          new_paths.append(path + [n])
    else:
      for n in naybs:
        if self.is_big(n):
          new_paths.append(path + [n])
        elif n not in ('start', 'end') and path.count(n) <= 1:
          pc = path.count(n)
          if pc == 0:
            new_paths.append(path + [n])
          if pc == 1 and not is_extended():
            new_paths.append(path + [n])
        elif n == 'end' and n not in path:
          new_paths.append(path + [n])

    return new_paths

def build_graph(data):
  """data is in the puzzle format."""
  edge_list = []
  for line in data.split('\n'):
    x, y = line.split('-')
    edge_list.append(set((x,y)))
  return Graph(edge_list)

for i in (1, 2):
  b = build_graph(puzz12)
  paths = ['start']
  next_paths = b.extend_path(paths, i)
  result = []
  while next_paths:
    next_paths_end = [p for p in next_paths if p[-1] == 'end']
    result += [p for p in next_paths_end if p not in result]
    next_paths = [b.extend_path(path, i) for path in next_paths]
    next_paths = [item for subl in next_paths for item in subl]
  print(f"part {i}: {len(result)}")


