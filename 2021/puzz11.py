import numpy as np

sample = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

height, width = (lambda t: (len(t), len(t[0])))(sample.split('\n'))

values = [int(x) for row in sample.split('\n') for x in row]

grid = np.array(values, int).reshape(height, width)

def neighbors(x, y, xmax, ymax):
  return [(x + dx, y + dy) for dx in range(-1, 2) for dy in range(-1, 2)
    if 0 <= x + dx < xmax and 0 <= y + dy < ymax]

def increment(g):
  # over = np.where(lambda t: t == 0, 1, 0)
  xmax = len(g) - 1
  ymax = len(g[0]) - 1
  flashes = np.select([g == 0], [np.ones(g.shape, int)], 0)
  return g + flashes + 1

def flash(g):
  # over = [0 if x <= 9 else 1 for x in g if x >= 0]
  while g[g > 9].size > 0:
    g[g > 9] = 0
    flashes = np.select([g == 0], [np.ones(g.shape, int)], 0)
  return(g)

print(grid)
print(increment(grid))
print(flash(grid))
# print(increment(grid))
# print(flash(grid))