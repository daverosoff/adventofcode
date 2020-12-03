import time

with open("input", 'r') as f:
  ourmap = [line[:-1] for line in f.readlines()]

def count_trees(ourmap, deltax, deltay):
  result = 0
  x = 0
  y = 0

  while y < len(ourmap):
    if ourmap[y][x] == '#':
      result += 1
    x = (x + deltax) % len(ourmap[0])
    y += deltay

  return result

tic = time.perf_counter()
p0 = count_trees(ourmap, 3, 1)
toc = time.perf_counter()
print(f"Part One: {p0:d}, {1e6*(toc-tic):0.0f} µsec")

part_two = 1
tic = time.perf_counter()
part_two *= count_trees(ourmap, 1,1)
part_two *= count_trees(ourmap, 3,1)
part_two *= count_trees(ourmap, 5,1)
part_two *= count_trees(ourmap, 7,1)
part_two *= count_trees(ourmap, 1,2)
toc = time.perf_counter()
print(f"Part Two: {part_two:d}, {1e6*(toc-tic):0.0f} µsec")
