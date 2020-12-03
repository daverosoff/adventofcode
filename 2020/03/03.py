import time

with open("input", 'r') as f:
  ourmap = [line[:-1] for line in f.readlines()]

def count_trees(ourmap, dx, dy):
  result = 0
  x = 0
  y = 0

  while y < len(ourmap):
    if ourmap[y][x] == '#':
      result += 1
    x = (x + dx) % len(ourmap[0])
    y += dy

  return result

tic = time.perf_counter()
p1 = count_trees(ourmap, 3, 1)
toc = time.perf_counter()
print(f"Part One: {p1}, {1e6 * (toc - tic):0.3f} µsec")

p2 = 1 # empty product, initial value of accumulation
tic = time.perf_counter()
p2 *= count_trees(ourmap, 1, 1)
p2 *= count_trees(ourmap, 3, 1)
p2 *= count_trees(ourmap, 5, 1)
p2 *= count_trees(ourmap, 7, 1)
p2 *= count_trees(ourmap, 1, 2)
toc = time.perf_counter()
print(f"Part Two: {p2}, {1e6 * (toc - tic):0.3f} µsec")
