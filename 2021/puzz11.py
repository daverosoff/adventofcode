from collections import deque
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

s2 = """11111
19991
19191
19991
11111"""

puzz11 = """5665114554
4882665427
6185582113
7762852744
7255621841
8842753123
8225372176
7212865827
7758751157
1828544563
"""

class Grid:

  def __init__(self, puzzle):
    self.g = [[int(x) for x in row] for row in puzzle.split('\n')][:-1]
    self.ymax = len(self.g) - 1
    self.xmax = len(self.g[0]) - 1
    self.flashes = 0
    self.all_flash = None
    self.step = 0

  def is_valid(self, x, y, dx, dy):
    return (dx != 0 or dy != 0) and 0 <= x + dx <= self.xmax and 0 <= y + dy <= self.ymax

  def neighbors(self, x, y):
    return [(x + dx, y + dy) for dx in range(-1, 2) for dy in range(-1, 2)
      if self.is_valid(x, y, dx, dy)]

  def neighbors_with_value_at_least(self, x, y, value):
    return [n for n in self.neighbors(x, y) if self.g[n[1]][n[0]] >= value]

  def increment_grid(self):
    for y in range(self.ymax + 1):
      for x in range(self.xmax + 1):
        self.increment(x, y)

  def increment(self, x, y):
    self.g[y][x] += 1

  def reset_energy(self, x, y):
    for y in range(self.ymax + 1):
      for x in range(self.xmax + 1):
        if self.g[y][x] >= 10:
          self.g[y][x] = 0
          for n in self.neighbors(x, y):
            i, j = n[0], n[1]
            if 0 < self.g[j][i] < 10:
              self.increment(i, j)

  def do_step(self):
    self.increment_grid()
    for y in range(self.ymax + 1):
      for x in range(self.xmax + 1):
        self.reset_energy(x, y)
    tens = self.neighbors_with_value_at_least(x, y, 10)
    while tens:
      for ten in tens:
        self.reset_energy(ten[0], ten[1])
      tens = self.neighbors_with_value_at_least(x, y, 10)
    self.step += 1
    step_flashes = len([(i, j) for i in range(self.xmax + 1) for j in
    range(self.ymax + 1) if self.g[i][j] == 0])
    if step_flashes == len(self.g) * len(self.g[0]):
      self.all_flash = self.step
    self.flashes += step_flashes

  def part_one(self):
    while self.step < 100:
      self.do_step()
    print(f"Part one: {self.flashes}")

  def part_two(self):
    while True:
      self.do_step()
      if self.all_flash:
        print(f"Part two: {self.all_flash}")
        return

g = Grid(puzz11)
g.part_one()
g.part_two()

# def increment(g):
#   # over = np.where(lambda t: t == 0, 1, 0)
#   xmax = len(g) - 1
#   ymax = len(g[0]) - 1
#   # flashes = np.select([g == 0], [np.ones(g.shape, int)], 0)
#   return g + 1

# def flash(g):
#   # over = [0 if x <= 9 else 1 for x in g if x >= 0]
#   done = not g[g > 9].size > 0
#   while not done:
#     # g[g > 9] = 0
#     flashes = np.select(g == 10, np.ones(g.shape, int), 0)
#     print(flashes)

#   return(g)

# def part_one(arr):
  # height, width = (lambda t: (len(t), len(t[0])))(arr.split('\n'))

  # values = [[int(x) for x in row] for row in arr.split('\n')]

  # grid = np.array(values, int).reshape(height, width)

  # print(grid)
  # print(increment(grid))
  # print(flash(increment(grid)))

# part_one(s2)

