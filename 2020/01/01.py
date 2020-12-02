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

print("Part One: {}".format(part_one()))
print("Part Two: {}".format(part_two()))

# recursive solution

def prob_one(report_l, n, target):
  if n == 0 or len(report_l) == 0:
    return None # not found

  if n == 1:
    if target in report_l:
      return target

  for i in range(len(report_l)):
    subprob = [v for (j, v) in enumerate(report_l) if j != i]
    subsoln = prob_one(subprob, n-1, target - report_l[i])
    if subsoln:
      return report_l[i] * subsoln

print("Part One: {}".format(prob_one(reports, 2, 2020)))
print("Part Two: {}".format(prob_one(reports, 3, 2020)))
