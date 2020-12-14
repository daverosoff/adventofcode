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

class Puzzle12(Puzzle):

  def init_helper(self):
    self.clock = 0
    self.x = 0
    self.y = 0
    self.dir = 0
    self.wp_x = 10
    self.wp_y = 1

  def __init__(self, filename="input"):
    super().__init__(filename)
    self.init_helper()
    self.instructions = []
    for line in self.lines:
      opcode, argument = line[0], int(line[1:])
      self.instructions.append((opcode, argument))

  def N(self, argument, part_two = False):
    if part_two:
      self.wp_y += argument
    else:
      self.y += argument

  def S(self, argument, part_two = False):
    if part_two:
      self.wp_y -= argument
    else:
      self.y -= argument

  def E(self, argument, part_two = False):
    if part_two:
      self.wp_x += argument
    else:
      self.x += argument

  def W(self, argument, part_two = False):
    if part_two:
      self.wp_x -= argument
    else:
      self.x -= argument

  def F(self, argument, part_two = False):
    if part_two:
      for i in range(argument):
        self.x += self.wp_x
        self.y += self.wp_y
    else:
      if self.dir % 360 == 0:
        self.E(argument)
      elif self.dir % 360 == 90:
        self.N(argument)
      elif self.dir % 360 == 180:
        self.W(argument)
      elif self.dir % 360 == 270:
        self.S(argument)
      else:
        raise ValueError

  def R(self, argument, part_two = False):
    if part_two:
      if argument % 360 == 0:
        pass
      elif argument % 360 == 90:
        self.wp_x, self.wp_y = self.wp_y, -self.wp_x
      elif argument % 360 == 180:
        self.wp_x, self.wp_y = -self.wp_x, -self.wp_y
      elif argument % 360 == 270:
        self.wp_x, self.wp_y = -self.wp_y, self.wp_x
      else:
        raise ValueError
    else:
      self.dir -= argument

  def L(self, argument, part_two = False):
    if part_two:
      if argument % 360 == 0:
        pass
      elif argument % 360 == 90:
        self.wp_x, self.wp_y = -self.wp_y, self.wp_x
      elif argument % 360 == 180:
        self.wp_x, self.wp_y = -self.wp_x, -self.wp_y
      elif argument % 360 == 270:
        self.wp_x, self.wp_y = self.wp_y, -self.wp_x
      else:
        raise ValueError
    else:
      self.dir += argument

  def execute(self, opcode, argument, part_two = False):
    print(f"After {self.clock} instructions: position ({self.x}, {self.y}), waypoint ({self.wp_x}, {self.wp_y})")
    if opcode == 'N':
      self.N(argument, part_two)
    elif opcode == 'S':
      self.S(argument, part_two)
    elif opcode == 'E':
      self.E(argument, part_two)
    elif opcode == 'W':
      self.W(argument, part_two)
    elif opcode == 'F':
      self.F(argument, part_two)
    elif opcode == 'R':
      self.R(argument, part_two)
    elif opcode == 'L':
      self.L(argument, part_two)
    self.clock += 1

  def part_one(self):
    self.init_helper()
    for opcode, argument in self.instructions:
      self.execute(opcode, argument)
    return abs(self.x) + abs(self.y)

  def part_two(self):
    self.init_helper()
    self.clock = 0
    self.x = 0
    self.y = 0
    self.wp_x = 10
    self.wp_y = 1
    for opcode, argument in self.instructions:
      self.execute(opcode, argument, True)
    return abs(self.x) + abs(self.y)

p = Puzzle12("input")
print(f"Part one: {p.part_one()}")
print(f"Part two: {p.part_two()}")
