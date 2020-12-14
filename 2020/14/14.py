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

class Puzzle14(Puzzle):

  def __init__(self, filename="input"):
    super().__init__(filename)
    self.mem = {}
    self.mask = self.lines[0]
    self.pc = 1

  def fetch(self, address):
    if address in self.mem.keys():
      return self.mem[address]
    else:
      raise ValueError

  def apply_mask(self, value):
    masked = value
    for place, bit in enumerate(self.mask):
      if bit == '1':
        masked |= 2**(len(self.mask) - 1 - place)
      if bit == '0':
        masked &= 2**36 - 1 - 2**(len(self.mask) - 1 - place)
    return masked

  def apply_mask_two(self, value, values_rec = []):
    for place, bit in enumerate(self.mask):
      if bit == '1':
        masked |= 2**(len(self.mask) - 1 - place)
    place = self.mask.find('X')
        with_zero = 2**36 - 1 - 2**(len(self.mask) - 1 - place)
        with_one  = 2**(len(self.mask) - 1 - place)
        values_rec.append(with_zero)
        values_rec.append(with_one)


  def part_one(self):
    while self.pc < len(self.lines):
      current_line = self.lines[self.pc]
      if current_line[:7] == "mask = ":
        self.mask = current_line[7:]
        self.pc += 1
      else:
        address_b = current_line.find('[') + 1
        address_e = current_line.find(']')
        value_b = current_line.find('=') + 2
        address = int(current_line[address_b : address_e])
        value = int(current_line[value_b:])
        self.mem[address] = self.apply_mask(value)
        self.pc += 1
    result = 0
    for value in self.mem.values():
      result += value
    return result

  def part_two(self):
    while self.pc < len(self.lines):
      current_line = self.lines[self.pc]
      if current_line[:7] == "mask = ":
        self.mask = current_line[7:]
        self.pc += 1
      else:


p = Puzzle14("input")
print(p.part_one())
