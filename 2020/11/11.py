import numpy as np

class Puzzle:

  def __init__(self, filename="input"):
    with open(filename, 'r') as f:
      self.input = f.read()
    self.lines = [line for line in self.input.split("\n") if line]
    self.paragraphs = [graf for graf in self.input.split("\n\n") if graf]

  def part_one(self):
    raise NotImplementedError

  def part_two(self):
    raise NotImplementedError

class Puzzle11(Puzzle):

  def __init__(self, filename="input"):
    super().__init__(filename)
    self.height = len(self.lines)
    self.width = len(self.lines[0])
    unstrung = np.array([x for line in self.lines for x in line])
    self.grid = np.array(unstrung).reshape(self.height, self.width)
    self.clock = 0

  def count_occupied_neighbors(self, row, col):
    result = 0
    if col > 0: # away from left edge
      if self.is_occupied(row, col - 1):
        result += 1
      if row > 0:
        if self.is_occupied(row - 1, col - 1):
          result += 1
        if self.is_occupied(row - 1, col):
          result += 1
      if row < self.height - 1:
        if self.is_occupied(row + 1, col - 1):
          result += 1
        if self.is_occupied(row + 1, col):
          result += 1
    if col < self.width - 1:
      if self.is_occupied(row, col + 1):
        result += 1
      if row > 0:
        if self.is_occupied(row - 1, col - 1):
          result += 1
      if row < self.height - 1:
        if self.is_occupied(row + 1, col - 1):
          result += 1
    return result

  def is_occupied(self, row, col):
    return self.grid[row][col] == '#'

  def is_empty(self, row, col):
    return self.grid[row][col] == 'L'

  def will_fill(self, row, col):
    return self.is_occupied(row, col) and self.count_occupied_neighbors(row, col) == 0

  def will_empty(self, row, col):
    return self.is_occupied(row, col) and self.count_occupied_neighbors(row, col) >= 4

  def next_grid(self):
    result = []
    for i in range(self.height):
      row = []
      for j in range(self.width):
        if self.is_empty(i, j):
          if self.will_fill(i, j):
            row.append('#')
          else:
            row.append('L')
        elif self.is_occupied(i, j):
          if self.will_empty(i, j):
            row.append('L')
          else:
            row.append('#')
        else:
          row.append('.')
      result.append(row)
    return np.array(result)

  def advance_clock(self):
    self.grid = self.next_grid()
    self.clock += 1

  def is_stable(self):
    next_grid = self.next_grid()
    if self.grid.shape == next_grid.shape:
      return (self.grid == next_grid).all()
    else:
      raise ValueError

  def part_one(self):
    while not self.is_stable():
      self.advance_clock()
    result = np.count_nonzero(self.grid == '#')
    return result

p = Puzzle11("input")
p1 = p.part_one()
print(f"Part one: {p1} after {p.clock} steps")
