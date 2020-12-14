import time

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


class Puzzle10(Puzzle):
  def __init__(self, filename="input"):
    super().__init__(filename)
    self.voltages = [int(line) for line in self.lines]
    self.voltages.append(max(self.voltages) + 3)
    self.voltages.append(0)
    self.sorted_voltages = sorted(self.voltages)

  def part_one(self):
    diffs = [self.sorted_voltages[i+1] - self.sorted_voltages[i]
      for i in range(len(self.sorted_voltages) - 1)]
    result = dict([(x, diffs.count(x)) for x in diffs])
    diff1, diff3 = result[1], result[3]
    return diff1 * diff3

  class Node:
    def __init__(self, value_v):
      self.values = sorted(value_v)
      self.children = []

    def check_child(self, chain):
      for child in self.children:
        if child.values == chain:
          return True
      return False

    def check_descendants(self):
      if len(self.values) == 1:
        return
      for cursor in self.values:
        omit = [val for val in self.values if val != cursor]
        if all([not self.check_child(omit) for child in self.children]):
          self.children.append(Puzzle10.Node(omit))
      # [self.check_descendants() for child in self.children]

    def count_leaves(self):
      if not self.children:
        return 1
      else:
        return sum([child.count_leaves() for child in self.children])

  def part_two(self, values_v):
    root = self.Node(self.sorted_voltages)
    root.check_descendants()
    return root.count_leaves()

p = Puzzle10("test")
p1 = p.part_one()
print(f"Part one: {p1}")
p2 = p.part_two(p.sorted_voltages)
print(f"Part two: {p2}")
