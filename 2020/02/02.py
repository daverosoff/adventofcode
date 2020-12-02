with open("input1", 'r') as f:
  policies = f.readlines()

part_one = 0
part_two = 0

for pol in policies:
  # format is mm-nn x: ppppppppp
  mn, xx, pp = pol.split(' ')
  m, n = mn.split('-')
  m = int(m)
  n = int(n)
  x = xx[0]
  count = len([ch for ch in pp if ch == x])
  if (m <= count) and (count <= n):
    part_one += 1
  if (pp[m-1] == x) != (pp[n-1] == x):
    part_two += 1

print("Part One: {}".format(part_one))
print("Part Two: {}".format(part_two))
