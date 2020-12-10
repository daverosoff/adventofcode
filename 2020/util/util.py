class Puzzle:

  def __init__(self, filename="input"):
    with open(filename, 'r') as f:
      self.input = f.read()
    self.lines = [line for line in self.input.split("\n") if line]
    self.paragraphs = [graf for graf in self.input.split("\n\n") if graf]

  def input(self):
    return self.input

  def lines(self):
    return self.lines

  def paragraphs(self):
    return self.paragraphs

  def part_one(self):
    raise NotImplementedError

  def part_two(self):
    raise NotImplementedError
