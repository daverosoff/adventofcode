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

def least_multiple_exceeding(modulus, bound):
  quotient = bound // modulus
  result = quotient * modulus
  while (result < bound):
    result += modulus
  return result

def gcd(a, b):
  if (a < b):
    return gcd(b, a)
  q, r = a // b, a % b
  if r == 0:
    return b
  else:
    return gcd(b, r)

def extended_euc(a, b):
  old_r, r = a, b
  old_s, s = 1, 0
  old_t, t = 0, 1

  while r != 0:
    quotient = old_r // r
    old_r, r = r, old_r - quotient * r
    old_s, s = s, old_s - quotient * s
    old_t, t = t, old_t - quotient * t

  return old_s, old_t

crcount = 0

def chinese_remainder(moduli_l, residues_l):
  global crcount
  crcount += 1
  if len(moduli_l) == 2:
    n1, n2 = moduli_l
    m1, m2 = extended_euc(n1, n2)
    a1, a2 = residues_l
    result = a1 * m2 * n2 + a2 * m1 * n1
    # while result < 0:
      # result += n1 * n2
    if result < 0:
      result %= n1 * n2
    return result
  else:
    # n1, n2 = moduli_l[:2]
    # a1, a2 = residues_l[:2]
    n12 = moduli_l[0] * moduli_l[1]
    a12 = chinese_remainder(moduli_l[:2], residues_l[:2])
    moduli_rest = moduli_l[2:]
    moduli_rest.append(n12)
    residues_rest = residues_l[2:]
    residues_rest.append(a12)
    return chinese_remainder(moduli_rest, residues_rest)

class Puzzle13(Puzzle):

  def __init__(self, filename="input"):
    super().__init__(filename)
    self.earliest = int(self.lines[0])
    self.conditions = []
    for entry in self.lines[1].split(','):
      if entry == 'x':
        self.conditions.append('x')
      else:
        self.conditions.append(int(entry))
    self.schedule = [entry for entry in self.conditions if entry != 'x']

  def part_one(self):
    earliest_id = None
    earliest_time = None
    for entry in self.schedule:
      current = least_multiple_exceeding(entry, self.earliest)
      if (not earliest_time) or (earliest_time > current):
        earliest_id = entry
        earliest_time = current
    return earliest_id * (earliest_time - self.earliest)

  def part_two(self):

    moduli = [entry for index, entry in enumerate(self.conditions) if entry != 'x']
    residues = [-index for index, entry in enumerate(self.conditions) if entry != 'x']
    result = chinese_remainder(moduli, residues)
    big_modulus = 1
    for mod in moduli:
      big_modulus *= mod
    result %= big_modulus
    return result


extended_euc(13,8)

p = Puzzle13("input")

t0 = time.perf_counter()
p1 = p.part_one()
t1 = time.perf_counter()
elapsed = t1 - t0
print(f"Part one: {p1} ({1000 * elapsed:0.3f} msec)")

t0 = time.perf_counter()
p2 = p.part_two()
t1 = time.perf_counter()
elapsed = t1 - t0
print(f"Part two: {p2} ({1000 * elapsed:0.3f} msec)")
print(f"{crcount} calls to chinese remainder")
