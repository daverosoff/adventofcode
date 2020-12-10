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

class Puzzle09(Puzzle):

  def __init__(self):
    super().__init__()
    self.lines = [int(line) for line in self.lines]

  def part_one(self, preamble_length):
    code = self.lines[:]
    for i in range(preamble_length, len(code)):
      current_pre = code[i - preamble_length:i]
      sums = [k + j for k in current_pre for j in current_pre if k != j]
      if code[i] not in sums:
        return code[i]
    return 0

  def part_two(self, target):
    for ngram_length in range(2, len(self.lines) - 1):
      for i in range(len(self.lines) - ngram_length):
        current_ngram = self.lines[i:i + ngram_length]
        if sum(current_ngram) == target:
          return max(current_ngram) + min(current_ngram)

p = Puzzle09()

t0 = time.perf_counter()
p1 = p.part_one()
t1 = time.perf_counter()
elapsed = t1 - t0
print(f"Part one: {p1}, {1000 * elapsed:0.3f} msec")

t0 = time.perf_counter()
p2 = p.part_two(p1)
t1 = time.perf_counter()
elapsed = t1 - t0
print(f"Part two: {p2}, {1000 * elapsed:0.3f} msec")
