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

class Puzzle08(Puzzle):

  def __init__(self, filename="input"):
    super().__init__(filename)
    self.accumulator = 0
    self.pc = 0

  def parse_instr(self, instr):
    result = [tok for tok in instr.split(' ') if tok]
    result[1] = int(result[1])
    return result

  def execute_instr(self, opcode, arg):
    # if (opcode == 'nop'):
    if (opcode == "acc"):
      self.accumulator += arg
      self.pc += 1
    elif (opcode == "jmp"):
      self.pc += arg
    elif (opcode == "nop"):
      self.pc += 1
    else:
      raise ValueError

  def part_one(self, program):
    self.pc = 0
    self.accumulator = 0
    visited = []
    while (self.pc < len(program)):
      if self.pc not in visited:
        visited.append(self.pc)
      else:
        break
      opcode, arg = self.parse_instr(program[self.pc])
      self.execute_instr(opcode, arg)
    return self.accumulator

  def part_two(self):
    self.pc = 0
    self.accumulator = 0
    for i in range(len(self.lines)):
      program = self.lines[:]
      # target = program[i]
      if program[i][:3] == 'nop':
        program[i] = 'jmp' + program[i][3:]
      elif program[i][:3] == 'jmp':
        program[i] = 'nop' + program[i][3:]
      else:
        continue
      self.pc = 0
      self.accumulator = 0
      visited = []
      while (self.pc < len(program)):
        if self.pc not in visited:
          visited.append(self.pc)
        else:
          break
        opcode, arg = self.parse_instr(program[self.pc])
        self.execute_instr(opcode, arg)
      if self.pc == len(program):
        return self.accumulator


p = Puzzle08("input")
print(f"Part one: {p.part_one(p.lines)}")
print(f"Part two: {p.part_two()}")
