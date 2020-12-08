import time

with open("input", 'r') as f:
  input_ = f.read()
  lines = [line for line in input_.split('\n') if line]
  grafs = [graf for graf in input_.split('\n\n') if graf]

class Rule:

  def __init__(self, color_, contents_d):
    self.color = ' '.join(color_)
    self.contents = contents_d

def parse_rule(line):
  words = [word for word in line.split(' ') if word]
  color = words[:2]
  contents_s = words[4:]
  num_contents = int(len(contents_s) / 4)
  contents_d = {}
  for i in range(num_contents):
    curr = 4 + 4*i
    if words[curr] != "no":
      contents_d[words[curr + 1] + ' ' + words[curr + 2]] = int(words[curr])
  result = Rule(color, contents_d)
  return result

rules = [parse_rule(line) for line in lines]

def part_one():
  part_one_colors = ["shiny gold"]

  def new_colors(colors_l):
    result = []
    for rule in rules:
      for color, num in rule.contents.items():
        if color in colors_l:
          result.append(rule.color)
    return result

  new_colors_l = new_colors(part_one_colors)
  while new_colors_l:
    for col in new_colors_l:
      if col not in part_one_colors:
        part_one_colors.append(col)
    new_colors_l = new_colors(part_one_colors)
    new_colors_l = [col for col in new_colors_l if col not in part_one_colors]
  return len(part_one_colors) - 1

t0 = time.perf_counter()
p1 = part_one()
t1 = time.perf_counter()
elapsed = t1 - t0

print(f"Part one: {p1}, {elapsed:0.3f} msec")

def nested(color):
  result = 0
  for rule in rules:
    if rule.color == color:
      for subcol, num in rule.contents.items():
        result += num * (1 + nested(subcol))
  return result

t0 = time.perf_counter()
p2 = nested("shiny gold")
t1 = time.perf_counter()
elapsed = t1 - t0

print(f"Part two: {p2}, {1e3 * elapsed:0.3f} msec")
