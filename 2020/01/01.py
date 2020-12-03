import time

with open("input1") as f:
  reports = [int(val) for val in f.readlines()]

def part_one():
  for i in reports:
    for j in reports:
      if i + j == 2020:
        return i * j

def part_two():
  for i in reports:
    for j in reports:
      for k in reports:
        if i + j + k == 2020:
          return i * j * k

t0 = time.perf_counter()
p1 = part_one()
t1 = time.perf_counter()
elapsed = t1 - t0

print(f"Part One: {p1:d}, {1e6 * elapsed:0.0f} µsec")

t0 = time.perf_counter()
p2 = part_two()
t1 = time.perf_counter()
elapsed = t1 - t0

print(f"Part Two: {p2:d}, {1e6 * elapsed:0.0f} µsec")

# recursive solution
# tail recursion uses accumulator to keep running product
# then I did a bunch of reading and found out python doesn't
# support tail-call optimization, woops

def prob_one(report_l, n, target, acc):
  if n == 0 or len(report_l) == 0:
    return None # not found

  if n == 1:
    if target in report_l:
      return target * acc

  for i in range(len(report_l)):
    subprob = [v for (j, v) in enumerate(report_l) if j != i]
    subsoln = prob_one(subprob, n - 1, target - report_l[i], acc * report_l[i])
    if subsoln:
      return subsoln

t0 = time.perf_counter()
p1 = prob_one(reports, 2, 2020, 1)
t1 = time.perf_counter()
elapsed = t1 - t0

print(f"Part One: {p1}, {1e6 * elapsed:0.3f} µsec")

t0 = time.perf_counter()
p1 = prob_one(reports, 3, 2020, 1)
t1 = time.perf_counter()
elapsed = t1 - t0

print(f"Part Two: {p1}, {1e6 * elapsed:0.3f} µsec")
